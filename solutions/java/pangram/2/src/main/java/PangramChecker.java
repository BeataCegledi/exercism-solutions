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
     * Removes all non-letters with a regex, then counts the distinct letters left.
     *
     * @param input the sentence to check
     * @return true if 26 distinct letters remain, otherwise false
     */
    public boolean isPangram(String input) {
        input = input.toLowerCase().replaceAll("[^a-z]", "");
        return input.chars().distinct().count() == 26;
    }
}