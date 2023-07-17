import unittest
import physics


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
        self.assertEqual(physics.calculate_torque(10, 10, 10), -54.40211)
        self.assertEqual(physics.calculate_torque(90, 8, 9), 801.38018)

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
        self.assertEqual(physics.calculate_auv_acceleration(10, 2,), [-0.04161, 0.09093])
        self.assertEqual(physics.calculate_auv_acceleration(9, 8), [-0.0131, 0.08904])

        self.assertNotEqual(physics.calculate_auv_acceleration(9, 8), [20, 20])
        self.assertNotEqual(physics.calculate_auv_acceleration(234, 0.9), [7.6, 8])

        self.assertRaises(ValueError, physics.calculate_auv_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_acceleration, 0, 76)

    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv_angular_acceleration(9, 3), 3.52569)
        self.assertEqual(physics.calculate_auv_angular_acceleration(8, 7.95), 0.11793)

        self.assertNotEqual(physics.calculate_auv_angular_acceleration(9, 8), 8)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(7, 737), 6)

        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, -10, 0)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 0, 4)
        self.assertRaises(ValueError, physics.calculate_auv_angular_acceleration, 9, 7, -3)

    def test_calculate_auv2_acceleration(self):
        self.assertEqual(physics.calculate_auv2_acceleration([3, 3, 3, 3], 10, 10), [0.00000, 0.00000])
        self.assertEqual(physics.calculate_auv2_acceleration([5, 6, 2, 9], 98, 0.76), [-0.0237, -0.02494])

        self.assertNotEqual(physics.calculate_auv2_acceleration([0, 3, 4.5, 9], 9, 72), [23.5, -0.2222])
        self.assertNotEqual(physics.calculate_auv2_acceleration([3, 1, 5.6, 0.2], 8, 3), [7, 0.00043])

    def test_calculate_auv2_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv2_angular_acceleration([3, 3, 3, 3], 4, 7, 5), 0)
        self.assertEqual(physics.calculate_auv2_angular_acceleration([5, 6, 2, 9], 2, 4.3, 0.4), 5.45578)

        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([0, 3, 4.5, 9], 23, 1, 2), 9)
        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([3, 1, 5.6, 0.2], 23, 9.88, 0.0002), -0.002)

        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 3, 3, 3], 23, -1, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [5, 6, 2, 9], 23, 0, 1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [0, 3, 4.5, 9], 23, 1, -1)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, 0)
        self.assertRaises(ValueError, physics.calculate_auv2_angular_acceleration, [3, 1, 5.6, 0.2], 23, 1, 1, -1)




