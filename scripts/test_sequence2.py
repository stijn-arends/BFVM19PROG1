
import unittest
from sequence import DNASequence

class TestSDNASequence(unittest.TestCase):
    #work with class rather then the instance of the class
    @classmethod
    def setUpClass(cls):
        print('setUpClass\n')

    @classmethod
    def tearDownClass(cls):
        #fill this if you need final step once
        print('tearDownClass\n')


    #runs before each test
    def setUp(self):
        print('setUp\n')
        self.seq1 = DNASequence('cgcgcgcg')
        self.seq2 = DNASequence('CGCGCG')
        self.seq3 = DNASequence('AAAAAAAAAA')
        self.seq4 = DNASequence('AAAAACAAAA')
        self.seq5 = DNASequence('AAAAACAAXA')
        self.seq6 = DNASequence('AA')

    #runs after each test
    def tearDown(self):
        # delete temp stuff or other cleanup things
        print('tearDown\n')

    #these test are in random order
    def test_sequence(self):
        print('test_sequence\n')
        self.assertEqual(self.seq1.sequence, 'CGCGCGCG')

    def test_gc_content(self):
        print('test_cg_content\n ')
        self.assertEqual(self.seq1.gc_content, 1)
        self.assertEqual(self.seq2.gc_content, 1)
        self.assertEqual(self.seq3.gc_content, 0)
        self.assertEqual(self.seq4.gc_content, 0.1)


    def test_invalid_chars(self):
        print('test_invalid_chars\n')
        self.assertEqual(self.seq5.invalid_chars, {'X'})

    def test_doubble_seq(self):
        print('test_doubble_seq\n')
        self.seq6.doubble_seq()
        self.assertEqual(self.seq6.seq, 'AAAA')



#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()
