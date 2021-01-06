"""
   unit test program for person class in person.py
   usage: python3 -m unittest test_person.py

"""

import unittest
from person import Person

class TestPerson(unittest.TestCase):

    def test_email(self):
        pers = Person('Fenna', 'Feenstra', 65, 174)
        pers_2 = Person('Bart', 'Barnard', 85, 185)

        self.assertEqual(pers_1.email, 'f.feenstra@st.hanze.nl')
        self.assertEqual(pers_2.email, 'b.barnard@st.hanze.nl')

        pers_1.first = 'Roxanne'
        pers_2.first = 'Martin'

        self.assertEqual(pers_1.email, 'r.feenstra@st.hanze.nl')
        self.assertEqual(pers_2.email, 'm.barnard@st.hanze.nl')

    def test_fullname(self):
        pers_1 = Person('Fenna', 'Feenstra', 65, 174)
        pers_2 = Person('Bart', 'Barnard', 85, 185)

        self.assertEqual(pers_1.fullname, 'Fenna Feenstra')
        self.assertEqual(pers_2.fullname, 'Bart Barnard')


        pers_1.first = 'Kees'
        pers_2.first = 'Martijn'

        self.assertEqual(pers_1.fullname, 'Kees Feenstra')
        self.assertEqual(pers_2.fullname, 'Martijn Barnard')

    def test_bmi(self):
        pers_1 = Person('Fenna', 'Feenstra', 65, 173)
        self.assertTrue(pers_1.bmi > 21 and pers_1.bmi < 22)


#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()
