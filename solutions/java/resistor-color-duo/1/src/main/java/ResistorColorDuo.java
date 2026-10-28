import java.util.Arrays;
import java.util.List;

/**
 * Resistor color duo: two color bands give a two-digit value.
 */
class ResistorColorDuo {
    /** Band colors in value order: "black" (0) to "white" (9). */
    static final String[] COLOR = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};

    /**
     * Calculates the value of the first two color bands.
     *
     * @param colors band colors; only the first two are used
     * @return first color * 10 + second color, e.g. {"yellow", "violet"} -> 47
     */
    int value(String[] colors) {
        List<String> list = Arrays.asList(COLOR);
        return (list.indexOf(colors[0])*10+list.indexOf(colors[1]));
    }
}
