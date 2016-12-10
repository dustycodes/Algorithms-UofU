#!/usr/bin/env python
from collections import namedtuple

Group = namedtuple("Group", ["v", "l"])

n = int(input())

C = [[0 for x in range(n)] for y in range(n)]
g = {}
p = {}

for u in range(n):
    line = input().split()
    for v in range(len(line)):
        if u != v:
            w = int(line[v])
            C[u][v] = w

for c in range(1,n):
    g[c] = Group(l=[], v=C[c][0])

for k in g.keys():
    



