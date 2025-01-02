import unittest
from main import add, subtract, multiply, divide, div_mod

class testmath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertNotEqual(add(3, 7), 9)
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertNotEqual(subtract(2, 1), 2)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertNotEqual(multiply(3, 5), 16)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertNotEqual(divide(9, 3), 2)

    def test_mod(self):
        self.assertEqual(div_mod(10, 5), 0)
        self.assertNotEqual(div_mod(9, 3), 2)


if __name__ == '__main__':
    unittest.main()
