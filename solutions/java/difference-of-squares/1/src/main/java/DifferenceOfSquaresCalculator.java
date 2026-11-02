/**
 * Calculates the difference between the square of the sum
 * and the sum of the squares of the first n natural numbers.
 */
class DifferenceOfSquaresCalculator {

    /**
     * Returns the square of the sum of the numbers from 1 to input.
     *
     * @param input the upper limit (inclusive)
     * @return (1 + 2 + ... + input)²
     */
    int computeSquareOfSumTo(int input) {
        int summe = 0;
        for (int i = 1; i <= input; i++) {
            summe += i;
        }
        return summe * summe;
    }

    /**
     * Returns the sum of the squares of the numbers from 1 to input.
     *
     * @param input the upper limit (inclusive)
     * @return 1² + 2² + ... + input²
     */
    int computeSumOfSquaresTo(int input) {
        int summe = 0;
        for (int i = 1; i <= input; i++) {
            summe += i * i;
        }
        return summe;
    }

    /**
     * Returns the difference between the square of the sum
     * and the sum of the squares from 1 to input.
     *
     * @param input the upper limit (inclusive)
     * @return squareOfSum - sumOfSquares
     */
    int computeDifferenceOfSquares(int input) {
        return computeSquareOfSumTo(input) - computeSumOfSquaresTo(input);
    }
}
