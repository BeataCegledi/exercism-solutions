import java.util.Collection;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

/**
 * An internal DSL for building graphs, similar to the Graphviz DOT language.
 * Nodes and edges are added through chainable method calls.
 */
public class Graph {
    private final Collection<Edge> edges = new ArrayList<>();
    private final Collection<Node> nodes = new ArrayList<>();
    private Map<String, String> attributes = new HashMap<>();

    /** Creates an empty graph without attributes. */
    public Graph() {
    }

    /**
     * Creates an empty graph with the given attributes.
     *
     * @param attributes the graph attributes, e.g. {@code bgcolor=yellow}
     */
    public Graph(Map<String, String> attributes) {
        this.attributes = attributes;
    }

    /** @return all nodes of the graph */
    public Collection<Node> getNodes() {
        return this.nodes;
    }

    /** @return all edges of the graph */
    public Collection<Edge> getEdges() {
        return this.edges;
    }

    /**
     * Adds a node without attributes.
     *
     * @param name the node name
     * @return this graph, for method chaining
     */
    public Graph node(String name) {
        Node n = new Node(name);
        nodes.add(n);
        return this;
    }

    /**
     * Adds a node with attributes.
     *
     * @param name       the node name
     * @param attributes the node attributes, e.g. {@code color=red}
     * @return this graph, for method chaining
     */
    public Graph node(String name, Map<String, String> attributes) {
        Node n = new Node(name, attributes);
        nodes.add(n);
        return this;
    }

    /**
     * Adds an edge between two nodes without attributes.
     *
     * @param start the start node name
     * @param end   the end node name
     * @return this graph, for method chaining
     */
    public Graph edge(String start, String end) {
        Edge e = new Edge(start, end);
        edges.add(e);
        return this;
    }

    /**
     * Adds an edge between two nodes with attributes.
     *
     * @param start      the start node name
     * @param end        the end node name
     * @param attributes the edge attributes, e.g. {@code color=green}
     * @return this graph, for method chaining
     */
    public Graph edge(String start, String end, Map<String, String> attributes) {
        Edge e = new Edge(start, end, attributes);
        edges.add(e);
        return this;
    }

    /** @return the attributes of the graph itself */
    public Map<String, String> getAttributes() {
        return this.attributes;
    }
}
