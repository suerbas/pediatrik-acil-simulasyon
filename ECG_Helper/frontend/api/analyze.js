/**
 * Vercel Serverless Function (ESM - frontend Root Directory kurulumu için): /api/analyze
 *   GET  -> sunucuda ortam değişkeniyle tanımlı bir anahtar olup olmadığını bildirir (anahtarı döndürmez).
 *   POST -> Ortam değişkenlerinden (OPENROUTER_API_KEY / GEMINI_API_KEY / OPENAI_API_KEY)
 *           güvenli şekilde çok-modlu (multimodal) EKG analizi yapar.
 * Sunucu tarafında anahtar tanımlı değilse HTTP 200 ile { mode: "no_server_key" }
 * döndürerek istemcinin kendi anahtarına veya demo simülasyonuna düşmesine izin verir.
 *
 * NOT: Bu dosya ile kök dizindeki api/analyze.js aynı mantığı içerir (CommonJS / ESM farkı dışında);
 * birinde yapılan değişiklik diğerine de uygulanmalıdır.
 */

const CLINICAL_DISCLAIMER =
  "Bu çıktı yapay zekâ klinik karar destek analizidir; kesin tanı ve tedavi kararı hekim değerlendirmesi gerektirir.";

const MAX_IMAGES = 6; // 1 tam görüntü + 5 anatomik bölge kırpması
const MAX_PROMPT_CHARS = 60000;
const UPSTREAM_TIMEOUT_MS = 120000;

const EXPECTED_STEP_KEYS = [
  "step1_calibration_quality",
  "step2_rate_rhythm",
  "step3_axis",
  "step4_intervals",
  "step5_morphology_st_t",
  "step6_clinical_synthesis",
];

function extractJsonBlock(rawText) {
  if (!rawText || typeof rawText !== "string") {
    throw new Error("Model boş yanıt döndürdü.");
  }
  const trimmed = rawText.trim();
  const fenced = trimmed.match(/```(?:json)?\s*([\s\S]*?)```/i);
  const candidate = fenced ? fenced[1].trim() : trimmed;

  let parsed;
  try {
    parsed = JSON.parse(candidate);
  } catch {
    const start = candidate.indexOf("{");
    const end = candidate.lastIndexOf("}");
    if (start === -1 || end <= start) {
      throw new Error("Model yanıtından geçerli JSON ayrıştırılamadı.");
    }
    try {
      parsed = JSON.parse(candidate.slice(start, end + 1));
    } catch {
      throw new Error("Model yanıtından geçerli JSON ayrıştırılamadı.");
    }
  }

  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    throw new Error("Model çıktısı bir JSON nesnesi değil.");
  }
  if (!EXPECTED_STEP_KEYS.some((k) => parsed[k] && typeof parsed[k] === "object")) {
    throw new Error("Model çıktısında beklenen 6 adımlı şema alanları bulunamadı.");
  }
  return parsed;
}

function resolveServerProvider(requestedProvider, requestedModel) {
  const openrouterKey = (process.env.OPENROUTER_API_KEY || "").trim();
  const geminiKey = (process.env.GEMINI_API_KEY || "").trim();
  const openaiKey = (process.env.OPENAI_API_KEY || "").trim();

  // İstemcinin model seçimi yalnızca istenen sağlayıcı gerçekten kullanılacaksa geçerlidir.
  // Aksi halde (ör. istemci "gemini-2.0-flash" istedi ama sunucuda yalnızca OpenRouter anahtarı var)
  // model adı başka sağlayıcıya taşınır ve çağrı "model bulunamadı" hatasıyla düşer.
  const pick = (prov, model) => {
    if (prov === "openrouter" && openrouterKey) {
      return {
        provider: "openrouter",
        apiKey: openrouterKey,
        baseUrl: (process.env.OPENROUTER_BASE_URL || "https://openrouter.ai/api/v1").replace(/\/+$/, ""),
        model: model || process.env.OPENROUTER_MODEL || "google/gemini-3.8-flash",
      };
    }
    if (prov === "gemini" && geminiKey) {
      return {
        provider: "gemini",
        apiKey: geminiKey,
        model: model || process.env.GEMINI_MODEL || "gemini-2.0-flash",
      };
    }
    if (prov === "openai" && openaiKey) {
      return {
        provider: "openai",
        apiKey: openaiKey,
        baseUrl: "https://api.openai.com/v1",
        model: model || process.env.OPENAI_MODEL || "gpt-4o",
      };
    }
    return null;
  };

  return (
    pick(requestedProvider, requestedModel) ||
    pick("openrouter", "") ||
    pick("openai", "") ||
    pick("gemini", "")
  );
}

function fetchWithTimeout(url, options) {
  return fetch(url, { ...options, signal: AbortSignal.timeout(UPSTREAM_TIMEOUT_MS) });
}

async function callOpenAiCompatible({ apiKey, baseUrl, model, prompt, images, isOpenRouter, referer }) {
  const contentParts = [{ type: "text", text: prompt }];
  for (const img of images) {
    if (img.label) contentParts.push({ type: "text", text: img.label });
    contentParts.push({ type: "image_url", image_url: { url: img.uri, detail: "high" } });
  }

  const headers = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  };
  if (isOpenRouter) {
    headers["HTTP-Referer"] = referer || "https://ecg-helper.vercel.app";
    headers["X-Title"] = "ECG_Helper";
  }

  const endpoint = `${baseUrl}/chat/completions`;
  const baseBody = {
    model,
    messages: [{ role: "user", content: contentParts }],
  };

  let res = await fetchWithTimeout(endpoint, {
    method: "POST",
    headers,
    body: JSON.stringify({ ...baseBody, temperature: 0.15, response_format: { type: "json_object" } }),
  });

  // Yalnızca "parametre desteklenmiyor" türü hatalarda (400/422) yalın istekle yinele.
  // 401/402/429 gibi hatalarda aynı isteği tekrarlamak kota tüketmekten başka işe yaramaz.
  if (res.status === 400 || res.status === 422) {
    res = await fetchWithTimeout(endpoint, {
      method: "POST",
      headers,
      body: JSON.stringify(baseBody),
    });
  }

  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`Upstream API hatası (${res.status}): ${errText.slice(0, 240)}`);
  }

  const data = await res.json();
  return extractJsonBlock(data?.choices?.[0]?.message?.content);
}

async function callGemini({ apiKey, model, prompt, images }) {
  const parts = [{ text: prompt }];
  for (const img of images) {
    const match = /^data:(image\/[a-zA-Z0-9.+-]+);base64,(.+)$/s.exec(img.uri);
    if (!match) continue;
    if (img.label) parts.push({ text: img.label });
    parts.push({ inline_data: { mime_type: match[1], data: match[2] } });
  }

  // Anahtar URL sorgu dizesi yerine başlıkta gönderilir (URL'ler erişim günlüklerine yazılır)
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(
    model
  )}:generateContent`;

  const res = await fetchWithTimeout(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "x-goog-api-key": apiKey },
    body: JSON.stringify({
      contents: [{ parts }],
      generationConfig: { responseMimeType: "application/json", temperature: 0.15 },
    }),
  });

  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`Gemini API hatası (${res.status}): ${errText.slice(0, 240)}`);
  }

  const data = await res.json();
  const text = (data?.candidates?.[0]?.content?.parts || []).map((part) => part?.text || "").join("");
  return extractJsonBlock(text);
}

export default async function handler(req, res) {
  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  if (req.method === "GET") {
    const resolved = resolveServerProvider("openrouter", "");
    return res.status(200).json({
      service: "ECG_Helper_Serverless",
      server_key_configured: Boolean(resolved),
      provider: resolved ? resolved.provider : null,
      model: resolved ? resolved.model : null,
    });
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Yalnızca GET ve POST desteklenir." });
  }

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch {
      return res.status(400).json({ error: "Geçersiz JSON gövdesi." });
    }
  }
  body = body || {};

  const { prompt, image_uris = [], image_labels = [], provider = "openrouter", model = "" } = body;
  if (!prompt || typeof prompt !== "string") {
    return res.status(400).json({ error: "Eksik 'prompt' alanı." });
  }
  if (prompt.length > MAX_PROMPT_CHARS) {
    return res.status(413).json({ error: "'prompt' alanı çok uzun." });
  }

  const resolved = resolveServerProvider(provider, typeof model === "string" ? model.trim() : "");
  if (!resolved) {
    return res.status(200).json({ mode: "no_server_key" });
  }

  const images = (Array.isArray(image_uris) ? image_uris : [])
    .map((uri, idx) => ({
      uri,
      label: Array.isArray(image_labels) && typeof image_labels[idx] === "string" ? image_labels[idx] : "",
    }))
    .filter((img) => typeof img.uri === "string" && img.uri.startsWith("data:image/"))
    .slice(0, MAX_IMAGES);
  if (images.length === 0) {
    return res.status(400).json({ error: "Analiz için en az bir EKG görseli ('image_uris') gereklidir." });
  }

  const referer =
    req.headers?.origin ||
    (req.headers?.host ? `https://${req.headers.host}` : "https://ecg-helper.vercel.app");

  try {
    let parsed;
    let label;

    if (resolved.provider === "gemini") {
      parsed = await callGemini({
        apiKey: resolved.apiKey,
        model: resolved.model,
        prompt,
        images,
      });
      label = `Gemini (${resolved.model})`;
    } else {
      const isOpenRouter = resolved.provider === "openrouter";
      parsed = await callOpenAiCompatible({
        apiKey: resolved.apiKey,
        baseUrl: resolved.baseUrl,
        model: resolved.model,
        prompt,
        images,
        isOpenRouter,
        referer,
      });
      label = `${isOpenRouter ? "OpenRouter" : "OpenAI"} (${resolved.model})`;
    }

    return res.status(200).json({
      ...parsed,
      mode: "live_llm",
      model_used: `${label} — sunucu anahtarı`,
      disclaimer: CLINICAL_DISCLAIMER,
    });
  } catch (err) {
    const timedOut = err?.name === "TimeoutError" || err?.name === "AbortError";
    return res.status(502).json({
      mode: "server_error",
      error: timedOut
        ? "Model sağlayıcısı zamanında yanıt vermedi (zaman aşımı)."
        : err?.message || "Sunucu tarafı model çağrısı başarısız oldu.",
    });
  }
}
