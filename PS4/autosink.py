#/usr/env python

visit_number = 1
linearized_cities = []
current_cost = []
sources = []


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

    def __init__(self, from_city, to_city):
        self.from_city = from_city
        self.to_city = to_city


def linearize(cities):
    global linearized_cities
    while len(cities) != 0:
        for city in cities:
            if len(city.routes_in) == 0:
                cities.remove(city)

                for sub_city in city.routes_to:
                    sub_city.routes_in.remove(city)

                linearized_cities.append(city)

def dfs(trip):
    global linearized_cities, current_cost
    origin = trip.from_city
    destination = trip.to_city

    if origin == destination:
        print("0")
        return

    current_cost = []
    for city in linearized_cities:
        city.visited = False

    index = linearized_cities.index(origin)
    for city in linearized_cities[index:len(linearized_cities)]:
        if city.visited is False:
            cost = explore(linearized_cities, origin, origin, destination)

    if len(current_cost) > 0:
        minimum = min(current_cost)
        if minimum != 0:
            print(minimum)
            return

    print("NO")

def explore(cities, origin, current, destination):
    global linearized_cities, current_cost

    if current == destination:
        return current.toll

    current.visited = True

    cost = 0

    for sub_city in current.routes_to:
        if sub_city.visited is False:
            c = explore(cities, origin, sub_city, destination)
            if current == origin and c > 0:
                current_cost.append(c)
            elif c > 0:
                cost = current.toll + c
                break

    return cost


def main():
    global linearized_cities, current_cost, list_of_cities
    cities = {}
    number_of_cities = int(input())
    n = 0
    while n < number_of_cities:
        line = input()
        s = line.split()
        name = s[0]
        toll = int(s[1])
        cities[name] = City(name, toll)
        n += 1

    number_of_highways = int(input())
    h = 0
    while h < number_of_highways:
        line = input()
        s = line.split()
        from_city_name = s[0]
        to_city_name = s[1]

        cities[from_city_name].routes_to.append(cities[to_city_name])
        cities[to_city_name].routes_in.append(cities[from_city_name])

        h += 1

    trips = []
    number_of_trips = int(input())
    t = 0
    while t < number_of_trips:
        line = input()
        s = line.split()
        from_city_name = s[0]
        to_city_name = s[1]

        trips.append(Trip(cities[from_city_name], cities[to_city_name]))

        t += 1

    list_of_cities = list(cities.values())
    linearize(list_of_cities)

    for trip in trips:
        dfs(trip)


if __name__ == "__main__":
    main()
