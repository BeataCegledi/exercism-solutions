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
        'UGG' : 'Tryptophan',
        'UAA' : 'STOP',
        'UAG' : 'STOP',
        'UGA' : 'STOP'}

def proteins(strand):
    '''Return the list of proteins encoded by the given RNA strand.

    Reads the strand codon by codon (3 nucleotides) and stops
    at the first STOP codon (UAA, UAG, UGA).'''
    
    stop = False
    count = 0
    protein = []
    while count < len(strand) and not stop:
        current = strand[count:count+3]
        count += 3
        if current in ('UAA', 'UAG', 'UGA'):
            stop = True
        else:
            protein.append(CODONS[current])
    return protein