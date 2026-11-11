// Vaka asistanı: Gemini (yedek: OpenRouter) ile vaka bağlamında soru-cevap.
// API anahtarları yalnızca sunucuda durur (Vercel ortam değişkenleri):
//   GEMINI_API_KEY      (zorunlu)   — https://aistudio.google.com/apikey
//   GEMINI_MODEL        (isteğe bağlı, varsayılan: gemini-flash-latest)
//   OPENROUTER_API_KEY  (isteğe bağlı yedek)
//   OPENROUTER_MODEL    (isteğe bağlı, varsayılan: nvidia/nemotron-3-nano-30b-a3b:free)
import { readFile } from 'node:fs/promises'
import path from 'node:path'

const MAX_MESSAGES = 12
const MAX_CHARS = 800
const PER_MINUTE = 8
const PER_DAY = 60

// Basit, örnek başına (best-effort) IP sınırlaması: kotayı birkaç kişinin tüketmesini önler.
const hits = new Map()
function rateLimited(ip) {
  const now = Date.now()
  const list = (hits.get(ip) || []).filter((t) => now - t < 86_400_000)
  const lastMinute = list.filter((t) => now - t < 60_000).length
  if (lastMinute >= PER_MINUTE || list.length >= PER_DAY) {
    hits.set(ip, list)
    return true
  }
  list.push(now)
  hits.set(ip, list)
  if (hits.size > 5000) hits.clear()
  return false
}

const json = (status, body) =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json; charset=utf-8' } })

function plain(html = '') {
  return String(html)
    .replace(/<span class="med-tooltip">[\s\S]*?<\/span><\/span>/g, '')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim()
}

async function loadCase(id, origin) {
  try {
    const file = path.join(process.cwd(), 'public', 'cases', `${id}.json`)
    return JSON.parse(await readFile(file, 'utf8'))
  } catch {
    const r = await fetch(`${origin}/cases/${id}.json`)
    if (!r.ok) throw new Error('case not found')
    return r.json()
  }
}

// Yalnızca hekimin o ana kadar gördüğü bilgiyi bota ver; vaka bitmeden doğru şıklar ve kesin tanı gönderilmez.
export function buildContext(c, step) {
  const total = c.steps.length
  const finished = step >= total
  const lines = [
    `Vaka: ${c.id} (${c.zone === 'yellow' ? 'Sarı alan' : 'Yeşil alan'}) · ${c.age} ${c.gender} · ${c.category}`,
    `Başvuru şikâyeti: ${c.complaint}`,
    `Öykü: ${plain(c.history)}`,
    `Geliş vitalleri: ${c.vitals.map(plain).join(', ')}`,
  ]
  for (let i = 0; i < Math.min(step, total); i++) {
    const s = c.steps[i]
    const ok = s.options.find((o) => o.correct)
    lines.push(`Aşama ${i + 1} (${s.title}) tamamlandı. Verilen doğru karar: ${ok.text}. Açıklama: ${ok.explanation}`)
    if (ok.finding) lines.push(`  Yeni bulgu: ${plain(ok.finding)}`)
  }
  if (finished) {
    lines.push(`Kesin tanı: ${c.diagnosis}`, `Sonuç/yatış: ${c.disposition}`, `Klinik inci: ${c.pearl}`)
  } else {
    const s = c.steps[step]
    lines.push(
      `ŞU ANKİ AŞAMA ${step + 1}/${total} (${s.title}): ${plain(s.question)}`,
      'Seçenekler:',
      ...s.options.map((o, i) => `  ${String.fromCharCode(65 + i)}) ${o.text}`),
    )
  }
  return { text: lines.join('\n'), finished }
}

export function systemPrompt(ctx) {
  const rules = ctx.finished
    ? 'Vaka tamamlandı; tanıyı, doğru kararları ve alternatifleri serbestçe tartışabilirsin.'
    : [
        'Vaka henüz tamamlanmadı. KESİN KURALLAR:',
        '- Şu anki aşamada hangi seçeneğin doğru olduğunu söyleme, ima etme, şıkları eleme.',
        '- Kesin tanıyı söyleme. Ayırıcı tanıyı ve düşünme yolunu tartışabilirsin.',
        '- Kullanıcı cevabı isterse kibarca reddet; bunun yerine yol gösterici bir soru veya ilgili kılavuz ilkesini anlat. Panelde "Klinik ipucu al" butonu olduğunu hatırlat.',
      ].join('\n')
  return [
    'Sen Türkiye’deki pediatrik acil serviste çalışan hekimlere eğitim veren deneyimli bir çocuk acil uzmanısın.',
    'Aşağıdaki simülasyon vakası hakkında hekimin sorularını Türkçe, kısa ve net yanıtla (genelde 3-8 cümle ya da kısa madde listesi).',
    'Güncel kılavuzlara (AAP, ESPGHAN, NICE, GINA, ISPAD, Türk kılavuzları vb.) dayan; emin olmadığın bilgiyi uydurma, belirsizliği açıkça söyle.',
    'Doz verirken mg/kg ve maksimum dozu belirt; ilaç dozlarının kılavuzdan teyit edilmesi gerektiğini hatırlat.',
    'Vaka dışı konularda (tıp dışı sorular) kısa bir cümleyle vakaya dönülmesini öner.',
    rules,
    '',
    '--- VAKA BİLGİSİ (hekimin şu ana kadar gördükleri) ---',
    ctx.text,
  ].join('\n')
}

async function askGemini(system, messages) {
  const key = process.env.GEMINI_API_KEY
  if (!key) throw Object.assign(new Error('no-key'), { code: 'no-key' })
  // Model adı tanınmazsa (404) sıradaki modele geç.
  const models = [process.env.GEMINI_MODEL, 'gemini-flash-latest', 'gemini-2.5-flash', 'gemini-2.0-flash'].filter(
    (m, i, a) => m && a.indexOf(m) === i,
  )
  let lastError
  for (const model of models) {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
      method: 'POST',
      headers: { 'content-type': 'application/json', 'x-goog-api-key': key },
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: system }] },
        contents: messages.map((m) => ({ role: m.role === 'user' ? 'user' : 'model', parts: [{ text: m.text }] })),
        generationConfig: { temperature: 0.4, maxOutputTokens: 2048 },
      }),
    })
    const data = await r.json().catch(() => ({}))
    if (!r.ok) {
      lastError = Object.assign(new Error(`${model}: ${data?.error?.message || `HTTP ${r.status}`}`), { status: r.status })
      console.error('[chat] Gemini hatası', lastError.message)
      if (r.status === 404) continue
      throw lastError
    }
    const text = data?.candidates?.[0]?.content?.parts?.map((p) => p.text || '').join('').trim()
    if (!text) {
      const reason = data?.candidates?.[0]?.finishReason || data?.promptFeedback?.blockReason || 'bilinmiyor'
      throw new Error(`${model}: boş yanıt (${reason})`)
    }
    return text
  }
  throw lastError
}

async function askOpenRouter(system, messages) {
  const key = process.env.OPENROUTER_API_KEY
  if (!key) throw new Error('no-openrouter-key')
  const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: { 'content-type': 'application/json', authorization: `Bearer ${key}` },
    body: JSON.stringify({
      model: process.env.OPENROUTER_MODEL || 'nvidia/nemotron-3-nano-30b-a3b:free',
      temperature: 0.4,
      max_tokens: 1200,
      messages: [
        { role: 'system', content: system },
        ...messages.map((m) => ({ role: m.role === 'user' ? 'user' : 'assistant', content: m.text })),
      ],
    }),
  })
  const data = await r.json().catch(() => ({}))
  if (!r.ok) throw new Error(data?.error?.message || `OpenRouter ${r.status}`)
  const text = data?.choices?.[0]?.message?.content?.trim()
  if (!text) throw new Error('OpenRouter boş yanıt döndü')
  return text
}

export async function POST(request) {
  let body
  try {
    body = await request.json()
  } catch {
    return json(400, { error: 'Geçersiz istek.' })
  }

  const { caseId, step, messages } = body || {}
  if (!/^[YS]\d{1,3}$/.test(caseId || '')) return json(400, { error: 'Geçersiz vaka.' })
  if (!Array.isArray(messages) || messages.length === 0) return json(400, { error: 'Mesaj yok.' })

  const history = messages
    .slice(-MAX_MESSAGES)
    .filter((m) => m && typeof m.text === 'string' && m.text.trim())
    .map((m) => ({ role: m.role === 'user' ? 'user' : 'model', text: m.text.slice(0, MAX_CHARS) }))
  if (history.at(-1)?.role !== 'user') return json(400, { error: 'Son mesaj kullanıcıdan olmalı.' })
  while (history.length && history[0].role !== 'user') history.shift()

  const ip = (request.headers.get('x-forwarded-for') || '').split(',')[0].trim() || 'local'
  if (rateLimited(ip)) return json(429, { error: 'Çok fazla soru gönderildi. Lütfen biraz sonra tekrar deneyin.' })

  let c
  try {
    c = await loadCase(caseId, new URL(request.url).origin)
  } catch {
    return json(404, { error: 'Vaka bulunamadı.' })
  }
  const s = Math.max(0, Math.min(Number.isInteger(step) ? step : 0, c.steps.length))
  const system = systemPrompt(buildContext(c, s))

  try {
    return json(200, { reply: await askGemini(system, history), provider: 'gemini' })
  } catch (e) {
    try {
      return json(200, { reply: await askOpenRouter(system, history), provider: 'openrouter' })
    } catch {
      if (e.code === 'no-key') return json(503, { error: 'Vaka asistanı henüz yapılandırılmadı (GEMINI_API_KEY eksik).' })
      if (e.status === 429) return json(429, { error: 'Günlük ücretsiz kota doldu. Yarın tekrar deneyin.' })
      // Ayrıntı yalnızca sağlayıcının hata metnidir (anahtar içermez); sorun gidermeyi kolaylaştırır.
      return json(502, { error: 'Asistan şu an yanıt veremiyor. Biraz sonra tekrar deneyin.', detail: String(e.message).slice(0, 300) })
    }
  }
}
