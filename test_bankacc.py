import unittest
import bankacc


class TestMyBankAccount(unittest.TestCase):
    def test_init(self):
        p1 = bankacc.MyBankAccount("John Doe", 100, 123456)

        self.assertEqual(p1.name, "John Doe")
        self.assertEqual(p1.accnum, 123456)
        self.assertEqual(p1._balance, 100)

        self.assertNotEqual(p1.name, "Jane Doe")
        self.assertNotEqual(p1.accnum, 654321)
        self.assertNotEqual(p1._balance, 10)

    def test_withdraw(self):
        p2 = bankacc.MyBankAccount("Jane Doe", 10, 654321)

        self.assertEqual(p2.withdraw(3), 7)
        self.assertNotEqual(p2.withdraw(5), 3)
        self.assertRaises(ValueError, p2.withdraw, 11)

    def test_deposit(self):
        p3 = bankacc.MyBankAccount("Charlotte", 200, 987654)

        self.assertEqual(p3.deposit(10), 210)
        self.assertNotEqual(p3.deposit(3), 20)
        self.assertRaises(ValueError, p3.deposit, -10)
