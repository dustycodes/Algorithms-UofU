#/usr/env python


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
        for u in range(number_of_nodes):
            dist[u] = float("inf")
            prev[u] = None
        dist[s] = 0

        # Read in edges
        E = []
        m = 0
        while m < number_of_edges:
            # edge from u to v with weight of w
            u, v, w = map(int, raw_input().split())
            E.append(Edge(u, v, w))
            m += 1

        for r in range(number_of_nodes-1):
            stop = True
            for edge in E:
                if dist[edge.v] > dist[edge.u] + edge.w:
                    dist[edge.v] = dist[edge.u] + edge.w
                    prev[edge.v] = edge.u
                    stop = False
            if stop:
                break

        # Read in Queries
        q = 0
        Q = []
        while q < number_of_queries:
            query = int(raw_input())
            Q.append(query)
            q += 1

        for query in Q:
            if query == s:
                print("0")
            elif prev[query] == None:
                print("Impossible")
            else:
                print(dist[query])
        print("")