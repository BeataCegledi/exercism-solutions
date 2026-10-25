import java.util.Map;
import java.util.HashMap;

/**
 * Manages a mapping of international dialing codes to country names.
 */
public class DialingCodes {
    private Map<Integer, String> dialingCodes = new HashMap<>();

    /**
     * Returns all dialing codes.
     *
     * @return map of dialing codes to countries
     */
    public Map<Integer, String> getCodes() {
        return dialingCodes;
    }

    /**
     * Adds or overwrites a dialing code.
     *
     * @param code    the dialing code
     * @param country the country name
     */
    public void setDialingCode(Integer code, String country) {
        dialingCodes.put(code, country);
    }

    /**
     * Returns the country for a dialing code.
     *
     * @param code the dialing code
     * @return the country name, or null if not found
     */
    public String getCountry(Integer code) {
        return dialingCodes.get(code);
    }

    /**
     * Adds a dialing code only if neither the code nor the country exists yet.
     *
     * @param code    the dialing code
     * @param country the country name
     */
    public void addNewDialingCode(Integer code, String country) {
        if (!(dialingCodes.containsValue(country) || dialingCodes.containsKey(code))){
            setDialingCode(code, country);
        }
    }

    /**
     * Finds the dialing code of a country.
     *
     * @param country the country name
     * @return the dialing code, or null if not found
     */
    public Integer findDialingCode(String country) {
        for (Map.Entry<Integer, String> entry : dialingCodes.entrySet()) {
            if (entry.getValue().equals(country)){
                return entry.getKey();
            }
        }
        return null;
    }

    /**
     * Replaces the dialing code of an existing country.
     * Does nothing if the country is not found.
     *
     * @param code    the new dialing code
     * @param country the country name
     */
    public void updateCountryDialingCode(Integer code, String country) {
        Integer oldCode = findDialingCode(country);
        if (oldCode != null) {
            dialingCodes.remove(oldCode);
            dialingCodes.put(code, country);
        }
    }
}