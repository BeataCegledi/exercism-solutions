import string
def rotate(text, key):
    """Rotate letters in text by key using Caesar cipher."""
    cipher = ""
    for letter in text:
        if  "a" <= letter <= "z":
            cipher += chr(((ord(letter) - 97 + key) % 26) + 97)
        elif "A" <= letter <= "Z":
            cipher += chr(((ord(letter) - 65 + key) % 26) + 65)         
        elif letter in (string.punctuation + " ") or letter.isdigit():
            cipher += letter
        else:
            raise ValueError("Ungültige Charaker im Text")
    return cipher
        