from math import pi

# A
def sound_hole_area(r: float) -> float:
    """
    Calculate the area of a circlular sound hole.

    Args:
        r (float): Radius of the sound hole (m).
    
    Returns: 
        float: Area of the sound hole in square meters (m²).
    """
    if r <= 0:
        raise ValueError("Radius must be greater than 0")
    return (pi * (r ** 2))

# c
def speed_of_sound(temp=22) -> float:
    """
    Calculate the speed of sound in air.

    Args:
        temp (float): Tempurature (℃ )

    Returns: 
        float: Speed of sound in meters per second (m/s).
    """
    return (331 + (0.61 * temp))

# Leff
def round_hole(t: float, r: float) -> float:
    """
    Calculate the effective length of a round sound hole.

    Args:
        t (float): Thickness of the neck of the sound hole (m).
        r (float): Radius of the sound hole (m).

    Returns: 
        float: Effective Length of sound hole in meters (m).
    """
    if r <= 0:
        raise ValueError("Radius must be greater than 0")
    if t <= 0:
        raise ValueError("Thickness must be greater than 0")
    return t + (1.7 * r)

def non_round_hole(t: float, a: float, p: float) -> float:
    """
    Calculate the efective length of a non round sound hole.

    Args:
        t (float): Thickness of the neck of the sound hole (m).
        a (float): Area of the sound hole (m²).
        p (float): Perimeter of the sound hole (m).

    Returns: 
        float: Effective Length of sound hole in meters (m).
    """
    if p <= 0:
        raise ValueError("Perimeter must be greater than 0")
    if a <= 0:
        raise ValueError("Area must be greater than 0")
    if t <= 0:
        raise ValueError("Thickness must be greater than 0")
    return t + (1.7 * (a / p))
