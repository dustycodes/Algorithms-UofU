#!/usr/env python2

import heapq


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.u = from_node
        self.v = to_node
        self.w = weight


class PrioritySet(object):
    def __init__(self):
        self.heap = []

    def insert_or_change(self, node, priority):
        if node not in self.heap:
            heapq.heappush(self.heap, (priority, node))

    def delete_min(self):
        pri, d = heapq.heappop(self.heap)
        return d

    def is_empty(self):
        if len(self.heap) > 0:
            return False
        return True


while True:
    inp = raw_input()

    if inp == "0 0 0 0":
        break

    arr = inp.split()

    # Begin test
    if len(arr) == 4:
        number_of_nodes, number_of_edges, number_of_queries, s = map(int, arr)

        dist = {}
        prev = {}
        pq = PrioritySet()
        for u in range(number_of_nodes):
            pq.insert_or_change(u, 1002)
            dist[u] = float("inf")
            prev[u] = None
        pq.insert_or_change(s, 0)
        dist[s] = 0

        # Read in edges
        E = []
        m = 0
        while m < number_of_edges:
            # edge from u to v with weight of w
            u, v, w = map(int, raw_input().split())
            E.append(Edge(u, v, w))
            m += 1

        while pq.is_empty() is False:
            u = pq.delete_min()
            changed = False
            for edge in E:
                if dist[edge.v] > dist[edge.u] + edge.w:
                    dist[edge.v] = dist[edge.u] + edge.w
                    prev[edge.v] = edge.u
                    pq.insert_or_change(edge.v, dist[edge.v])
                    changed = True

            if changed is False:
                break

        # Read in Queries
        q = 0
        while q < number_of_queries:
            query = int(raw_input())
            if query == s:
                print("0")
            elif prev[query] is None:
                print("Impossible")
            else:
                print(dist[query])
            q += 1

        print("")
