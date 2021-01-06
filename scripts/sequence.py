
class DNASequence:

    def __init__(self, seqstring):
        self.seq = seqstring

    @property
    def sequence(self):
        return self.seq.upper()

    @property
    def gc_content(self):
        """"Return the percentage of G and C characters in the sequence"""
        return (self.seq.upper().count('G') + self.seq.upper().count('C')) / len(self.seq)

    @property
    def invalid_chars(self):
        """Check for invalid characters """
        return {char for char in self.seq if char not in 'TCAGtcag'}

    def doubble_seq(self):
        self.seq = self.seq * 2
