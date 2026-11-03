# -*- coding: utf-8 -*-
"""
Yeşil Alan Simülasyon Vakaları (70 Vaka)
Her vaka 4 aşamalıdır ve her yanlış seçeneğin dinamik senaryo güncellemesi (scenario_update)
ve öğretici geri bildirimi (teaching_point) mevcuttur.
"""

from cases_green_part1 import GREEN_CASES_PART1
from cases_green_part2 import GREEN_CASES_PART2
from cases_green_part3 import GREEN_CASES_PART3
from cases_green_part4 import GREEN_CASES_PART4
from cases_green_part5 import GREEN_CASES_PART5
from cases_green_part6 import GREEN_CASES_PART6
from cases_green_part7 import GREEN_CASES_PART7

GREEN_CASES = (
    GREEN_CASES_PART1
    + GREEN_CASES_PART2
    + GREEN_CASES_PART3
    + GREEN_CASES_PART4
    + GREEN_CASES_PART5
    + GREEN_CASES_PART6
    + GREEN_CASES_PART7
)
