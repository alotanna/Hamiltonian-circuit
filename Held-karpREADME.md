Held-Karp Algorithm Implementation
This Python implementation solves the Traveling Salesman Problem (TSP) using the Held-Karp algorithm, demonstrating a solution for finding a Hamiltonian circuit in a complete graph.
Requirements

No additional packages required (uses only standard libraries)

Installation

Clone or download the repository containing held_karp.py
No additional installation steps required

Usage
Running the Example
The simplest way to run the program is to execute it directly after you have navigated to the folder where the program is stored:

python3 Held-Karp.py
OR

python Held-Karp.py

This will run the example case with a 4x4 distance matrix and output both the minimum cost and the path taken.

Input Format
The distance matrix should be:

A square matrix where each entry [i][j] represents the distance from city i to city j
Symmetric (distance from A to B equals distance from B to A)
Have zeros on the diagonal (distance from a city to itself)
All distances should be non-negative integers

Output Format
The program returns:

The minimum cost of the complete tour
The path taken (sequence of cities visited)