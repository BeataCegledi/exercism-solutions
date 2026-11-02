/**
 * Calculates the difference between the square of the sum
 * and the sum of the squares of the first n natural numbers,
 * using closed-form formulas (O(1)) instead of loops.
 */
class DifferenceOfSquaresCalculator {

    /**
     * Returns the square of the sum of the numbers from 1 to input.
     * Uses Gauss' formula: n(n+1) / 2.
     *
     * @param input the upper limit (inclusive)
     * @return (1 + 2 + ... + input)²
     */
    int computeSquareOfSumTo(int input) {
        int summe = input * (input + 1) / 2;
        return summe * summe;
    }

    /**
     * Returns the sum of the squares of the numbers from 1 to input.
     * Uses the formula: n(n+1)(2n+1) / 6.
     *
     * @param input the upper limit (inclusive)
     * @return 1² + 2² + ... + input²
     */
    int computeSumOfSquaresTo(int input) {
        return input * (input + 1) * (2 * input + 1) / 6;
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