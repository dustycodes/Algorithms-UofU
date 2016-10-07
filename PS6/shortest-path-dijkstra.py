#/usr/env python
import heapq


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.u = from_node
        self.v = to_node
        self.w = weight


while True:

    number_of_nodes, number_of_edges, number_of_queries, s = map(int, raw_input().split())

    # Begin test
    if number_of_nodes > 0:

        dist = {}
        prev = {}
        pq = []
        pq_set = set()
        E = {}
        for u in range(number_of_nodes):
            dist[u] = 2002
            prev[u] = None
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
            if u[1] not in pq_set:
                pq_set.add(u[1])
                for edge in E[u[1]]:
                    if edge.v not in pq_set:
                        if dist[edge.v] > dist[edge.u] + edge.w:
                            dist[edge.v] = dist[edge.u] + edge.w
                            prev[edge.v] = edge.u
                            heapq.heappush(pq, (dist[edge.v], edge.v))

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
    else:
        break
