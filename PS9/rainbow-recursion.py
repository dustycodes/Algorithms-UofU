#!/usr/bin/env python


def penalties(distances):
    cache = {}
    return compute_penalties(distances, 0, len(distances)-1, cache)


def compute_penalties(distances, source, destination, cache):
    tu = source,destination

    if tu in cache.keys():
        return cache[n]
    else:
        dist = distances[destination] - distances[source]
        cost = (400 - dist) ** 2

        x = destination
        while x > 0:
            next_cost = compute_penalties(distances, source+1, x, cache)
            cost = min(cost, next_cost)
            x -= 1

        cache[tu] = cost
        return cost


distances = {}
number_of_distances = int(input())

for i in range(number_of_distances + 1):
    element = int(input())
    distances[i] = element

answer = penalties(distances)
print(answer)