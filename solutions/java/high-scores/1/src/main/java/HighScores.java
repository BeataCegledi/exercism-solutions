import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Manages the scores of a single player. */
class HighScores {
    private final List<Integer> highScores;

    /** Creates the score list from a copy of the given list. */
    public HighScores(List<Integer> highScores) {
        this.highScores = new ArrayList<>(highScores);
    }

    /** Returns all scores. */
    List<Integer> scores() {
        return highScores;
    }

    /** Returns the most recently added score. */
    Integer latest() {
        return highScores.get(highScores.size() - 1);
    }

    /** Returns the highest score. */
    Integer personalBest() {
        return Collections.max(highScores);
    }

    /** Returns the top (up to) three scores in descending order. */
    List<Integer> personalTopThree() {
        List<Integer> sorted = new ArrayList<>(highScores);
        sorted.sort(Collections.reverseOrder());
        return sorted.subList(0, Math.min(3, sorted.size()));
    }
}
