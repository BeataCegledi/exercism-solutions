// Basisfigur mit standardmäßiger Verwundbarkeit und Schaden.
class Fighter {

    // Gibt zurück, ob diese Figur verwundbar ist.
    boolean isVulnerable() {
        return true;
    }

    // Gibt den Grundschaden für die gegebene Figur zurück.
    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

// TODO: define the Warrior class
// Ein Krieger ist stark und niemals verwundbar.
class Warrior extends Fighter {
    // Gibt die Beschreibung des Kriegers zurück.
    @Override
    public String toString() {
        return "Fighter is a Warrior";
    }

    // Ein Krieger ist nicht verwundbar.
    @Override
    boolean isVulnerable() {
        return false;
    }

    // Gibt den Schaden zurück, den ein Krieger verursacht.
    @Override
    int getDamagePoints(Fighter fighter) {
        if (fighter.isVulnerable()) {
            return 10;
        } else {
            return 6;
        }
    }
}

// TODO: define the Wizard class
// Ein Magier kann einen Zauber vorbereiten und dadurch resistent werden.
class Wizard extends Fighter {
    boolean spellPrepared = false;

    // Gibt die Beschreibung des Magiers zurück.
    @Override
    public String toString() {
        return "Fighter is a Wizard";
    }

    // Bereitet den Zauber vor und macht den Magier widerstandsfähig.
    public boolean prepareSpell() {
        spellPrepared = true;
        return true;
    }

    // Ein Magier ist verwundbar, solange der Zauber nicht vorbereitet ist.
    @Override
    boolean isVulnerable() {
        return !spellPrepared;
    }

    // Gibt den Schaden zurück, je nachdem, ob der Zauber vorbereitet ist.
    @Override
    int getDamagePoints(Fighter fighter) {
        if (spellPrepared) {
            return 12;
        } else {
            return 3;
        }
    }
}