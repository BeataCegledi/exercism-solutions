public class JedliksToyCar {
    private int METERS = 0;
    private int PERCENTAGE = 100;
    
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {  
        return ("Driven " + this.METERS + " meters");
    }

    public String batteryDisplay() {
        return (this.PERCENTAGE == 0) ? "Battery empty" : ("Battery at " + this.PERCENTAGE + "%");
    }

    public void drive() {
        if (this.PERCENTAGE > 0) {
            this.METERS += 20;
            this.PERCENTAGE--;
        }
    }
}
