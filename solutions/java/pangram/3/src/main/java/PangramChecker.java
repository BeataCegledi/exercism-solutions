import java.util.stream.IntStream;

/**
 * Checks whether a sentence is a pangram.
 *
 * A pangram contains every letter of the alphabet (a-z) at least once.
 * Case-insensitive; non-letters are ignored.
 */
public class PangramChecker {

    /**
     * Checks whether the input contains every letter from a to z.
     *
     * Uses IntStream.allMatch, which stops at the first missing letter.
     *
     * @param input the sentence to check
     * @return true if all 26 letters occur, otherwise false
     */
    public boolean isPangram(String input) {
        String lower = input.toLowerCase();
        return IntStream.rangeClosed('a', 'z').allMatch(ch -> lower.indexOf(ch) >= 0);
    }
}