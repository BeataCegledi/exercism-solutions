public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double rate;
        int carsPerHour = 221;
        if (speed <= 4) { rate = speed * carsPerHour; }
        else if (speed <= 8) {rate  = speed * carsPerHour * 0.90;}
        else if (speed == 9) {rate  = speed * carsPerHour * 0.80;}
        else {rate  = speed * carsPerHour * 0.77;}
        return rate;        
    }

    public int workingItemsPerMinute(int speed) {
       return (int) (productionRatePerHour(speed) / 60);
    }
}
