/**
 * Calculates the score of a single dart throw on a circular target.
 */
class Darts {

    /**
     * Returns the points for a dart landing at (x, y).
     *
     * Inner circle (r ≤ 1): 10, middle (r ≤ 5): 5, outer (r ≤ 10): 1, outside: 0.
     *
     * @param xOfDart x coordinate of the dart
     * @param yOfDart y coordinate of the dart
     * @return the score (10, 5, 1 or 0)
     */
    int score(double xOfDart, double yOfDart) {
        double dist = Math.hypot(xOfDart, yOfDart);
        if (dist <= 1) {
            return 10;
        }
        if (dist <= 5) {
            return 5;
        }
        if (dist <= 10) {
            return 1;
        }
        return 0;
    }
}