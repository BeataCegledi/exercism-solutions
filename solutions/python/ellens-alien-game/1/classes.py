"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Erstellt einen Alien an den angegebenen Koordinaten mit 3 Lebenspunkten und erhöht den                 Anzahl von allen erstellten Aliens"""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Verringert die Lebenspunkte des Aliens um eins."""
        self.health-=1

    def is_alive(self):
        """Gibt zurück, ob der Alien noch lebt (health > 0)."""
        return self.health > 0

    def teleport(self,x_coordinate, y_coordinate):
        """Versetzt den Alien an die neuen Koordinaten."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, alien):     
        """Kollisionserkennung zwischen zwei Aliens (noch nicht implementiert)."""
        pass
    

#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates
def new_aliens_collection(alien_start_positons):
    """Erstellt eine Liste von Alien-Objekten aus den angegebenen (x, y)-Koordinaten."""
    aliens = []
    for positions in alien_start_positons:
        aliens.append(Alien(positions[0], positions[1]))
    return aliens
