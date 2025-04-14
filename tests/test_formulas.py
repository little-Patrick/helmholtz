import math
from helmholtz.formulas.formula import helmholtz_formula
from helmholtz.formulas.formula import area_of_sound_hole


def test_helmholtz_formula():
    f = helmholtz_formula(1, 1, 1, 1)
    expected = ((1 / (2 * math.pi)) * (math.sqrt((1 / (1 * 1)))))
    assert abs(f - expected) < 1e-10

def test_area_of_sound_hole():
    f = area_of_sound_hole(1, 1, 1, 1)
    expected = ((((2 * math.pi * 1) / 1) ** 2) * 1 * 1)
    assert abs(f - expected) < 1e-10
