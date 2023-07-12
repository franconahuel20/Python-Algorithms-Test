import unittest
from main import FindKaprekarNumber

class FindKaprekarNumberTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fk = FindKaprekarNumber()

    def test_case_1(self):
        inputNumber = '8963'
        expectedIterations = 1
        iterations = self.fk.main(inputNumber)
        self.assertEqual(iterations, expectedIterations)

    def test_case_2(self):
        inputNumber = '1000'
        expectedIterations = 5
        iterations = self.fk.main(inputNumber)
        self.assertEqual(iterations, expectedIterations)

    def test_case_3(self):
        inputNumber = '1729'
        expectedIterations = 7
        iterations = self.fk.main(inputNumber)
        self.assertEqual(iterations, expectedIterations)

if __name__ == "__main__":
    unittest.main()