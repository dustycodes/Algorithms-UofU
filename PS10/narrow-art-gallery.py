#!/usr/bin/env python


def max_value(g, k):
    cache = {len(g):0}
    return compute_max_value(g, cache, 0, -1, k)


def compute_max_value(g, cache, r, unclosed_room, k):
    if r == len(g):
        return 0
    #elif (r, k) in cache.keys():
    #    return cache[r, k]
    else:
        if k == len(g) - r:
            left = 0
            right = 0
            if unclosed_room == 0:
                left = g[r][0] + compute_max_value(g, cache, r+1, 0, k-1)
            elif unclosed_room == 1:
                right = g[r][1] + compute_max_value(g, cache, r+1, 1, k-1)
            else:
                left = g[r][0] + compute_max_value(g, cache, r+1, 0, k-1)
                right = g[r][1] + compute_max_value(g, cache, r + 1, 1, k - 1)
            m = max(right, left)
            #cache[r, k] = m
            return m
        else:
            middle = g[r][0] + g[r][1] + compute_max_value(g, cache, r+1, -1, k)
            left = 0
            right = 0
            if unclosed_room == 0:
                left = g[r][0] + compute_max_value(g, cache, r+1, 0, k-1)
            elif unclosed_room == 1:
                right = g[r][1] + compute_max_value(g, cache, r+1, 1, k-1)
            else:
                left = g[r][0] + compute_max_value(g, cache, r+1, 0, k-1)
                right = g[r][1] + compute_max_value(g, cache, r+1, 1, k-1)
            m = max(right, left, middle)
            #cache[r, k] = m
            return m


N, k = input().split()
N = int(N)
k = int(k)

gallery = [[0 for x in range(2)] for y in range(N)]

for i in range(N):
    f, s = input().split()
    f = int(f)
    s = int(s)
    gallery[i][0] = f
    gallery[i][1] = s

s = input()

m = max_value(gallery, k)
print(m)