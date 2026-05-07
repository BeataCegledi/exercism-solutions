def to_rna(dna_strand):
    """"
    Return the RNA complement of a DNA strand by replacing each nucleotide
    with its corresponding RNA base according to transcription rules.
    """

    rna = ""
    for letter in dna_strand:
        if letter.upper() == "G":
            rna += "C"
        elif letter.upper() == "C":
            rna += "G"
        elif letter.upper() == "T":
            rna += "A"
        elif letter.upper() == "A":
            rna += "U"
    return rna
