#/usr/env python

import copy


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class AdjacencyListNode:
    def __init__(self, name, toll):
        self.name = name
        self.toll = toll


class Trip:
    def __init__(self, from_name, to_name):
        self.from_name = from_name
        self.to_name = to_name


class AdjacencyGraph:
    def __init__(self, names_of_cities):
        self.stack = Stack()
        self.adjacency_map = {}
        self.distance_map = {}
        for name in names_of_cities:
            self.adjacency_map[name] = []
            self.distance_map[name] = []

    def add_edge(self, from_city, to_city):
        node = to_city
        self.adjacency_map[from_city.name].append(node)

    def topological_sort(self, name, visited, stack):
        visited[name] = True
        for node in self.adjacency_map[name]:
            if visited[node.name] is False:
                self.topological_sort(node.name, visited, stack)

        stack.push(name)

    def build(self):
        visited = {}
        for vertice in self.adjacency_map.keys():
            visited[vertice] = False

        for vertice in self.adjacency_map.keys():
            if visited[vertice] is False:
                self.topological_sort(vertice, visited, self.stack)

    def shortest_path(self, origin, destination):
        distance = {}
        edges = {}

        if len(self.distance_map[origin]) == 0:
            if destination == origin:
                print("0")
                return

            for vert in self.adjacency_map.keys():
                distance[vert] = float("inf")
                edges[vert] = float("inf")
            distance[origin] = 0
            edges[origin] = 0

            stack_copy = copy.deepcopy(self.stack)

            while stack_copy.is_empty() is False:
                name = stack_copy.pop()

                if distance[name] != float("inf"):
                    for node in self.adjacency_map[name]:
                        if distance[node.name] > (distance[name] + node.toll):
                            distance[node.name] = (distance[name] + node.toll)


            self.distance_map[origin] = distance

        if self.distance_map[origin][destination] == float("inf"):
            print("NO")
        else:
            print(self.distance_map[origin][destination])


def main():
    cities = {}
    number_of_cities = int(input())
    n = 0
    while n < number_of_cities:
        line = input()
        s = line.split()
        name = s[0]
        toll = int(s[1])
        cities[name] = AdjacencyListNode(name, toll)
        n += 1

    graph = AdjacencyGraph(cities.keys())

    number_of_highways = int(input())
    h = 0
    while h < number_of_highways:
        line = input()
        s = line.split()
        from_city_name = s[0]
        to_city_name = s[1]
        graph.add_edge(cities[from_city_name], cities[to_city_name])

        h += 1

    trips = []
    number_of_trips = int(input())
    t = 0
    while t < number_of_trips:
        line = input()
        s = line.split()
        from_city_name = s[0]
        to_city_name = s[1]

        trips.append(Trip(from_city_name, to_city_name))

        t += 1

    graph.build()

    for trip in trips:
        graph.shortest_path(trip.from_name, trip.to_name)


if __name__ == "__main__":
    main()
