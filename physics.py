g = 9.81  # m/s**2
buoyancy = 0  # N
force_g = 0  # N
weight = 0  # kg*m/s**2
density_water = 1000  # kg/m**2
pressure = 0  # Pa
pressure_at_surface = 101.325  # Pa


def calculate_buoyancy(v, density_fluid):
    """
    Problem 1: Calculate the buoyancy of an object in a fluid

    force of buoyancy = density of fluid * volume of water displaced/object * gravity
    force of buoyancy is calculated in N, density is kg/m**2, volume is m**3, gravity is 9.81 m/s**2

    volume and density must be positive values in order to not raise an error
    """

    if density_fluid < 0:
        raise ValueError("density cannot be negative")
    elif v < 0:
        raise ValueError("volume cannot be negative")
    buoyancy = density_fluid * v * g
    return buoyancy  # in N (newtons)


def will_it_float(v, mass):
    """
    Problem 2: Determine whether the object will float or sink

    In order to know if the object will float or sink, we need to know if there is
    neutral, positive, or negative buoyancy
    negative buoyancy is when the force of gravity is greater than the force of buoyancy
    positive buoyancy is when the force of buoyancy is greater than the force of gravity
    neutral buoyancy is when the force of buoyancy and gravity are equivalent

    volume and mass must be positive in order to not raise an error

    force of gravity = buoyancy - (mass * gravity)
    force of gravity is given in N, weight is in kgm/s**2
    """

    if v < 0:
        raise ValueError("volume cannot be negative")
    elif mass < 0:
        raise ValueError("mass cannot be negative")
    weight = mass * g
    force_g = buoyancy - weight
    if buoyancy > force_g:
        return True
    elif buoyancy < force_g:
        return False
    else:
        return None


def calculate_pressure(depth):
    """
    Problem 3: Calculate the pressure on the object in water

    pressure = density_water * gravity * depth + the pressure at the surface
    adding the pressure at the surface is essential because it contributes to the pressure acting on the object
    depth can be input in a negative or positive fashion
    depth is in m, pressure is in Pa, and density is in kg/m**2
    """

    depth = abs(depth)
    pressure = density_water * g * depth + pressure_at_surface
    return pressure  # in Pa (pascals)
