
import unittest
from sequence import DNASequence

class TestSDNASequence(unittest.TestCase):


    def test_sequence(self):

        seq1 = DNASequence('cgcgcgcg')
        self.assertEqual(seq1.sequence, 'CGCGCGCG')

    def test_gc_content(self):

        seq1 = DNASequence('cgcgcgcg')
        self.assertEqual(seq1.gc_content, 1)

        seq2 = DNASequence('CGCGCG')
        self.assertEqual(seq2.gc_content, 1)

        seq3 = DNASequence('AAAAAAAAAA')
        self.assertEqual(seq3.gc_content, 0)

        seq4 = DNASequence('AAAAACAAAA')
        self.assertEqual(seq4.gc_content, 0.1)


    def test_invalid_chars(self):

        seq5 = DNASequence('AAAAACAAXA')
        self.assertEqual(seq5.invalid_chars, {'X'})

    def test_doubble_seq(self):
        seq6 = DNASequence('AA')
        seq6.doubble_seq()
        self.assertEqual(seq6.seq, 'AAAA')



#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()
