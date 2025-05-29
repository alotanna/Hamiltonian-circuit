import java.util.*;

public class RepeatedNearestNeighbor {
    private int[][] graph;
    private int numVertices;

    public RepeatedNearestNeighbor(int[][] graph) {
        this.graph = graph;
        this.numVertices = graph.length;
    }

    public Map<String, Object> findHamiltonianCircuit() {
        List<Integer> bestPath = null;
        int bestPathLength = Integer.MAX_VALUE;

        for (int start = 0; start < numVertices; start++) {
            List<Integer> path = new ArrayList<>();
            boolean[] visited = new boolean[numVertices];
            int current = start;
            int pathLength = 0;

            path.add(current);
            visited[current] = true;

            for (int i = 1; i < numVertices; i++) {
                int nearestNeighbor = -1;
                int minDistance = Integer.MAX_VALUE;

                for (int j = 0; j < numVertices; j++) {
                    if (!visited[j] && graph[current][j] < minDistance) {
                        minDistance = graph[current][j];
                        nearestNeighbor = j;
                    }
                }

                path.add(nearestNeighbor);
                visited[nearestNeighbor] = true;
                pathLength += minDistance;
                current = nearestNeighbor;
            }

            // Complete the circuit by returning to the starting vertex
            pathLength += graph[current][start];
            path.add(start);

            if (pathLength < bestPathLength) {
                bestPathLength = pathLength;
                bestPath = new ArrayList<>(path);
            }
        }

        System.out.println("Best path length: " + bestPathLength);

        Map<String, Object> result = new HashMap<>();
        result.put("path", bestPath);
        result.put("length", bestPathLength);
        return result;
    }

    public static void main(String[] args) {
        int[][] graph = {
                {0, 29, 20, 21},
                {29, 0, 15, 17},
                {20, 15, 0, 28},
                {21, 17, 28, 0}
        };

        RepeatedNearestNeighbor rnn = new RepeatedNearestNeighbor(graph);
        Map<String, Object> result = rnn.findHamiltonianCircuit();
        System.out.println("Hamiltonian Circuit Path: " + result.get("path"));
        
    }
}
