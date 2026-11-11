// Mesai paylaştırma mantığı (arayüzden bağımsız, test edilebilir).

export const SHIFTS = {
  sabah: { key: 'sabah', label: 'Sabah Şifti', start: 8 * 60, end: 16 * 60 + 30 },
  aksam: { key: 'aksam', label: 'Akşam Şifti', start: 16 * 60 + 30, end: 24 * 60 + 90 },
}

// 0 -> A, 25 -> Z, 26 -> AA ...
export function letter(index) {
  let s = ''
  let n = index + 1
  while (n > 0) {
    const r = (n - 1) % 26
    s = String.fromCharCode(65 + r) + s
    n = Math.floor((n - 1) / 26)
  }
  return s
}

// Dakika -> "HH:MM" (gece yarısını geçen saatler 00:xx, 01:xx olarak gösterilir)
export function clock(minutes) {
  const m = ((minutes % 1440) + 1440) % 1440
  const h = Math.floor(m / 60)
  const mm = m % 60
  return `${String(h).padStart(2, '0')}:${String(mm).padStart(2, '0')}`
}

// Dakika -> "2 saat 7 dakika"
export function duration(minutes) {
  const h = Math.floor(minutes / 60)
  const m = minutes % 60
  if (h === 0) return `${m} dakika`
  if (m === 0) return `${h} saat`
  return `${h} saat ${m} dakika`
}

/**
 * Bir şift için plan üretir.
 * @param {object} shift   SHIFTS içinden bir şift
 * @param {number} count   Şiftteki kişi sayısı
 * @param {number} parts   Kişi başına alan başına blok sayısı (1 = tek blok, 2 = ikiye böl ...)
 * @param {number} firstIndex  İlk kişinin harf sırası (sabah 0 -> A; akşam sabahın devamı)
 * @param {number} yellowCount Sarı alanda aynı anda bulunacak kişi sayısı (1 veya 2)
 *
 * Kurallar:
 *  - Her an yeşilde 1, sarıda 1 (seçilirse 2) kişi vardır; aynı kişi iki alanda birden olamaz.
 *  - Şift, kişi sayısı x parça kadar eşit dilime bölünür.
 *  - Çift kişi sayısında kişiler ikili eşleşir: A yeşil/B sarı, ardından B yeşil/A sarı.
 *  - Tek kişi sayısında döngü kullanılır: A/B, B/C, C/A ...
 *  - Sarıda 2 kişi seçiliyse döngü: A yeşil/B+C sarı, B yeşil/C+D sarı ...
 *    Herkes 1 yeşil + 2 sarı dilim alır; bu yüzden en az 3 kişi gerekir.
 *  - Herkes eşit sayıda yeşil ve eşit sayıda sarı dilim alır, dolayısıyla süreler eşittir.
 */
export function buildShiftPlan(shift, count, parts, firstIndex = 0, yellowCount = 1) {
  const people = Array.from({ length: count }, (_, i) => letter(firstIndex + i))
  const needed = 1 + yellowCount
  if (count < needed) {
    let error = null
    if (count > 0) {
      error = yellowCount === 2
        ? `Yeşilde 1, sarıda 2 kişi için en az 3 kişi gerekir. Bu şiftte ${count} kişi var.`
        : 'Tek kişiyle yeşil ve sarı alan aynı anda doldurulamaz. En az 2 kişi gerekir.'
    }
    return { shift, people, slots: [], summary: [], error }
  }

  const total = shift.end - shift.start
  const slotCount = count * parts
  const bound = (i) => shift.start + Math.round((i * total) / slotCount)

  const partner = (p) => {
    if (count % 2 === 0) return p % 2 === 0 ? p + 1 : p - 1
    return (p + 1) % count
  }

  const slots = []
  for (let i = 0; i < slotCount; i++) {
    const g = i % count
    const start = bound(i)
    const end = bound(i + 1)
    const yellow = yellowCount === 2
      ? [people[(g + 1) % count], people[(g + 2) % count]]
      : [people[partner(g)]]
    slots.push({ start, end, minutes: end - start, green: people[g], yellow })
  }

  const summary = people.map((name) => {
    const green = slots.filter((s) => s.green === name)
    const yellow = slots.filter((s) => s.yellow.includes(name))
    const sum = (arr) => arr.reduce((t, s) => t + s.minutes, 0)
    return { name, green, yellow, greenMin: sum(green), yellowMin: sum(yellow), totalMin: sum(green) + sum(yellow) }
  })

  return { shift, people, slots, summary, error: null }
}
