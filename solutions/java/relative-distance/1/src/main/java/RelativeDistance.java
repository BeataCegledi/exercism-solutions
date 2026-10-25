import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Set;

/**
 * Computes the degree of separation between two people in a family tree.
 *
 * Parents, children and siblings are direct relatives (distance 1).
 */
class RelativeDistance {
    /** Undirected graph: person -> direct relatives. */
    private final Map<String, Set<String>> family = new HashMap<>();

    /**
     * Builds the relative graph from the family tree.
     *
     * @param familyTree parent -> list of children
     */
    RelativeDistance(Map<String, List<String>> familyTree) {
        for (var entry : familyTree.entrySet()) {
            String parent = entry.getKey();
            List<String> children = entry.getValue();
            family.computeIfAbsent(parent, key -> new HashSet<>()).addAll(children);
            for (String child : children) {
                Set<String> contact = family.computeIfAbsent(child, key -> new HashSet<>());
                contact.add(parent);
                contact.addAll(children);
                contact.remove(child);
            }
        }
    }

    /**
     * Returns the shortest number of connections between two people (BFS).
     *
     * @param personA start person
     * @param personB target person
     * @return degree of separation, 0 if same person, -1 if not related
     */
    int degreeOfSeparation(String personA, String personB) {
        if (personA.equals(personB)) { return 0; }
        Queue<String> line = new ArrayDeque<>(); // FIFO
        line.offer(personA);
        Map<String, Integer> distance = new HashMap<>(); // also serves as "seen"
        distance.put(personA, 0);
        while (!line.isEmpty()) {
            String act = line.poll();
            for (String member : family.getOrDefault(act, Set.of())) {
                if (!distance.containsKey(member)) { // not seen yet
                    distance.put(member, distance.get(act) + 1);
                    if (member.equals(personB)) {
                        return distance.get(member);
                    }
                    line.offer(member);
                }
            }
        }
        return -1;
    }
}