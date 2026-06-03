"""Convert numbers to English words."""
NUMWORDS = {1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred"}

def translate_group(current):
    """Convert 1-999 to English words."""
    parts = []
    if current >= 100:
        hundreds = current // 100
        parts.append(NUMWORDS[hundreds]+" hundred")
        current = current % 100

    if current in NUMWORDS:
        parts.append(NUMWORDS[current])
    elif current > 20: 
        ones = current % 10
        tens = current - ones
        parts.append(f"{NUMWORDS[tens]}-{NUMWORDS[ones]}")
    return " ".join(parts)

def say(number):
    """Convert integer to English words (0-999,999,999,999)."""
    if number == 0:
        return "zero"
    if not 0 < number <= 999999999999:
        raise ValueError("input out of range")

    groups = [(1_000_000_000, " billion"),
              (1_000_000, " million"),
              (1_000, " thousand")]
    
    result = []
    for group, name in groups:
        if number >= group:
            result.append(translate_group(number // group)+name)
            number = number % group
            
    if number > 0:
        result.append(translate_group(number))
        
    return " ".join(result)
