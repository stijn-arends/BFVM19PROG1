""" usage: python3 -m unittest test_calc.py without if __name__
    rule
"""


import unittest
import calc

#create some test cases for the functions we want to unittest
#in order to create the test cases we need to create a test class
#that inherits from unittest.testcase (gives us access to lot of nice stuff)

class TestCalc(unittest.TestCase):
    #by convention test_ If we do not name this test_ it will not run in the
    #unit test (show!)
    def test_add(self):
        self.assertEqual(calc.add(3,4), 7) #change this to demonstrate
        self.assertEqual(calc.add(-1,1),0) #extend
        self.assertEqual(calc.add(-1,-1),-2) #try to find egdy cases

    def test_substract(self):
        self.assertEqual(calc.substract(-3,4), -7)

    def test_multiply(self):
        self.assertEqual(calc.multiply(0,7),0)

    def test_divide(self):
        #self.assertIsNone(calc.divide(7,0)) #test first without
        self.assertEqual(calc.divide(5,2),2.5) #test floor division
        #this is also an option
        #self.assertRaises(ValueError, calc.divide, 10, 0)
        # or
        with self.assertRaises(ValueError):
            calc.divide(10,0)



#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()
