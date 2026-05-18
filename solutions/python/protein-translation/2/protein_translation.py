'''Translate an RNA strand into the corresponding sequence of proteins.'''
CODONS = {'AUG' : 'Methionine', 
        'UUU' : 'Phenylalanine',
        'UUC' : 'Phenylalanine',
        'UUA' : 'Leucine',
        'UUG' : 'Leucine',
        'UCU' : 'Serine',
        'UCC' : 'Serine',
        'UCA' : 'Serine',
        'UCG' : 'Serine',
        'UAU' : 'Tyrosine',
        'UAC' : 'Tyrosine',
        'UGU' : 'Cysteine',
        'UGC' : 'Cysteine',
        'UGG' : 'Tryptophan'}

STOP = {'UAA', 'UAG', 'UGA'}

def proteins(strand):
    '''Return the list of proteins encoded by the given RNA strand.

    Reads the strand codon by codon (3 nucleotides) and stops
    at the first STOP codon (UAA, UAG, UGA).'''
    
    protein = []
    for count in range(0,len(strand),3):
        current = strand[count:count+3]
        if current in STOP:
            break
        protein.append(CODONS[current])
    return protein