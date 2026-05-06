def is_isogram(string):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if string.lower().count(letter)>1 :
            return False
    return True

   # string = string.lower().replace(" ","").replace("-","")   
    # return len(string) == len(set(string))
    