#!/usr/bin/env python


def rtsp(dest, remaining_set, g):
    ans = (float('inf'), None)
    if remaining_set:
        for loc in remaining_set:
            val = (g[loc][dest] + rtsp(loc, remaining_set - set([loc]), g)[0], loc)
            if val[0] < ans[0]:
                ans = val
    else:
        ans = (g[0][dest], 0)
    return ans


def tsp(g):
    best_tour = []
    current = 0
    key_set = set(range(1, len(g)))
    while True:
        cost, location = rtsp(current, key_set, g)
        if location == 0:
            break
        key_set -= set([location])
        best_tour.append(location)
        current = location

    best_tour = tuple(reversed(best_tour))
    last = 0
    tour_cost = 0
    for current in best_tour:
        tour_cost += g[last][current]
        last = current
    tour_cost += g[last][0]

    return best_tour, tour_cost


n = int(input())

C = [[0 for x in range(n)] for y in range(n)]

for u in range(n):
    line = input().split()
    for v in range(len(line)):
        if u != v:
            w = int(line[v])
            C[u][v] = w

f, cost = tsp(C)
print(cost)