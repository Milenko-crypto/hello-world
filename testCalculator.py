import unittest
from calculator import Calculator

class testSumFromNumbers(unittest.TestCase):
    def test_isCorrect(self):
        calc = Calculator()
        result = calc.SumfromNumbers(2,3)
        expected = 5
        self.assertEqual(result,expected)
    
    def test_isNegative(self):
        calc = Calculator()
        result = calc.SumfromNumbers(-4,1)
        expected = 0
        self.assertLess(result, expected)
    
    def test_isGreater(self):
        calc = Calculator()
        result = calc.SumfromNumbers(2,3)
        expected = 5
        self.assertGreaterEqual(result, expected)

def suite():

    test_suite = unittest.TestSuite() # instancira metodu TestSuite()
    test_suite.addTest(unittest.makeSuite(testSumFromNumbers))

    return test_suite

mySuite = suite()

runner = unittest.TextTestRunner() #unittest.TextTestRunner()metoda pokrece sve testove
runner.run(mySuite) # runner.run(mySuite) koji skup testova pokrecemo


