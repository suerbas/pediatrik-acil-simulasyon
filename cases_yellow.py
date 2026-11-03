# -*- coding: utf-8 -*-
"""
Sarı Alan Simülasyon Vakaları (70 Vaka)
Her vaka 4 aşamalıdır ve her yanlış seçeneğin dinamik senaryo güncellemesi (scenario_update)
ve öğretici geri bildirimi (teaching_point) mevcuttur.
"""

from cases_yellow_part1 import YELLOW_CASES_PART1
from cases_yellow_part2 import YELLOW_CASES_PART2
from cases_yellow_part3 import YELLOW_CASES_PART3
from cases_yellow_part4 import YELLOW_CASES_PART4
from cases_yellow_part5 import YELLOW_CASES_PART5
from cases_yellow_part6 import YELLOW_CASES_PART6
from cases_yellow_part7 import YELLOW_CASES_PART7

YELLOW_CASES = (
    YELLOW_CASES_PART1
    + YELLOW_CASES_PART2
    + YELLOW_CASES_PART3
    + YELLOW_CASES_PART4
    + YELLOW_CASES_PART5
    + YELLOW_CASES_PART6
    + YELLOW_CASES_PART7
)
