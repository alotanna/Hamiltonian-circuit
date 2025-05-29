#include <iostream>
#include <vector>
#include <set>
#include <limits>
#include <algorithm>
using namespace std;

class Graph {
private:
    int V; // Number of vertices
    vector<vector<int>> adj; // Adjacency matrix

public:
    // Constructor
    Graph(int vertices) : V(vertices) {
        // Initialize adjacency matrix with zeros
        adj.resize(V, vector<int>(V, 0));
    }

    // Add an edge to the graph
    void addEdge(int u, int v, int weight) {
        adj[u][v] = weight;
        adj[v][u] = weight; // For undirected graph
    }

    // Implementation of Nearest Neighbor Algorithm
    vector<int> findHamiltonianCircuit(int start) {
        vector<int> path;
        set<int> unvisited;
        
        // Initialize unvisited set with all vertices except start
        for (int i = 0; i < V; i++) {
            if (i != start) {
                unvisited.insert(i);
            }
        }
        
        // Add starting vertex to path
        path.push_back(start);
        int current = start;
        
        // Main algorithm loop
        while (!unvisited.empty()) {
            int nearest = -1;
            int minWeight = numeric_limits<int>::max();
            
            // Find nearest unvisited vertex
            for (const int& v : unvisited) {
                if (adj[current][v] != 0 && adj[current][v] < minWeight) {
                    minWeight = adj[current][v];
                    nearest = v;
                }
            }
            
            // If no valid next vertex found, circuit is impossible
            if (nearest == -1) {
                return vector<int>(); // Return empty path to indicate failure
            }
            
            // Add nearest vertex to path and update current position
            path.push_back(nearest);
            unvisited.erase(nearest);
            current = nearest;
        }
        
        // Check if we can return to start
        if (adj[current][start] == 0) {
            return vector<int>(); // Return empty path if can't complete circuit
        }
        
        // Add start vertex to complete the circuit
        path.push_back(start);
        return path;
    }

    // Calculate total circuit weight
    int calculateCircuitWeight(const vector<int>& circuit) {
        if (circuit.empty()) return -1;
        
        int weight = 0;
        for (size_t i = 0; i < circuit.size() - 1; i++) {
            weight += adj[circuit[i]][circuit[i + 1]];
        }
        return weight;
    }

    // Utility function to print the circuit
    void printCircuit(const vector<int>& circuit) {
        if (circuit.empty()) {
            cout << "No Hamiltonian circuit exists!" << endl;
            return;
        }
        
        cout << "Hamiltonian Circuit: ";
        for (size_t i = 0; i < circuit.size(); i++) {
            cout << circuit[i];
            if (i < circuit.size() - 1) cout << " -> ";
        }
        cout << endl;
        
        cout << "Total Circuit Weight: " << calculateCircuitWeight(circuit) << endl;
    }
};

// Test function to demonstrate the algorithm
void testCase1() {
    // Create graph from Case Study 1 in your paper
    Graph g(4);  // Vertices: A(0), B(1), C(2), D(3)
    
    // Add edges with weights from your example
    g.addEdge(0, 3, 1);  // A-D
    g.addEdge(3, 2, 8);  // D-C
    g.addEdge(2, 1, 13); // C-B
    g.addEdge(1, 0, 4);  // B-A
    
    cout << "Test Case 1 (Small Graph Example):" << endl;
    vector<int> circuit = g.findHamiltonianCircuit(0); // Start from A (vertex 0)
    g.printCircuit(circuit);
}

void testCase2() {
    // Create graph from Case Study 2 (Travel Network)
    Graph g(5);  // Vertices: Seattle(0), LA(1), Chicago(2), Atlanta(3), Dallas(4)
    
    // Add edges with weights from your example
    g.addEdge(0, 1, 70);  // Seattle-LA
    g.addEdge(1, 2, 100); // LA-Chicago
    g.addEdge(2, 3, 75);  // Chicago-Atlanta
    g.addEdge(3, 4, 85);  // Atlanta-Dallas
    g.addEdge(4, 0, 120); // Dallas-Seattle
    
    cout << "\nTest Case 2 (Travel Network):" << endl;
    vector<int> circuit = g.findHamiltonianCircuit(0); // Start from Seattle
    g.printCircuit(circuit);
}

int main() {
    testCase1();
    testCase2();
    return 0;
}