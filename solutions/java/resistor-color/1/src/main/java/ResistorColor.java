import java.util.Arrays;

/**
 * Resistor color codes: maps band colors to their numeric values (0-9).
 */
class ResistorColor {

    /**
     * Returns the numeric value of a color band.
     *
     * @param color band color, e.g. "red"
     * @return index of the color (0-9), or -1 if unknown
     */
    int colorCode(String color) {
        return Arrays.asList(this.colors()).indexOf(color);
    }

    /**
     * Lists all band colors in value order.
     *
     * @return colors from "black" (0) to "white" (9)
     */
    String[] colors() {
        return new String[] {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    }
}