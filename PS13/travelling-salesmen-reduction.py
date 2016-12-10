#!/usr/bin/env python
from heapq import *

# Return the Hamiltonian cycle with the smallest weight or report
# there is not solution.
def hamiltonian_cycle_optimization(graph, minimum, maximum):
    optimal_budget = maximum
    while True:
        if maximum < minimum:
            break
        budget = (minimum + maximum) // 2
        found, new_graph = hamiltonian_cycle_search(graph, budget)
        if found:
            graph = new_graph
            maximum = budget - 1
        else:
            minimum = budget + 1


# Return a Hamiltonian cycle with total weight at most budget or
# report there is no solution
def hamiltonian_cycle_search(graph, budget):
    if hamiltonian_cycle_decision(graph, budget) is False:
        return False, None
    else:
        # Foreach edge in G
        for u in range(len(G[0])):
            for v in range(len(G[0])):
                new_graph = graph
                new_graph[u][v] = None
                if hamiltonian_cycle_decision(graph, budget):
                    graph = new_graph

        return True, graph


# Is there a hamiltonian cycle with total weight at most budget?
def hamiltonian_cycle_decision(graph, budget):
    # TODO fix this crap
    n = range(len(graph[0]))
    u = 0
    start = 0
    weight = 0
    while True:
        for v in n:
            if v is not None:
                if budget < weight
                    weight += graph[u][v]
                    u = v

        if budget < weight:
            return False

        if u == start:
            return True




n = int(input())

G = [[0 for x in range(n)] for y in range(n)]
minimum_q = []
maximum_q = []

for i in range(n):
    line = input().split()
    for j in range(len(line)):
        heappush(minimum_q, int(line[j]))
        heappush(maximum_q, -1*int(line[j]))
        G[i][j] = int(line[j])

minimum = 0
maximum = 0
for f in range(n):
    minimum += heappop(minimum_q)
    maximum += -1*heappop(maximum_q)

hamiltonian_cycle_optimization(G, minimum, maximum)