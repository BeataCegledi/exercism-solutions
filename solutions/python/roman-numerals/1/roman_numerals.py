'''Convert Arabic numerals to Roman numerals (1..3999).'''

CONVERT = {1000 : 'M', 900 : 'CM', 
           500 : 'D', 400 : 'CD', 
           100 : 'C', 90 : 'XC',
           50 : 'L', 40 : 'XL',
           10 : 'X', 9 : 'IX',
           5 : 'V', 4: 'IV', 1 : 'I'
          }
def roman(number):
    '''Return the Roman numeral representation of `number`.'''
    
    zahl = ''
    for key, value in CONVERT.items():
        while number >= key:
            zahl += value
            number -= key
    return zahl