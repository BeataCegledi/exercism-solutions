import java.util.List;

/**
 * Decodes the resistance value of a resistor from its three color bands.
 */
class ResistorColorTrio {

    /** Color bands in order of their digit value (index = value). */
    static final List<String> COLOR = List.of("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white");

    /** Units in steps of 1000 (index = number of divisions by 1000). */
    static final List<String> UNIT = List.of(" ohms", " kiloohms", " megaohms", " gigaohms");

    /**
     * Returns the resistance as a human-readable label with metric prefix.
     *
     * @param colors three color bands: two digits and the exponent of ten
     * @return the resistance value with its unit, e.g. "33 kiloohms"
     */
    String label(String[] colors) {
        int exp = COLOR.indexOf(colors[2]);
        long value = (COLOR.indexOf(colors[0]) * 10 + COLOR.indexOf(colors[1])) * (long) Math.pow(10, exp);
        int i = 0;
        while (value != 0 && value % 1000 == 0) {
            i++;
            value /= 1000;
        }
        return value + UNIT.get(i);
    }
}