import unittest
import SpanishSolve
import FunctionalAddition
import ScrollingText


class MainTest(unittest.TestCase):

    def test_conjugate(self):
        self.assertEqual(SpanishSolve.conjugate("caminar"), {"caminar": ["camino", "caminas", "camina", "caminamos", "caminais", "caminan"]})
        print(SpanishSolve.conjugate("caminar"))
        self.assertEqual(SpanishSolve.conjugate("comer"), {"comer": ["como", "comes", "come", "comemos", "comeis", "comen"]})
        print(SpanishSolve.conjugate("comer"))
        self.assertEqual(SpanishSolve.conjugate("vivir"), {"vivir": ["vivo", "vives", "vive", "vivimos", "vivis", "viven"]})
        print(SpanishSolve.conjugate("vivir"))

    def test_functionalAdd(self):
        add_one = FunctionalAddition.add(1)
        self.assertEqual(add_one(3), 4)
        add_three = FunctionalAddition.add(3)
        self.assertEqual(add_three(3), 6)

    def test_scrollingText(self):
        print(ScrollingText.scrolling_text("abc"))
        self.assertEqual(ScrollingText.scrolling_text("abc"), ["ABC", "BCA", "CAB"])
        print(ScrollingText.scrolling_text("codewars"))
        self.assertEqual(ScrollingText.scrolling_text("codewars"), ["CODEWARS", "ODEWARSC", "DEWARSCO", "EWARSCOD",
                                                                    "WARSCODE", "ARSCODEW" "RSCODEWA", "SCODEWAR"])


if __name__ == '__main__':
    unittest.main()
