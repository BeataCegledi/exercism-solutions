public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        int Expected = 40;
        return Expected;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int spentInOven){
        return (expectedMinutesInOven() - spentInOven);
    }

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int numberOfLayers){
        int PreparationProLayer = 2;
        return (numberOfLayers * PreparationProLayer);
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int numberOfLayers, int spentInOven){
       return (preparationTimeInMinutes(numberOfLayers) + spentInOven);
    }
    
}
