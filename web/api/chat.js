// Vaka asistanı: önce ERNIE (OpenRouter), sonra Gemini/Gemma, en son diğer OpenRouter modelleri.
// API anahtarları yalnızca sunucuda durur (Vercel ortam değişkenleri):
//   GEMINI_API_KEY      (zorunlu)   — https://aistudio.google.com/apikey
//   GEMINI_MODEL        (isteğe bağlı, varsayılan: gemini-flash-latest)
//   OPENROUTER_API_KEY  (isteğe bağlı yedek)
//   PRIMARY_MODEL       (isteğe bağlı, ilk denenen OpenRouter modeli; varsayılan: baidu/ernie-5.5-flash-preview:free)
import { readFile } from 'node:fs/promises'
import path from 'node:path'

const MAX_MESSAGES = 12
const MAX_CHARS = 800
const TRUNCATED = '\n\n(Yanıt uzunluk sınırında kesildi; daha dar bir soru sorabilirsin.)'
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
        '- Yalnızca kullanıcı açıkça "doğru şık hangisi / cevap ne / tanı ne" diye sorarsa kibarca reddet ve "Klinik ipucu al" butonunu hatırlat.',
        '- İlaç, doz, tetkik, kılavuz, fizyopatoloji gibi genel tıbbi sorular SERBESTTİR: doğrudan ve tam yanıtla. Bu tür sorularda reddetme cümlesi, ipucu butonu hatırlatması ya da "şu aşamada yapılması gerekenler" listesi EKLEME.',
      ].join('\n')
  return [
    'Sen Türkiye’deki pediatrik acil serviste çalışan hekimlere eğitim veren deneyimli bir çocuk acil uzmanısın.',
    'Aşağıdaki simülasyon vakası hakkında hekimin sorularını Türkçe, kısa ve net yanıtla.',
    'UZUNLUK: En fazla ~180 kelime. Liste gerekiyorsa en önemli 5-7 maddeyi ver, her madde tek satır; ders kitabı gibi her şeyi sayma. Önce en kritik bilgiyi yaz.',
    'Biçim: düz metin, gerekirse "- " ile madde ve **kalın**; başlık (#) ve tablo kullanma.',
    'Güncel kılavuzlara (AAP, ESPGHAN, NICE, GINA, ISPAD, Türk kılavuzları vb.) dayan; emin olmadığın bilgiyi uydurma, belirsizliği açıkça söyle.',
    'Doz verirken mg/kg ve maksimum dozu belirt; ilaç dozlarının kılavuzdan teyit edilmesi gerektiğini hatırlat.',
    'Tıbbi her soru vakayla ilgili kabul edilir. Yalnızca tıpla hiç ilgisi olmayan sorularda (spor, siyaset vb.) kısa bir cümleyle vakaya dönülmesini öner.',
    'Üslup: meslektaşa "sen" diye hitap et, tutarlı ol; "Kıymetli meslektaşım" gibi hitap ve süslü giriş cümleleri kullanma. Soruyu doğrudan yanıtlayarak başla; sorulmayan konuları ekleme.',
    rules,
    '',
    '--- VAKA BİLGİSİ (hekimin şu ana kadar gördükleri) ---',
    ctx.text,
  ].join('\n')
}

// Gemma, sistem talimatı alanını desteklemez: talimat ilk kullanıcı mesajının başına eklenir.
function geminiBody(model, system, messages, generationConfig) {
  const contents = messages.map((m) => ({ role: m.role === 'user' ? 'user' : 'model', parts: [{ text: m.text }] }))
  if (!model.startsWith('gemma')) return { systemInstruction: { parts: [{ text: system }] }, contents, generationConfig }
  const first = [system, '', '--- SORU ---', contents[0].parts[0].text].join('\n')
  contents[0] = { role: 'user', parts: [{ text: first }] }
  return { contents, generationConfig }
}

async function askGemini(system, messages) {
  const key = process.env.GEMINI_API_KEY
  if (!key) throw Object.assign(new Error('no-key'), { code: 'no-key' })
  // Sırayla denenecek modeller; ilki yoğunsa, yavaşsa ya da kotası dolduysa sonrakine geçilir.
  // (2.0 Flash kaldırıldı; 2.5 Flash yeni kullanıcılara kapalı. İlk model yoğunsa kısa beklemeyle bir kez daha denenir.)
  // Gemma modelleri de aynı anahtarla çalışır ve ücretsiz günlük kotaları Gemini'den çok daha yüksektir.
  const models = [
    process.env.GEMINI_MODEL,
    'gemini-3.8-flash',
    'gemini-flash-latest',
    'gemini-flash-lite-latest',
    'gemma-4-31b-it',
    'gemma-3-27b-it',
  ].filter(
    (m, i, a) => m && a.indexOf(m) === i,
  )
  const attempts = [...models]
  let retried = false
  const deadline = Date.now() + 30_000
  const errors = []
  let lastError
  for (let i = 0; i < attempts.length; i++) {
    const model = attempts[i]
    const left = deadline - Date.now()
    if (left < 4000) break
    const generationConfig = { temperature: 0.4, maxOutputTokens: 4096 }
    if (model.startsWith('gemini-3')) generationConfig.thinkingConfig = { thinkingLevel: 'low' }
    let r
    try {
      r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: 'POST',
        headers: { 'content-type': 'application/json', 'x-goog-api-key': key },
        signal: AbortSignal.timeout(Math.min(15_000, left)),
        body: JSON.stringify(geminiBody(model, system, messages, generationConfig)),
      })
    } catch (err) {
      lastError = Object.assign(new Error(`${model}: zaman aşımı/bağlantı hatası (${err.name})`), { status: 504 })
      console.error('[chat] Gemini hatası', lastError.message)
      errors.push(lastError.message)
      continue
    }
    const data = await r.json().catch(() => ({}))
    if (!r.ok) {
      lastError = Object.assign(new Error(`${model}: ${data?.error?.message || `HTTP ${r.status}`}`), { status: r.status })
      console.error('[chat] Gemini hatası', lastError.message)
      errors.push(lastError.message.slice(0, 120))
      // Geçersiz ayar (400), model yok (404), aşırı yük (500/503) ya da kota (429): sıradaki modeli dene.
      if (r.status === 503 && model === models[0] && !retried) {
        retried = true
        await new Promise((res) => setTimeout(res, 1500))
        attempts.splice(i + 1, 0, model)
      }
      if ([400, 404, 429, 500, 503].includes(r.status)) continue
      throw lastError
    }
    const cand = data?.candidates?.[0]
    let text = cand?.content?.parts?.filter((p) => !p.thought).map((p) => p.text || '').join('').trim()
    // Sınır yüzünden yarıda kesildiyse kullanıcıya belirt.
    if (text && cand?.finishReason === 'MAX_TOKENS') text += TRUNCATED
    if (!text) {
      const reason = data?.candidates?.[0]?.finishReason || data?.promptFeedback?.blockReason || 'bilinmiyor'
      throw new Error(`${model}: boş yanıt (${reason})`)
    }
    return { text, model: data?.modelVersion || model, skipped: errors }
  }
  if (lastError) lastError.message = errors.join(' | ')
  throw lastError || new Error('Gemini için süre doldu')
}

// Asistanın ilk tercihi (OpenRouter üzerinden). Yanıt veremezse Gemini zincirine geçilir.
const PRIMARY_MODEL = process.env.PRIMARY_MODEL || 'baidu/ernie-5.5-flash-preview:free'
// Gemini de başarısız olursa denenecek OpenRouter yedekleri.
const OPENROUTER_FALLBACKS = ['google/gemma-4-31b-it:free', 'nvidia/nemotron-3-ultra-550b-a55b:free']

async function askOpenRouter(system, messages, models, timeoutMs) {
  const key = process.env.OPENROUTER_API_KEY
  if (!key) throw new Error('no-openrouter-key')
  // models birden fazlaysa OpenRouter'ın yerleşik yedeklemesi sıradakini kendisi dener.
  const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    signal: AbortSignal.timeout(timeoutMs),
    headers: { 'content-type': 'application/json', authorization: `Bearer ${key}` },
    body: JSON.stringify({
      models,
      temperature: 0.4,
      max_tokens: 2500,
      messages: [
        { role: 'system', content: system },
        ...messages.map((m) => ({ role: m.role === 'user' ? 'user' : 'assistant', content: m.text })),
      ],
    }),
  })
  const data = await r.json().catch(() => ({}))
  if (!r.ok) throw new Error(data?.error?.message || `OpenRouter ${r.status}`)
  const choice = data?.choices?.[0]
  let text = choice?.message?.content?.trim()
  if (text && choice?.finish_reason === 'length') text += TRUNCATED
  if (!text) throw new Error('OpenRouter boş yanıt döndü')
  return { text, model: data?.model || models[0] }
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

  // 1) İlk tercih: ERNIE (OpenRouter)
  let e0
  try {
    const { text, model } = await askOpenRouter(system, history, [PRIMARY_MODEL], 12_000)
    return json(200, { reply: text, provider: 'openrouter', model })
  } catch (err) {
    e0 = err
  }
  // 2) Gemini / Gemma zinciri, 3) kalan OpenRouter yedekleri
  try {
    const { text, model, skipped } = await askGemini(system, history)
    // skipped: atlanan modellerin hata özetleri (arayüzde gösterilmez, sorun giderme için)
    return json(200, { reply: text, provider: 'gemini', model, skipped: [`${PRIMARY_MODEL}: ${e0.message}`.slice(0, 120), ...skipped] })
  } catch (e) {
    try {
      const { text, model } = await askOpenRouter(system, history, OPENROUTER_FALLBACKS, 14_000)
      return json(200, { reply: text, provider: 'openrouter', model })
    } catch (e2) {
      if (e.code === 'no-key' && e2.message === 'no-openrouter-key')
        return json(503, { error: 'Vaka asistanı henüz yapılandırılmadı (API anahtarı eksik).' })
      if (e.status === 429) return json(429, { error: 'Günlük ücretsiz kota doldu. Yarın tekrar deneyin.' })
      // Ayrıntı yalnızca sağlayıcıların hata metnidir (anahtar içermez); sorun gidermeyi kolaylaştırır.
      const detail = `ERNIE: ${e0.message} || Gemini: ${e.message} || OpenRouter: ${e2.message}`.slice(0, 700)
      return json(502, { error: 'Asistan şu an yanıt veremiyor. Biraz sonra tekrar deneyin.', detail })
    }
  }
}
