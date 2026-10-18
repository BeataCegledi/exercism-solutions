class School:
    """Verwaltet eine Schüler-Liste pro Klasse (Roster)."""

    schule = {}
    add = []

    def __init__(self):
        self.schule = {}
        self.add = []

    def add_student(self, name, grade):
        """Fügt einen Schüler der angegebenen Klasse hinzu.

        Wird nicht hinzugefügt, wenn der Name bereits in irgendeiner
        Klasse vorhanden ist.
        """
        if grade not in self.schule:
            self.schule[grade] = []
        if any(name.capitalize() in self.schule[gr] for gr in self.schule):
            self.add.append(False)
        else:
            self.schule[grade].append(name.capitalize())
            self.add.append(True)

    def roster(self):
        """Gibt alle Schüler zurück, sortiert nach Klasse und Name."""
        return [name for klasse in sorted(self.schule) for name in sorted(self.schule[klasse])]

    def grade(self, grade_number):
        """Gibt die sortierte Schülerliste der angegebenen Klasse zurück."""
        return sorted(self.schule.get(grade_number, []))

    def added(self):
        """Gibt zurück, welche add_student-Aufrufe erfolgreich waren."""
        return self.add
