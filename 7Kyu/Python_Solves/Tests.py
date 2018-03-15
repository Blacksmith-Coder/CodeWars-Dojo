import unittest
import SpanishSolve
import FunctionalAddition


class SpanishConjugatorTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
