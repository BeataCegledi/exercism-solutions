'''Return True if number is an Armstrong number (sum of digits each raised to the power of digit         count equals the number).'''
    
def is_armstrong_number(number):
    armstrong = 0
    for digit in str(number):
        armstrong += int(digit) ** len(str(number))
    return number == armstrong
        