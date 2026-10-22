import java.util.List;
import java.util.ArrayList;

public class TestTrack {

    public static void race(RemoteControlCar car) {
     car.drive();
    }

    public static List<ProductionRemoteControlCar> getRankedCars(List<ProductionRemoteControlCar> cars) {
    List<ProductionRemoteControlCar> sorted = new ArrayList<>(cars);

    for (int j = 0; j < sorted.size() - 1; j++) {
        for (int i = 0; i < sorted.size() - 1 - j; i++) {
            if (sorted.get(i).compareTo(sorted.get(i + 1)) > 0) {
                ProductionRemoteControlCar temp = sorted.get(i);
                sorted.set(i, sorted.get(i + 1));
                sorted.set(i + 1, temp);
            }
        }
    }

    return sorted;
    }
}
