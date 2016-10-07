# /usr/env python
import heapq


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.u = from_node
        self.v = to_node
        self.w = weight


number_of_nodes, number_of_edges, number_of_queries, s = map(int, raw_input().split())
while True:

    dist = {}
    pq = []
    E = {}
    for u in range(number_of_nodes):
        dist[u] = float("inf")
        E[u] = []
    dist[s] = 0
    heapq.heappush(pq, (0, s))

    # Read in edges
    m = 0
    while m < number_of_edges:
        # edge from u to v with weight of w
        u, v, w = map(int, raw_input().split())
        E[u].append(Edge(u, v, w))
        m += 1

    while len(pq) > 0:
        u = heapq.heappop(pq)

        for edge in E[u[1]]:
            if dist[edge.v] > dist[edge.u] + edge.w:
                if (dist[edge.v], edge.v) in pq:
                    pq.remove((dist[edge.v], edge.v))
                dist[edge.v] = dist[edge.u] + edge.w
                heapq.heappush(pq, (dist[edge.v], edge.v))

    # Read in Queries
    q = 0
    while q < number_of_queries:
        query = int(raw_input())
        if query == s:
            print("0")
        elif dist[query] == float("inf"):
            print("Impossible")
        else:
            print(dist[query])
        q += 1

    number_of_nodes, number_of_edges, number_of_queries, s = map(int, raw_input().split())

    if number_of_nodes < 1:
        break

    print("")
