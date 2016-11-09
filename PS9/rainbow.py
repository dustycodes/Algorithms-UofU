#!/usr/bin/env python


def penalties(ds):
    cache = {0: 0}
    return compute_penalties(ds, len(ds)-1, cache)


def compute_penalties(distances, n, cache):
    if n in cache.keys():
        return cache[n]

    cost = (400 - distances[n]) ** 2
    min_cost = cost
    #i = n - 1
    i = 1
    #while i > 0:
    while i < n:
        dist = distances[n] - distances[i]
        cost = (400 - dist) ** 2
        cost = cost + compute_penalties(distances, i, cache)
        min_cost = min(min_cost, cost)
        #i -= 1
        i += 1

    cache[n] = min_cost
    return min_cost


d = {}
number_of_distances = int(input())

for r in range(number_of_distances + 1):
    element = int(input())
    d[r] = element

answer = penalties(d)
print(answer)
