import unittest
import PythonSolve


class SpanishConjugatorTest(unittest.TestCase):

    def test_conjugate(self):
        self.assertEqual(PythonSolve.conjugate("caminar"), {"caminar": ["camino", "caminas", "camina", "caminamos", "caminais", "caminan"]})
        print(PythonSolve.conjugate("caminar"))
        self.assertEqual(PythonSolve.conjugate("comer"), {"comer": ["como", "comes", "come", "comemos", "comeis", "comen"]})
        print(PythonSolve.conjugate("comer"))
        self.assertEqual(PythonSolve.conjugate("vivir"), {"vivir": ["vivo", "vives", "vive", "vivimos", "vivis", "viven"]})
        print(PythonSolve.conjugate("vivir"))


if __name__ == '__main__':
    unittest.main()