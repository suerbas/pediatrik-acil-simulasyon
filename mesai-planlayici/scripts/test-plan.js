// Plan mantığı için basit doğrulama: node scripts/test-plan.js
import { SHIFTS, buildShiftPlan } from '../src/plan.js'

let failures = 0
const check = (cond, msg) => { if (!cond) { failures++; console.error('HATA:', msg) } }

for (const shift of Object.values(SHIFTS)) {
  const total = shift.end - shift.start
  for (let n = 2; n <= 20; n++) {
    for (let parts = 1; parts <= 3; parts++) {
      const tag = `${shift.key} n=${n} parts=${parts}`
      const plan = buildShiftPlan(shift, n, parts, 0)
      check(!plan.error, `${tag}: beklenmeyen hata`)
      check(plan.slots.length === n * parts, `${tag}: dilim sayısı`)
      check(plan.slots[0].start === shift.start && plan.slots.at(-1).end === shift.end, `${tag}: şift sınırları`)
      plan.slots.forEach((s, i) => {
        check(s.green !== s.yellow, `${tag}: dilim ${i} aynı kişi iki alanda`)
        if (i > 0) check(plan.slots[i - 1].end === s.start, `${tag}: dilim ${i} boşluk/çakışma`)
      })
      const totals = plan.summary.map((p) => p.totalMin)
      check(Math.max(...totals) - Math.min(...totals) <= 2 * parts, `${tag}: süreler eşit değil (${totals})`)
      check(plan.summary.every((p) => p.green.length === parts && p.yellow.length === parts), `${tag}: blok sayısı`)
      check(totals.reduce((a, b) => a + b, 0) === 2 * total, `${tag}: toplam süre`)
    }
  }
}

check(buildShiftPlan(SHIFTS.sabah, 1, 1).error, 'tek kişide uyarı verilmeli')

const p = buildShiftPlan(SHIFTS.sabah, 4, 1)
check(p.slots[0].green === 'A' && p.slots[0].yellow === 'B' && p.slots[1].green === 'B' && p.slots[1].yellow === 'A', 'A/B ikili eşleşme')

if (failures) { console.error(`${failures} hata`); process.exit(1) }
console.log('Tüm kontroller geçti.')
