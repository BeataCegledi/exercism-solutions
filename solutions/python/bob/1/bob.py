def response(hey_bob):
    
    """Gibt Bobs Antwort abhängig von der Eingabe zurück.

    Unterscheidet Schweigen, Fragen, Schreien und geschriene Fragen.
    """

    if hey_bob.strip() == '':
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob.strip()[-1] == '?':
        return "Calm down, I know what I'm doing!" 
    elif hey_bob.strip()[-1] == '?' and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and hey_bob.strip()[-1] != '?':
        return "Whoa, chill out!"
    return "Whatever."