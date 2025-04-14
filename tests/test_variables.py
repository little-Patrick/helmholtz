from helmholtz.variables.variables import round_hole
from helmholtz.variables.variables import non_round_hole
from helmholtz.variables.variables import sound_hole_area
from helmholtz.variables.variables import speed_of_sound
import math

def test_sound_hole_area():
    speed = speed_of_sound(2)
    expected = (331 + (0.61 * 2))
    assert abs(speed - expected) < 1e-10

def test_sound_hole_area_for_radius_1():
    assert sound_hole_area(1) == math.pi

def test_sound_hole_area_precision():
    area = sound_hole_area(2)
    expected = math.pi * 4
    assert abs(area - expected) < 1e-10

def test_round_hole_effective_length():
    assert round_hole(1, 1) == 2.7

def test_non_round_hole():
    el = non_round_hole(1, 1, 1)
    expected = 1 + (1.7 * (1 / 1))
    assert abs(el - expected) < 1e-10
