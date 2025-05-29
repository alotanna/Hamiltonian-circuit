from itertools import permutations

def is_valid_circuit(graph, path):
    """Check if the path forms a valid Hamiltonian circuit."""
    # Check connections between consecutive vertices
    for i in range(len(path)):
        next_vertex = path[(i + 1) % len(path)]
        if next_vertex not in graph[path[i]]:
            return False
    return True

def find_all_hamiltonian_circuits(graph):
    """
    Find all Hamiltonian circuits in the graph.
    
    Args:
    graph (dict): Adjacency list representation of the graph
    
    Returns:
    list: All Hamiltonian circuits found
    """
    vertices = list(graph.keys())
    n = len(vertices)
    circuits = []
    
    # Try all permutations of vertices
    for perm in permutations(vertices):
        # Skip permutations that don't start with first vertex to avoid duplicates
        if perm[0] != vertices[0]:
            continue
        
        # Check if the current permutation forms a valid Hamiltonian circuit
        if is_valid_circuit(graph, perm):
            circuits.append(list(perm))
    
    return circuits

# Example usage
def main():
    # Example graph represented as an adjacency list
    # Each vertex is a letter, and its value is a list of connected vertices
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    
    all_circuits = find_all_hamiltonian_circuits(graph)
    
    if all_circuits:
        print(f"Found {len(all_circuits)} Hamiltonian Circuits:")
        for circuit in all_circuits:
            # Complete the circuit by adding the start vertex at the end
            print(" -> ".join(circuit + [circuit[0]]))
    else:
        print("No Hamiltonian Circuits exist")

if __name__ == "__main__":
    main()