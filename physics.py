import numpy as np
import matplotlib.pyplot as plt

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
    if v < 0:
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
    if mass <= 0:
        raise ValueError("Invalid mass input")
    weight = mass * g
    force_g = buoyancy - weight
    if buoyancy > force_g:
        return True
    if buoyancy < force_g:
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
        raise ValueError("Invalid values!")
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
        raise ValueError("Invalid values!")
    if  r <= 0:
        raise ValueError("Invalid values!")
    F_direction_rad = (F_direction * np.pi) / 180
    torque = F_magnitude * np.sin(F_direction_rad) * r
    return torque #Nm

def calculate_moment_of_inertia(mass, r):

    '''
    Problem 7: Calculate moment of inertia

    Inertia = sum of mass * r**2
    moment of inertia = mass * r**2

    mass is in kg, r is in m
    '''

    if mass <= 0:
        raise ValueError("Invalid values!")
    if  r <= 0:
        raise ValueError("Invalid values!")
    moment_of_inertia = mass * np.power(r, 2)
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
    if F_magnitude <= 0 or mass<= 0 or volume <= 0 or thruster_distance <= 0:
        raise ValueError("Invalid values!")
    
    Fy = F_magnitude * np.sin(F_angle)
    Fx = F_magnitude * np.cos(F_angle)
    Ay = calculate_acceleration(Fy, mass)
    Ax = calculate_acceleration(Fx, mass)
    auv_acceleration = np.array([Ax, Ay])
    return auv_acceleration

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia=1, 
                                       thruster_distance=0.5):
    
    '''
    Problem 8.2: Calculate the angular acceleration of the auv

    In order to find the angular acceleration we first have to convert the units of F_angle
    from radians to degrees by multiplying by 180/pi. Then using this we can solve for
    torque by calling the calculate_torque function from above. Now that we have calculated
    torque we can plug this into the calculate_angular_acceleration function to find the
    angular acceleration of our auv

    auv_angular_acceleration is returned in rad/s**2
    '''

    if F_magnitude <= 0 or inertia <= 0 or thruster_distance <= 0:
        raise ValueError("Invalid values!")
    tau = calculate_torque(F_magnitude, F_angle, thruster_distance)
    perpendicular_force = F_magnitude*np.sin(F_angle)
    auv_angular_acceleration = calculate_angular_acceleration(perpendicular_force*thruster_distance, inertia)
    return auv_angular_acceleration

def calculate_auv2_acceleration(T, alpha, theta, mass=100):

    '''
    Problem 9.1: Calculate AUV2 acceleration

    In order to calculate the acceleration of the auv, we use the T array, an array of
    magnitudes of the forces applied, and multiply this by x which allows for the total
    force in the x' and y' direction to be found. Then using theta, this is flipped to a 
    global perspective in order to find the acceleration of the AUV in the x and y 
    direction. These are returned as an array [acc in x, acc in y]

    F_magnitude is in N, F_angle is in radians, mass is in kg
    '''
    if type(T) != np.ndarray:
        raise TypeError("T has to be an ndarray!")
    if mass <= 0:
        raise ValueError("Invalid values!")
    components = np.array([[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)]])
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]])
    net_force_prime = np.matmul(components, T)
    net_force = np.matmul(rotation_matrix, net_force_prime)
    Ax = net_force[0]/mass
    Ay = net_force[1]/mass
    auv2_acceleration = np.array([Ax, Ay])
    return auv2_acceleration

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):

    '''
    Problem 9.2: Calculate angular acceleration for auv2

    In order to solve for angular acceleration we need to use T, an array of
    the magnitudes of the forces applied on the auv, and multiply this by x in order
    to find the effects the force has in the x and y directions (this is given by F)
    To solve for total force being applied we add the force in the x direction
    and the y direction for Fnet. We can then use this net force to plug into our
    calculate_torque function and then use the returned value to input into the
    calculate_angular_acceleration function along with r. r was found by using the 
    pythagorean theorem to find r, the hypotenuse, of a triangle where L and l are
    the two legs lengths.

    auv2_angular_acceleration is returned in rad/s**2
    '''

    if type(T) != np.ndarray:
        raise TypeError("T has to be an ndarray!")
    if  L <= 0 or l <= 0 or inertia <= 0:
        raise ValueError("Invalid values!")
    components = np.array([L*np.sin(alpha)+l*np.cos(alpha), 
                  -L*np.sin(alpha)-l*np.cos(alpha),
                  L*np.sin(alpha)+l*np.cos(alpha),
                  -L*np.sin(alpha)-l*np.cos(alpha)])
    net_torque = np.matmul(components, T)
    auv2_angular_acceleration = calculate_angular_acceleration(net_torque, inertia)
    return auv2_angular_acceleration

def simulate_auv2_motion(T, alpha, L, l, inertia=100, mass=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0):
    time = np.arange(0, t_final, dt)
    x = np.zeros_like(time)
    x[0] = x0
    y = np.zeros_like(time)
    y[0] = y0
    theta = np.zeros_like(time)
    theta[0] = theta0
    v = np.zeros(shape =(len(time), 2))
    omega = np.zeros_like(time)
    linear_acceleration = np.zeros(shape =(len(time), 2))
    angular_acceleration = np.zeros_like(time)
    for i in range (1, len(time)):
        angular_acceleration[i] = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)
        omega[i] = omega[i-1] + angular_acceleration[i]*dt
        theta[i] = np.mod(theta[i-1] + omega[i-1]*dt, (2*np.pi))
        linear_acceleration[i][0] = calculate_auv2_acceleration(T, alpha, theta[i], mass)[0]
        linear_acceleration[i][1] = calculate_auv2_acceleration(T, alpha, theta[i], mass)[1]
        v[i][0] = v[i-1][0] + linear_acceleration[i][0]*dt
        v[i][1] = v[i-1][1] + linear_acceleration[i][1]*dt
        x[i] = x[i-1] + v[i][0]*dt
        y[i] = y[i-1] + v[i][1]*dt

    ret = (time, x, y, theta, v, omega, linear_acceleration)
    return ret

def plot_auv2_motion(time, x, y, theta, v, omega, linear_acceleration):
    plt.plot(time, x, label="X: Position")
    plt.plot(time, y, label="Y: Position")
    vx = np.zeros_like(time)
    vy = np.zeros_like(time)
    ax = np.zeros_like(time)
    ay = np.zeros_like(time)
    for i in range (0, len(v)):
        vx[i] = v[i][0]
        vy[i] = v[i][1]
        ax[i] = linear_acceleration[i][0]
        ay[i] = linear_acceleration[i][1]
    plt.plot(time, vx, label="X: Velocity")
    plt.plot(time, vy, label="Y: Velocity")
    plt.plot(time, ax, label="X: Acceleration")
    plt.plot(time, ay, label="Y: Acceleration")
    plt.plot(time, omega, label="Angular Velocity")
    plt.plot(time, theta, label="Angular Displacement")
    plt.xlabel("Time (s)")
    plt.ylabel("Variables")
    plt.legend()
    plt.show()