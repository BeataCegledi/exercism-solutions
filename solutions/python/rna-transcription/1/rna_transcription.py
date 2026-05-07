def to_rna(dna_strand):
    """"
    Return the RNA complement of a DNA strand by replacing each nucleotide
    with its corresponding RNA base according to transcription rules.
    """

    rna = ""
    for letter in dna_strand:
        if letter.upper() == "G":
            letter = "C"
        elif letter.upper() == "C":
            letter = "G"
        elif letter.upper() == "T":
            letter = "A"
        elif letter.upper() == "A":
            letter = "U"
        rna += letter  
    return rna
