public class Lasagna {

    public int expectedMinutesInOven(){
        int Expected = 40;
        return Expected;
    }

    public int remainingMinutesInOven(int spentInOven){
        return (expectedMinutesInOven() - spentInOven);
    }


    public int preparationTimeInMinutes(int numberOfLayers){
        int PreparationProLayer = 2;
        return (numberOfLayers * PreparationProLayer);
    }

    
    public int totalTimeInMinutes(int numberOfLayers, int spentInOven){
       return (preparationTimeInMinutes(numberOfLayers) + spentInOven);
    }
    
}
