import java.math.BigInteger;

/** Grains of wheat on a chessboard, doubling on each square. */
class Grains {

    /** Returns the grains on the given square (1–64): 2^(square-1). */
    BigInteger grainsOnSquare(final int square) {
        if (square > 64 || square < 1) {
            throw new IllegalArgumentException("square must be between 1 and 64");
        }
        return BigInteger.TWO.pow(square - 1);
    }

    /** Returns the total grains on all 64 squares. */
    BigInteger grainsOnBoard() {
        BigInteger summe = BigInteger.ZERO;
        for (int i = 1; i <= 64; i++) {
            summe = summe.add(grainsOnSquare(i));
        }
        return summe;
    }
}
