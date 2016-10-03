#/usr/env python
import heapq


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.u = from_node
        self.v = to_node
        self.w = weight


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
        pq = []
        for u in range(number_of_nodes):
            dist[u] = float("inf")
            prev[u] = None
            heapq.heappush(pq, (float("inf"), u))
        dist[s] = 0
        heapq.heappush(pq, (0, s))

        # Read in edges
        E = []
        m = 0
        while m < number_of_edges:
            # edge from u to v with weight of w
            u, v, w = map(int, raw_input().split())
            E.append(Edge(u, v, w))
            m += 1

        while len(pq) > 0:
            u = heapq.heappop(pq)
            for edge in E:
                if dist[edge.v] > dist[edge.u] + edge.w:
                    dist[edge.v] = dist[edge.u] + edge.w
                    prev[edge.v] = edge.u
                    heapq.heappush(pq, (dist[v], v))

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