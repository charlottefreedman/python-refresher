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
        np.testing.assert_array_equal(physics.calculate_auv_acceleration(10, 2,), np.array([-0.04161468365471424, 0.09092974268256818]))
        np.testing.assert_array_equal(physics.calculate_auv_acceleration(9, 8), np.array([-0.013095003042775217, 0.08904224219610436]))

        self.assertRaises(ValueError, physics.calculate_auv_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_acceleration, 0, 76)

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(9, 3), 0.235511803)
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(8, 7.95), 0.5532355)

        self.assertNotEqual(physics.calculate_auv_angular_acceleration(9, 8), 8)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(7, 737), 6)

        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 0, 4)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 9, 7, -3)

    def test_calculate_auv2_acceleration(self):
        np.testing.assert_array_equal(physics.calculate_auv2_acceleration([3, 3, 3, 3], 10, 10), np.array([-1.863113061776228e-18, 1.2079695263830675e-18]))
        np.testing.assert_array_equal(physics.calculate_auv2_acceleration([5, 6, 2, 9], 98, 0.76), np.array([-0.02370090407111011, -0.024936469723481437]))

    def test_calculate_auv2_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv2_angular_acceleration([3, 3, 3, 3], 4, 7, 5), 0)
        self.assertAlmostEqual(physics.calculate_auv2_angular_acceleration([5, 6, 2, 9], 2, 4.3, 0.4), 5.45578456)

        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([0, 3, 4.5, 9], 23, 1, 2), 9)
        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([3, 1, 5.6, 0.2], 23, 9.88, 0.0002), -0.002)

        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 3, 3, 3], 23, -1, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [5, 6, 2, 9], 23, 0, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [0, 3, 4.5, 9], 23, 1, -1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, -1)




