import math

def area_of_sound_hole(f: float, c: float, v: float, leff: float) -> float:
    """
    Calculate the Helmholtz resonance frequency.

    Args:
        f (float): Helmholz resonance frequency (Hz)
        c (float): Speed of sound in air (m/s).
        v (float): Volume of the air chamber (m³).
        leff (float): Effective neck length (m).

    Returns:
        float: Area of sound hole in square meters (m²).
    """
    if f <= 0:
        raise ValueError("Frequency must be greater than 0")
    if c <= 0:
        raise ValueError("Speed of Sound must be greater than 0")
    if v <= 0:
        raise ValueError("Volume must be greater than 0")
    if leff <= 0:
        raise ValueError("Effective Length must be greater than 0")
    return ((((2 * math.pi * f) / c) ** 2) * v * leff)

def helmholtz_formula(c: float, a: float, v: float, leff: float) -> float:
    """
    Claculate Helmholtz resonance frequency, the frequency of the tap-tuned note

    Args:
        c (float): speed of sound (m/s).
        a: area of the sound hole (m²).
        v: volume of the air chamber (m³).
        leff: effective neck length (m).

    Returns:
        float: Helmholtz resonance frequency in Hz.
    """
    if c <= 0:
        raise ValueError("Speed of Sound must be greater than 0")
    if a <= 0:
        raise ValueError("Area must be greater than 0")
    if v <= 0:
        raise ValueError("Volume must be greater than 0")
    if leff <= 0:
        raise ValueError("Effective Length must be greater than 0")
    return ((c / (2 * math.pi)) * (math.sqrt((a / (v * leff)))))
