def response(hey_bob):
    
    """Gibt Bobs Antwort abhängig von der Eingabe zurück.

    Unterscheidet Schweigen, Fragen, Schreien und geschriene Fragen.
    """

    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.strip()[-1] == "?":
        return "Calm down, I know what I'm doing!" 
    if hey_bob.strip()[-1] == "?" and not hey_bob.isupper():
        return "Sure."
    if hey_bob.isupper() and hey_bob.strip()[-1] != "?":
        return "Whoa, chill out!"
    return "Whatever."