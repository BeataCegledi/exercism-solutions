class SpaceAge:
    """Berechnet das Alter in Jahren der jeweiligen Planeten anhand gegebener Sekunden."""

    def __init__(self, seconds):
        """Speichert die vergangenen Sekunden."""
        self.seconds = seconds

    sec_per_year = 365.25 * 24 * 60 * 60

    def on_earth(self):
        """Alter in Erdjahren."""
        return round(self.seconds/self.sec_per_year, 2)

    def on_mercury(self):
        """Alter in Merkur-Jahren (Umlaufzeit: 0.2408467 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 0.2408467, 2)

    def on_venus(self):
        """Alter in Venus-Jahren (Umlaufzeit: 0.61519726 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 0.61519726, 2)

    def on_mars(self):
        """Alter in Mars-Jahren (Umlaufzeit: 1.8808158 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 1.8808158, 2)

    def on_jupiter(self):
        """Alter in Jupiter-Jahren (Umlaufzeit: 11.862615 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 11.862615, 2)

    def on_saturn(self):
        """Alter in Saturn-Jahren (Umlaufzeit: 29.447498 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 29.447498, 2)

    def on_uranus(self):
        """Alter in Uranus-Jahren (Umlaufzeit: 84.016846 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 84.016846, 2)

    def on_neptune(self):
        """Alter in Neptun-Jahren (Umlaufzeit: 164.79132 Erdjahre)."""
        return round(self.seconds/self.sec_per_year / 164.79132, 2)

    