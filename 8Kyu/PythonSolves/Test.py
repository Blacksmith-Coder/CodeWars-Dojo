import unittest

from HighestAndLowest import high_and_low
from SimpleStringReverseAll2 import solve


class TestSimples(unittest.TestCase):
    def test_high_and_low(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214", "[ERROR Test]")

    def test_solve(self):
        self.assertEqual(solve("codewars", 1, 5), "cawedors", "ERRORS")


if __name__ == '__main__':
    unittest.main()

