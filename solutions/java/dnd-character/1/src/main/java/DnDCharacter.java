import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.Collections;

/**
 * D&D character generator with six random ability scores.
 * Each ability: roll 4 dice, sum the largest 3.
 */
class DnDCharacter {
    private int strength, dexterity, constitution, intelligence, wisdom, charisma;

    /** Creates a character with six randomly rolled abilities. */
    public DnDCharacter(){
        this.strength = ability(rollDice());
        this.dexterity = ability(rollDice());
        this.constitution = ability(rollDice());
        this.intelligence = ability(rollDice());
        this.wisdom = ability(rollDice());
        this.charisma = ability(rollDice());
    }

    /**
     * Sums the largest three of four dice.
     *
     * @param scores four dice values (may be immutable)
     * @return sum of all dice minus the smallest
     */
    int ability(List<Integer> scores) {
        int sum = 0;
        for (int d : scores) {
            sum += d;
        }
        sum -= Collections.min(scores);
        return sum;
    }

    /**
     * Rolls four 6-sided dice.
     *
     * @return list of four values between 1 and 6
     */
    List<Integer> rollDice() {
        ArrayList<Integer> dice = new ArrayList<>();
        Random random = new Random();
        for (int i=0; i<4; i++){
            dice.add(random.nextInt(6)+1);
        }
        return dice;
    }

    /**
     * Calculates the ability modifier.
     *
     * @param input ability score
     * @return (input - 10) / 2, rounded down (floorDiv for negatives)
     */
    int modifier(int input) {
        return Math.floorDiv((input-10),2);
    }

    /** @return strength score */
    int getStrength() {
        return this.strength;
    }

    /** @return dexterity score */
    int getDexterity() {
        return this.dexterity;
    }

    /** @return constitution score */
    int getConstitution() {
        return this.constitution;
    }

    /** @return intelligence score */
    int getIntelligence() {
        return this.intelligence;
    }

    /** @return wisdom score */
    int getWisdom() {
        return this.wisdom;
    }

    /** @return charisma score */
    int getCharisma() {
        return this.charisma;
    }

    /** @return 10 + constitution modifier */
    int getHitpoints() {
        return (10 + modifier(this.constitution));
    }
}