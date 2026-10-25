/**
 * Two-fer – builds a "one for X, one for me" sentence.
 */
public class Twofer {

    /**
     * Returns the two-fer sentence; uses "you" if name is null.
     *
     * @param name the recipient's name, or null
     * @return "One for <name>, one for me."
     */
    public String twofer(String name) {
        if (name == null) {
            name = "you";
        }
        return "One for " + name + ", one for me.";
    }

}