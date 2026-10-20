/** Ferngesteuertes Auto mit begrenztem Akku. */
class NeedForSpeed {
    private final int speed;
    private final int batteryDrain;
    private int hasDriven = 0;
    private int charged = 100;

    public NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    /** Prüft, ob der Akku für eine weitere Fahrt nicht mehr ausreicht. */
    public boolean batteryDrained() {
        return (charged < this.batteryDrain);
    }

    /** Gibt die bisher gefahrene Strecke zurück. */
    public int distanceDriven() {
        return this.hasDriven;
    }

    /** Fährt eine Runde, falls noch genug Akku vorhanden ist. */
    public void drive() {
        if (!batteryDrained()){
            hasDriven += this.speed;
            charged -= this.batteryDrain;
        }
    }

    /** Erzeugt ein Auto mit hoher Geschwindigkeit und hohem Akkuverbrauch. */
    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50,4);
    }
}

/** Rennstrecke mit fester Länge. */
class RaceTrack {
    private final int distance;

    public RaceTrack(int distance) {
       this.distance = distance;
    }

    /** Prüft, ob das Auto die Strecke vor Akku-Ende schafft. */
    public boolean canFinishRace(NeedForSpeed car) {
        while (distance > car.distanceDriven() && !car.batteryDrained()) {
            car.drive();
        }
        return car.distanceDriven() >= distance;    
    }
}