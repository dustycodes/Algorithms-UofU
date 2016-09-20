#/usr/env python

visit_number = 1
linearized_cities = []
current_cost = 0

class City:

    def __init__(self, name, toll):
        self.name = name
        self.toll = toll
        self.routes_to = []
        self.routes_in = []
        self.visited = False
        self.post_number = -1
        self.pre_number = -1

class Trip:

    def __init__(self, from_index, to_index):
        self.from_index = from_index
        self.to_index = to_index


def previsit(city):
    global visit_number
    city.pre_number = visit_number
    visit_number += 1


def postvisit(city):
    global visit_number, linearized_cities
    city.post_number = visit_number
    linearized_cities.insert(0, city)
    visit_number += 1


def explore(cities, v):
    v.visited = True
    previsit(v)

    for ind in v.routes_to:
        if cities[ind].visited is False:
            explore(cities, cities[ind])

    postvisit(v)


def dfs(cities):
    for city_index in cities:
        cities[city_index].visited = False

    for city_index in cities:
        if cities[city_index].visited is False:
            explore(cities, cities[city_index])

def main():
    global linearized_cities, current_cost
    cities = {}
    city_names = {}
    number_of_cities = int(input())
    n = 0
    while n < number_of_cities:
        line = input()
        s = line.split()
        name = s[0]
        toll = int(s[1])
        cities[n] = City(name, toll)
        city_names[name] = n
        n += 1

    adj_matrix = [[None] * number_of_cities for x in range(number_of_cities)]
    number_of_highways = int(input())
    h = 0
    while h < number_of_highways:
        line = input()
        s = line.split()
        from_city = s[0]
        to_city = s[1]

        from_index = city_names[from_city]
        to_index = city_names[to_city]
        cities[from_index].routes_to.append(to_index)
        cities[to_index].routes_in.append(from_index)
        adj_matrix[from_index][to_index] = cities[to_index].toll

        h += 1

    trips = []
    number_of_trips = int(input())
    t = 0
    while t < number_of_trips:
        line = input()
        s = line.split()
        from_city = s[0]
        to_city = s[1]

        from_index = city_names[from_city]
        to_index = city_names[to_city]
        trips.append(Trip(from_index, to_index))

        t += 1

    dfs(cities)

    for trip in trips:
        f = cities[trip.from_index]
        t = cities[trip.to_index]
        from_index = linearized_cities.index(f)
        to_index = linearized_cities.index(t)
        cost = 0
        found = False

        if from_index == to_index:
            print("0")
            continue
        else:
            leng = len(linearized_cities)
            while from_index < leng and len(f.routes_to) != 0:
                cost += linearized_cities[from_index].toll

                if from_index == to_index and current_cost == 0 or current_cost > cost:
                    current_cost = cost
                    found = True

                f = cities[from_index]
                from_index += 1

        if found is True:
            print(current_cost)



if __name__ == "__main__":
    main()
