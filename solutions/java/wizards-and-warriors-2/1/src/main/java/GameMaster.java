/**
 * Describes characters, destinations and travel methods for narration.
 */
public class GameMaster {

    /** Describes a character's level, class and hit points. */
    public String describe(Character character){
        return "You're a level " + character.getLevel() + " " + character.getCharacterClass() + " with " + character.getHitPoints() + " hit points.";
    }

    /** Describes a destination's name and inhabitant count. */
    public String describe(Destination destination){
        return "You've arrived at " + destination.getName() + ", which has " + destination.getInhabitants() +" inhabitants.";
    }

    /** Describes the travel method; defaults to walking unless it's horseback. */
    public String describe(TravelMethod method){
        if (method == TravelMethod.HORSEBACK){
            return "You're traveling to your destination on horseback.";
        }
        else {
            return "You're traveling to your destination by walking.";
        }
    }

    /** Describes the full journey: character, travel method, then destination. */
    public String describe(Character character, Destination destination, TravelMethod method){
        return describe(character) + " " + describe(method) + " " + describe(destination);
    }

    /** Describes the journey assuming travel by walking. */
    public String describe(Character character, Destination destination){
        return describe(character) + " " + describe(TravelMethod.WALKING) + " " + describe(destination);
    }
}
