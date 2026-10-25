/**
 * Exercism: Leap – decides whether a year is a leap year.
 */
class Leap {

    /**
     * Checks whether the given year is a leap year.
     *
     * A year is a leap year if it is divisible by 4,
     * except when it is divisible by 100, unless it is also divisible by 400.
     *
     * @param year the year to check
     * @return true if the year is a leap year, otherwise false
     */
    boolean isLeapYear(int year) {
        if (year % 400 == 0) {
            return true;
        }
        if (year % 100 == 0) {
            return false;
        }
        return year % 4 == 0;
    }

}