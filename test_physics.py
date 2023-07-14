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
        self.assertEqual(physics.calculate_torque(10, 10, 10), -54.40211108893698)
