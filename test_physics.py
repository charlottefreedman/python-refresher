import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertRaises(ValueError, physics.calculate_buoyancy, -10, -10)

        self.assertEqual(physics.calculate_buoyancy(10, 10), 981.0)
        self.assertNotEqual(physics.calculate_buoyancy(10, 10), 400)

    def test_will_it_float(self):
        self.assertRaises(ValueError, physics.will_it_float, -10, -10)

        self.assertEqual(physics.will_it_float(10, 10), True)
        self.assertNotEqual(physics.will_it_float(10, 10), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(10), 98201.325)
        self.assertNotEqual(physics.calculate_pressure(10), 10)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(100, 10), 10)
        self.assertEqual(physics.calculate_acceleration(90, 9), 10)
        self.assertEqual(physics.calculate_acceleration(88, 2), 44)

        self.assertNotEqual(physics.calculate_acceleration(10, 100), 9)
        self.assertNotEqual(physics.calculate_acceleration(10, 10), 10)
        self.assertNotEqual(physics.calculate_acceleration(25, 35), 100)

        self.assertRaises(ValueError, physics.calculate_acceleration, 10, -10)
        self.assertRaises(ValueError, physics.calculate_acceleration, 90, 0)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(10, 10), 1)
        self.assertEqual(physics.calculate_angular_acceleration(-90, 9), -10)
        
        self.assertNotEqual(physics.calculate_angular_acceleration(900, 9), 10)
        self.assertNotEqual(physics.calculate_angular_acceleration(8, 8), 8)

        self.assertRaises(ValueError, physics.calculate_angular_acceleration, -10, -10)
        self.assertRaises(ValueError, physics.calculate_angular_acceleration, 9, 0)

    def test_calculate_torque(self):
        self.assertAlmostEqual(physics.calculate_torque(10, 10, 10), 17.3648178)
        self.assertAlmostEqual(physics.calculate_torque(90, 8, 9), 112.73021178)

        self.assertNotEqual(physics.calculate_torque(18, 18, 18), 97)
        self.assertNotEqual(physics.calculate_torque(76, 2, 4), 3)

        self.assertRaises(ValueError, physics.calculate_torque, 0, 10, 10)
        self.assertRaises(ValueError, physics.calculate_torque, -10, 10, 10)
        self.assertRaises(ValueError, physics.calculate_torque, 10, -13, -10)
        self.assertRaises(ValueError, physics.calculate_torque, 10, -10, 0)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(1, 1), 1)
        self.assertEqual(physics.calculate_moment_of_inertia(5, 2), 20)

        self.assertNotEqual(physics.calculate_moment_of_inertia(1, 3), 6)
        self.assertNotEqual(physics.calculate_moment_of_inertia(8, 7), 50)

        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, 0, 1)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, -1, 1)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, 1, 0)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, 1, -1)

    def test_calculate_auv_acceleration(self):
        np.testing.assert_array_almost_equal(physics.calculate_auv_acceleration(10, 2,), np.array([-0.0416146, 0.0909297]))
        np.testing.assert_array_almost_equal(physics.calculate_auv_acceleration(9, 8), np.array([-0.0130950, 0.089042]))

        self.assertRaises(ValueError, physics.calculate_auv_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_acceleration, 0, 76)

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(9, 3), 0.6350400362694024)
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(8, 7.95), 3.9815751090304796)

        self.assertNotEqual(physics.calculate_auv_angular_acceleration(9, 8), 8)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(7, 737), 6)

        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 0, 4)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 9, 7, -3)

    def test_calculate_auv2_acceleration(self):
        np.testing.assert_array_almost_equal(physics.calculate_auv2_acceleration(np.array([4, 2, 3, 5]), 10, 10), np.array([-0.025919,  0.009129]))
        np.testing.assert_array_almost_equal(physics.calculate_auv2_acceleration(np.array([5, 6, 2, 9]), 98, 0.76), np.array([ 0.023701, -0.024936]))

    def test_calculate_auv2_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv2_angular_acceleration(np.array([3, 3, 3, 3]), 4, 7, 5), 0)
        self.assertAlmostEqual(physics.calculate_auv2_angular_acceleration(np.array([5, 6, 2, 9]), 2, 4.3, 0.4), -0.2994816160585259)

        self.assertNotEqual(physics.calculate_auv2_angular_acceleration(np.array([0, 3, 4.5, 9]), 23, 1, 2), 9)
        self.assertNotEqual(physics.calculate_auv2_angular_acceleration(np.array([3, 1, 5.6, 0.2]), 23, 9.88, 0.0002), -0.002)

        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([3, 3, 3, 3]), 23, -1, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([5, 6, 2, 9]), 23, 0, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([0, 3, 4.5, 9]), 23, 1, -1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([3, 1, 5.6, 0.2]), 23, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([3, 1, 5.6, 0.2]), 23, 1, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, np.array([3, 1, 5.6, 0.2]), 23, 1, 1, -1)
        self.assertRaises(TypeError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, -1)

    def test_simulate_auv2_motion(self):
        (time, x, y, theta, v, omega, linear_acceleration) = physics.simulate_auv2_motion(
            np.array([10, 0, 10, 0]), np.pi / 4, 1, 1, 100, 100, 0.1, 0.3, 0, 0, np.pi /4)
        np.testing.assert_array_almost_equal(time, np.array([0.0, 0.1, 0.2]))
        np.testing.assert_array_almost_equal(x, np.array([0, 0, 0]))
        np.testing.assert_array_almost_equal(y, np.array([0, 0, 0]))
        np.testing.assert_array_almost_equal(
            theta, np.array([np.pi/4, np.pi/4, np.pi/4]))
        np.testing.assert_array_almost_equal(v, np.array([[0, 0], [0, 0], [0, 0]]))
        np.testing.assert_array_almost_equal(omega, np.array([0, 0, 0.028284]))
        np.testing.assert_array_almost_equal(linear_acceleration, np.array([[0, 0], [0, 0], [0, 0]]))