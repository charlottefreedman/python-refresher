import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "hi")

    def test_sub(self):
        self.assertEqual(hello.sub(4, 5), -1)
        self.assertNotEqual(hello.sub(9, 7), 3)
        self.assertEqual(hello.sub(5, 5), 0)
    
    def test_add(self):
        self.assertEqual(hello.add(4, 6), 10)
        self.assertNotEqual(hello.add(3, 0), 4)
        self.assertEqual(hello.add(-1, 9), 8)
    
    def test_power(self):
        self.assertEqual(hello.power(4, 1), 4)
        self.assertNotEqual(hello.power(5, 0), 2)
        self.assertEqual(hello.power(2, 2), 4)
    
    def test_log(self):
        self.assertEqual(hello.log(7), 1.9459101490553132)
        self.assertNotEqual(hello.log(1), 1)
        self.assertEqual(hello.log(100), 4.605170185988092)

    def test_exp(self):
        self.assertEqual(hello.exp(2), 7.38905609893065)
        self.assertNotEqual(hello.exp(1), 2)
        self.assertEqual(hello.exp(0), 1)

    def test_div(self):
        self.assertEqual(hello.div(92, 23), 4)
        self.assertNotEqual(hello.div(83, 1), 84)
        self.assertEqual(hello.div(0, 739), 0)

    def test_mul(self):
        self.assertEqual(hello.mul(7, 2), 14)
        self.assertNotEqual(hello.mul(0, 49), 1)
        self.assertEqual(hello.mul(1, 638), 638)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertNotEqual(hello.sqrt(9), 4)
        self.assertEqual(hello.sqrt(16), 4)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertNotEqual(hello.sin(1), 1)
        self.assertEqual(hello.sin(2), 0.9092974268256817)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertNotEqual(hello.cos(1), 1)
        self.assertEqual(hello.cos(2), -0.4161468365471424)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertNotEqual(hello.tan(1), 1)
        self.assertEqual(hello.tan(2), -2.185039863261519)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertNotEqual(hello.cot(1), 0)
        self.assertEqual(hello.cot(2), -0.45765755436028577)


if __name__ == "__main__":
    unittest.main()
