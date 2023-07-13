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
        self.assertEqual(physics.calculate_pressure(10), 98100.0)
        self.assertNotEqual(physics.calculate_pressure(10), 10)
