/**
 * Performs a basic calculation (addition, multiplication or division) on two operands.
 */
class CalculatorConundrum {

    /**
     * Calculates the result and returns it as a formatted string.
     * # operation is "+" or "*" -> returns the formatted sum/product
     * # operation is "/" and operand2 is 0 -> throws IllegalOperationException
     * # operation is null or empty -> throws IllegalArgumentException
     * # operation is anything else -> throws IllegalOperationException
     * @param operand1 first number
     * @param operand2 second number
     * @param operation one of "+", "*", "/"
     * @return formatted calculation, e.g. "3 + 4 = 7"
     */
    public String calculate(int operand1, int operand2, String operation) {
        switch (operation){
        case "+": {
            return operand1 + " + " + operand2 + " = " + (operand1+operand2);}
        case "*": {
            return operand1 + " * " + operand2 + " = " + (operand1*operand2);}
        case "/": {
            try {
                return operand1 + " / " + operand2 + " = " + (operand1/operand2);
            } catch (ArithmeticException e){
                throw new IllegalOperationException("Division by zero is not allowed",e);}
            }
        case null: {
            throw new IllegalArgumentException("Operation cannot be null");}
        case "": {
            throw new IllegalArgumentException("Operation cannot be empty");}
        default: {
            throw new IllegalOperationException("Operation '"+operation+"' does not exist");
            }
        }
    }
}
