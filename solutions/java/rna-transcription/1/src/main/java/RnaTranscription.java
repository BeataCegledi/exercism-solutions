class RnaTranscription {
    String transcribe(String dnaStrand){
        StringBuilder rnaStrand = new StringBuilder();     
        for (char dna : dnaStrand.toCharArray()){
        char rna = switch (dna) {
            case 'G' -> 'C';
            case 'C' -> 'G';
            case 'T' -> 'A';
            case 'A' -> 'U';
            default -> '?';   
            };
            rnaStrand.append(rna);
        }
        return rnaStrand.toString();
    }
}
