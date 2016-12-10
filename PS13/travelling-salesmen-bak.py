#!/usr/bin/env python
from heapq import *
import copy

number_of_nodes = 0

class DisjointSet:
    def __init__(self, list_of_nodes):
        self.n = len(list_of_nodes)
        self.ds = {}
        for i in list_of_nodes:
            s = set()
            s.add(i)
            self.ds[i] = s

    def add(self, node):
        s = set()
        s.add(node)
        self.ds[node] = s

    def find(self, x):
        return max(self.ds[x])

    def union(self, x, y):
        self.ds[x] = self.ds[x].union(self.ds[y])
        self.ds[y] = self.ds[x]

    def keys(self):
        return self.ds.keys()


def mst(graph, parent):
    minimum_q = []
    n = len(graph.keys())

    if n == 0:
        return 0

    ds = DisjointSet(graph.keys())
    ds.add(parent)

    for k in graph.keys():
        for item in graph[k]:
            if item[1][0] in ds.keys() and item[1][1] in ds.keys():
                heappush(minimum_q, item)

    total = 0

    while len(minimum_q) > 0:
        w, uv = heappop(minimum_q)
        u = uv[0]
        v = uv[1]

        if ds.find(u) != ds.find(v):
            total += w
            ds.union(u, v)

    return total


def minimize(graph):
    best_so_far = float('inf')

    for key in graph.keys():
        g = copy.deepcopy(graph)
        val = optimize(key, g, best_so_far, key)
        if val < best_so_far:
            best_so_far = val

    print(best_so_far)


def optimize(p, graph, best_so_far, start):

    if p not in graph.keys():
        return 0

    minimum_q = graph[p]
    graph.pop(p)

    #w, uv = heappop(minimum_q)
    #heappush(minimum_q, (w, (uv[0], uv[1])))
    lower_bound = mst(graph, start)# + w

    if lower_bound < best_so_far:
        l_best = float('inf')
        while len(minimum_q) > 0:
            w, uv = heappop(minimum_q)
            u = uv[0]
            v = uv[1]
            cost = w + optimize(v, graph, best_so_far, start)
            if cost < l_best:
                l_best = cost
        return l_best
    return float('inf')


n = int(input())

G = {}

for u in range(n):
    line = input().split()
    minimum_q = []
    for v in range(len(line)):
        if u != v:
            w = int(line[v])
            heappush(minimum_q, (w, (u, v)))

    G[u] = minimum_q

minimize(G)