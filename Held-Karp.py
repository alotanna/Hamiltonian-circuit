from itertools import combinations
from typing import List, Dict, Set, Tuple

def held_karp(distance_matrix: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Implements the Held-Karp algorithm to solve the Traveling Salesman Problem.
    
    Args:
        distance_matrix: A matrix where distance_matrix[i][j] represents the distance
                        between city i and city j
    
    Returns:
        A tuple containing:
        - The minimum cost of the TSP tour
        - The path taken (list of cities in order)
    """
    n = len(distance_matrix)
    if n <= 2:
        return 0, [0]
    
    # Create dictionaries to store costs and paths
    costs: Dict[Tuple[frozenset, int], int] = {}
    paths: Dict[Tuple[frozenset, int], List[int]] = {}
    
    # Initialize the base cases
    for k in range(1, n):
        costs[frozenset([k]), k] = distance_matrix[0][k]
        paths[frozenset([k]), k] = [0, k]
    
    # Iterate through all possible set sizes
    for size in range(2, n):
        for subset in combinations(range(1, n), size):
            subset_set = frozenset(subset)
            for k in subset:
                prev_subset = subset_set - {k}
                min_cost = float('inf')
                best_path = []
                
                for m in subset:
                    if m == k:
                        continue
                    cost = costs[prev_subset, m] + distance_matrix[m][k]
                    if cost < min_cost:
                        min_cost = cost
                        # Create new path by extending the path to m with k
                        best_path = paths[prev_subset, m].copy()
                        best_path.append(k)
                
                costs[subset_set, k] = min_cost
                paths[subset_set, k] = best_path
    
    # Calculate final minimum cost and path
    all_cities = frozenset(range(1, n))
    min_total_cost = float('inf')
    final_path = []
    
    for k in range(1, n):
        cost = costs[all_cities, k] + distance_matrix[k][0]
        if cost < min_total_cost:
            min_total_cost = cost
            final_path = paths[all_cities, k].copy()
            final_path.append(0)  # Return to starting city
    
    return min_total_cost, final_path
   
if __name__ == "__main__":
     # Example distance matrix
    distance_matrix = [
        [0, 20, 42, 35],
        [20, 0, 30, 34],
        [42, 30, 0, 12],
        [35, 34, 12, 0]
    ]
    
    min_cost, path = held_karp(distance_matrix)
    print(f"Minimum cost of TSP tour: {min_cost}")
    print(f"Path taken: {path}")
    print(f"This is a Hamiltonian circuit as it visits each vertex exactly once and returns to the start: {path}")
