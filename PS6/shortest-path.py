#/usr/env python


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.u = from_node
        self.v = to_node
        self.w = weight


class PriorityQueue:
    def __init__(self, num, source):
        self.m = {}
        for i in range(0, num):
            self.m[i] = float("inf")

        self.q = self.m.keys()
        self.q.remove(source)
        self.m[source] = 0
        self.q.insert(0, source)

    def is_empty(self):
        if len(self.q) > 0:
            return False
        return True

    def insert_or_change(self, v, w):
        self.m[v] = w
        try:
            self.q.remove(v)
        except ValueError:
            pass
        i = 0
        for itm in self.q:
            if self.m[itm] > self.m[v]:
                self.q.insert(i, v)
                return
        self.q.append(v)

    def delete_min(self):
        return self.m[self.q.pop()]


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
        pq = PriorityQueue(number_of_nodes,s)
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

        while pq.is_empty() is False:
            u = pq.delete_min()
            for edge in E:
                if dist[edge.v] > dist[edge.u] + edge.w:
                    dist[edge.v] = dist[edge.u] + edge.w
                    prev[edge.v] = edge.u
                    pq.insert_or_change(v, dist[edge.v])

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