/**
 * Calculates the Hamming distance between two DNA strands,
 * i.e. the number of positions where the nucleotides differ.
 */
public class Hamming {
    private final int distance;

    /**
     * Creates a Hamming calculator and computes the distance.
     *
     * @param leftStrand  the first DNA strand
     * @param rightStrand the second DNA strand
     * @throws IllegalArgumentException if the strands have different lengths
     */
    public Hamming(String leftStrand, String rightStrand) {
        if (leftStrand.length() != rightStrand.length()) {
            throw new IllegalArgumentException("strands must be of equal length");
        }

        int count = 0;
        for (int i = 0; i < leftStrand.length(); i++) {
            if (leftStrand.charAt(i) != rightStrand.charAt(i)) {
                count++;
            }
        }
        this.distance = count;
    }

    /**
     * Returns the Hamming distance between the two strands.
     *
     * @return the number of differing positions
     */
    public int getHammingDistance() {
        return distance;
    }
}