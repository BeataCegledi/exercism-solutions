/**
 * Reverse String – reverses the order of characters in a string.
 */
class ReverseString {

    /**
     * Reverses the given string.
     *
     * @param inputString the string to reverse (may be empty)
     * @return the characters of inputString in reverse order
     */
    String reverse(String inputString) {
        return new StringBuilder(inputString).reverse().toString();
    }
}
