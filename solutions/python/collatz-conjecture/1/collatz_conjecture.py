def steps(number):
    
    """Berechnet die Anzahl der Schritte nach der Collatz-Vermutung.

    Bei geraden Zahlen wird durch 2 geteilt,
    bei ungeraden mit 3 multipliziert und 1 addiert,
    bis 1 erreicht ist.
    """

    step = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while not number == 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = number *3 +1
            step += 1
    return step
                
