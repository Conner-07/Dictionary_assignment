
def create_deck():
    """
    Create dictionaries to represent a standard deck of 52 playing cards 

    Schema 1:
    {Suit : {Value : {}}}
    Schema 2:
    {Value : {Suit : {}}}
  """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # Schema 1: {Suit : {Value : {}}}
    deck_schema1 = {suit: {value: {} for value in values} for suit in suits}

    # Schema 2: {Value : {Suit : {}}}
    deck_schema2 = {value: {suit: {} for suit in suits} for value in values}

    return deck_schema1, deck_schema2

# Test the function
deck_schema1, deck_schema2 = create_deck()
print("Schema 1:")
print(deck_schema1)
print("\nSchema 2:")
print(deck_schema2)


def translate_rna(rna_sequence, print_length=False, print_most_common_codon=False):
    # RNA codon table (from the provided link)
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    protein_sequence = ""
    codon_frequency = {}

    # Translate RNA sequence into protein sequence
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            protein_sequence += amino_acid
            codon_frequency[codon] = codon_frequency.get(codon, 0) + 1

    # Printing length of the encoded protein sequence
    if print_length:
        print("Length of encoded protein:", len(protein_sequence))

    # Printing most commonly occurring codon 
    if print_most_common_codon:
        most_common_codon = max(codon_frequency, key=codon_frequency.get)
        print("Most commonly occurring codon:", most_common_codon)

    return protein_sequence

# Test Case:
rna_sequence = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGT..."
encoded_protein = translate_rna(rna_sequence, print_length=True, print_most_common_codon=True)
print("Encoded Protein Sequence:", encoded_protein)
