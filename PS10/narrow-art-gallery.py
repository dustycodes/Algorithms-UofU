#!/usr/bin/env python


def max_value(g, k):
    return compute_max_value(g, {}, {}, {}, 0, -1, k)


def compute_max_value(g, cachen, cache0, cache1, r, unclosed_room, k):

    if unclosed_room == -1:
        if (r,k) in cachen.keys():
            return cachen[r,k]
    elif unclosed_room == 0:
        if (r,k) in cache0.keys():
            return cache0[r,k]
    elif unclosed_room == 1:
        if (r,k) in cache1.keys():
            return cache1[r,k]

    if r == len(g):
        return 0
    else:
        if k == len(g) - r:
            left = 0
            right = 0
            if unclosed_room == 0:
                left = g[r][0] + compute_max_value(g, cachen, cache0, cache1, r+1, 0, k-1)
            elif unclosed_room == 1:
                right = g[r][1] + compute_max_value(g, cachen, cache0, cache1, r+1, 1, k-1)
            else:
                left = g[r][0] + compute_max_value(g, cachen, cache0, cache1, r+1, 0, k-1)
                right = g[r][1] + compute_max_value(g, cachen, cache0, cache1, r + 1, 1, k - 1)
            m = max(right, left)
            if unclosed_room == -1:
                cachen[r, k] = m
            elif unclosed_room == 0:
                cache0[r, k] = m
            elif unclosed_room == 1:
                cache1[r, k] = m
            return m
        else:
            middle = g[r][0] + g[r][1] + compute_max_value(g, cachen, cache0, cache1, r+1, -1, k)
            left = 0
            right = 0
            if k > 0:
                if unclosed_room == 0:
                    left = g[r][0] + compute_max_value(g, cachen, cache0, cache1, r+1, 0, k-1)
                elif unclosed_room == 1:
                    right = g[r][1] + compute_max_value(g, cachen, cache0, cache1, r+1, 1, k-1)
                else:
                    left = g[r][0] + compute_max_value(g, cachen, cache0, cache1, r+1, 0, k-1)
                    right = g[r][1] + compute_max_value(g, cachen, cache0, cache1, r+1, 1, k-1)
            m = max(right, left, middle)
            if unclosed_room == -1:
                cachen[r, k] = m
            elif unclosed_room == 0:
                cache0[r, k] = m
            elif unclosed_room == 1:
                cache1[r, k] = m
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