#!/usr/bin/env python


def penalties(ds):
    return compute_penalties(ds, len(ds)-1)


def compute_penalties(distances, i):

    cost = (400 - distances[i]) ** 2
    min_cost = cost
    n = 1
    while n < i:
        dist = distances[i] - distances[n]
        cost = (400 - dist) ** 2
        cost = cost + compute_penalties(distances, n, cache)
        min_cost = min(min_cost, cost)
        n += 1

    return min_cost


d = {}
number_of_distances = int(input())

for r in range(number_of_distances + 1):
    element = int(input())
    d[r] = element

answer = penalties(d)
print(answer)
