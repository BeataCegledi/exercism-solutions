class NaturalNumber {
    private int number;
    NaturalNumber(int number) {
        if (number <= 0) {
            throw new IllegalArgumentException("You must supply a natural number (positive integer)");
        }
       this.number = number;
    }

    Classification getClassification() {
        int aliquot = 0;
        for (int i = 1; i<=number/2; i++){
            if (number % i == 0){
                aliquot += i;
            }
        }
        Classification ergebnis = number == aliquot ? Classification.PERFECT : (number > aliquot ?         Classification.DEFICIENT : Classification.ABUNDANT);
        return ergebnis;
    }
}
