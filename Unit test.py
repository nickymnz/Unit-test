import unittest
import calculations


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = calculations.add(5, 6)
        self.assertEqual(11, result)


if __name__ == '__main__':
    unittest.main()