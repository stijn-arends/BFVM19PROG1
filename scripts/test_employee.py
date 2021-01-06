
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Fenna', 'Feenstra', 2300)
        emp_2 = Employee('Bart', 'Barnard', 2800)

        self.assertEqual(emp_1.email, 'f.feenstra@pl.hanze.nl')
        self.assertEqual(emp_2.email, 'b.barnard@pl.hanze.nl')

        emp_1.first = 'Kees'
        emp_2.first = 'Martijn'

        self.assertEqual(emp_1.email, 'k.feenstra@pl.hanze.nl')
        self.assertEqual(emp_2.email, 'm.barnard@pl.hanze.nl')

    def test_fullname(self):
        emp_1 = Employee('Fenna', 'Feenstra', 2300)
        emp_2 = Employee('Bart', 'Barnard', 2800)

        self.assertEqual(emp_1.fullname, 'Fenna Feenstra')
        self.assertEqual(emp_2.fullname, 'Bart Barnard')


        emp_1.first = 'Kees'
        emp_2.first = 'Martijn'

        self.assertEqual(emp_1.fullname, 'Kees Feenstra')
        self.assertEqual(emp_2.fullname, 'Martijn Barnard')

    def test_pay_raise(self):
        emp_1 = Employee('Fenna', 'Feenstra', 2300)
        emp_1.pay_raise()
        self.assertEqual(emp_1.pay, 2392)


#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()
