# Transcription of DNA To M-RNA

# Helicase : unwinds double-helix structure 

# Ligase : joins Okazaki fragments in laggin strand

# Create Dictionary For Nitrogenous Base Transcription

DNA_BASES = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}

MRNA_BASES = {'A' : 'U', 'G' : 'C', 'T' : 'A', 'C' : 'G'}

# DNA Polymerase Reads Template Strand (3' to 5') left to right

# Then, creates mRNA strand from (5' to 3')

class DNA:

    def __init__(self, template_strand = "", non_template_strand = ""):
        self._template_strand = template_strand # Runs Parallel 3' to 5'
        self._non_template_strand = non_template_strand # Runs Anti-Parallel 5' to 3'
        self._genome_sequence = []

    def getTemplateStrand(self):
        print("DNA (3'- 5') Template Strand: {self._template_strand}")

    def getNonTemplateStrand(self):
        print("DNA (5'- 3') Non-Template Strand: {self._non_template_strand}") 


non_template_strand = ""

template_strand = "CAGTACGCTCACGCTCACGCTCAC"




def main():
    print("Hello, World")

if __name__ == "__main__":
    main()
    