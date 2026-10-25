import java.util.ArrayList;

/**
 * Armstrong Numbers – checks if a number is an Armstrong number.
 */
class ArmstrongNumbers {

    /**
     * Checks whether the number equals the sum of its digits,
     * each raised to the power of the digit count.
     *
     * @param numberToCheck the non-negative number to check
     * @return true if it is an Armstrong number, otherwise false
     */
    boolean isArmstrongNumber(int numberToCheck) {
        if (numberToCheck < 10) {
            return true;
        }
        ArrayList<Integer> digits = new ArrayList<>();
        int number = numberToCheck;
        while (number > 9) {
            digits.add(number % 10);
            number /= 10;
        }
        digits.add(number);
        int pow = digits.size();
        int check = 0;
        for (int digit : digits) {
            check += Math.pow(digit, pow);
        }
        return numberToCheck == check;
    }

}
