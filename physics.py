import numpy as np

g = 9.81  # m/s**2
buoyancy = 0  # N
force_g = 0  # N
weight = 0  # kg*m/s**2
density_water = 1000  # kg/m**2
pressure = 0  # Pa
pressure_at_surface = 101.325  # Pa
force = 0 #N
mass = 0 #kg
tau = 0 #Nm
I = 0 #kgm**2


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

    if v <= 0:
        raise ValueError("Invalid volume input")
    elif mass <= 0:
        raise ValueError("Invalid mass input")
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

def calculate_acceleration(force, mass):

    '''
    Problem 4: Calculate acceleration

    Acceleration = force / mass
    mass cannot be negative

    mass is in kg and force is in N
    '''
    if mass <= 0:
        raise ValueError("Invalid mass input")
    acceleration = force / mass
    return acceleration # in m/s**2

def calculate_angular_acceleration(tau, I):

    '''
    Problem 5: Calculate angular acceleration

    Solve for angular acceleration by rearranging the equation tau=I*angular accceleration to 
    angular acceleration = tau / I

    Inertia cannot be negative or equal to 0

    Tau is in Nm and I is in kg*(m**2)
    '''

    if I <= 0:
        raise ValueError("Invalid inertia input")
    angular_acceleration = tau/I
    return angular_acceleration #N/kgm

def calculate_torque(F_magnitude, F_direction, r):

    '''
    Problem 6: Calculate Torque

    Torque = F * r
    To find the force perpendicular to r, solve using trig functions
    Fperp = magnitude * sin(degree)

    F_magnitude and r cannot be negative

    F_magnitude is in N, F_direction is in degrees, r is in m
    '''

    if F_magnitude <= 0:
        raise ValueError("Invalid magnitude input")
    elif  r <= 0:
        raise ValueError("Invalid r input")
    x = F_magnitude * np.sin(F_direction)
    torque = x * r
    return torque #Nm

def calculate_moment_of_inertia(mass, r):

    '''
    Problem 7: Calculate moment of inertia

    Inertia = sum of mass * r**2
    moment of inertia = mass * r**2

    mass is in kg, r is in m
    '''

    if mass <= 0:
        raise ValueError("Invalid mass input")
    elif  r <= 0:
        raise ValueError("Invalid r input")
    moment_of_inertia = mass * r * r
    return moment_of_inertia #kg(m**2)

def calculate_auv_acceleration(F_magnitude, F_angle, mass=100,
                                volume=0.1, thruster_distance=0.5):
    
    '''
    Problem 8.1: Calculate AUV acceleration

    In order to calculate the acceleration of the auv, we needed to calculate the force
    of the vector in the x and y directions using trig functions. These forces are then
    plugged into the calculate_acceleration function in order to find the acceleration
    of the AUV in the x and y direction. These are returned as an array [acc in x, acc in y]

    F_magnitude is in N, F_angle is in radians, mass is in kg
    '''

    Fy = F_magnitude * np.sin(F_angle)
    Fx = F_magnitude * np.cos(F_angle)
    Ay = calculate_acceleration(Fy, mass)
    Ax = calculate_acceleration(Fx, mass)
    auv_acceleration = [Ax, Ay]
    return auv_acceleration

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia=1, 
                                       thruster_distance=0.5):
    
    '''
    
    '''

    F_angle = (F_angle*180)/np.pi
    tau = calculate_torque(F_magnitude, F_angle, thruster_distance)
    auv_angular_acceleration = calculate_angular_acceleration(tau, inertia)
    return auv_angular_acceleration

def calculate_auv2_acceleration(T, alpha, mass=100):
    T = [[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
         [np.sin(alpha)], -np.sin(alpha), -np.sin(alpha), np.sin(alpha)]
    
    
