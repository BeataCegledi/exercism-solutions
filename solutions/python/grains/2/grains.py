"""Berechnung der Weizenkörner auf einem Schachbrett.

Auf jedem Feld des Schachbretts verdoppelt sich die Anzahl der Weizenkörner
im Vergleich zum vorherigen Feld. Dieses Modul stellt Funktionen zur
Berechnung der Körner pro Feld und der Gesamtanzahl bereit.
"""


def square(number):
    """Gib die Anzahl der Weizenkörner auf einem bestimmten Feld zurück."""
    if 0 < number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Gib die Gesamtanzahl der Weizenkörner auf dem Schachbrett zurück."""
    grains = 0
    for i in range(64):
        grains += 2 ** i
    return grains