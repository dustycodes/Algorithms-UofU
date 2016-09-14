import math

class Star:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.galaxy = None


class Galaxy:

    def __init__(self, diameter):
        self.diameter = diameter
        self.stars = []


    def fits(self, check_star):
        if len(self.stars) == 0:
            return True

        for star in self.stars:
            if (self.is_in_diameter(check_star.x, star.x, check_star.y, star.y)):
                return True

        return False


    def is_in_diameter(self, x1, x2, y1, y2):
        return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2) <= self.diameter)


    def add_star(self, new_star):
        if (self.fits(new_star)):
            new_star.galaxy = self
            self.stars.append(new_star)
            return True
        else:
            return False



it = 1
diameter, star_count = map(int, raw_input().split())
galaxies = []

x, y = map(int, raw_input().split())
new_star = Star(x, y)
g = Galaxy(diameter)
g.stars.append(new_star)
galaxies.append(g)

while it < star_count:
    x, y = map(int, raw_input().split())
    new_star = Star(x, y)
    added = False
    for galaxy in galaxies:
        if galaxy.add_star(new_star):
            added = True

    if added == False:
        g = Galaxy(diameter)
        g.stars.append(new_star)
        galaxies.append(g)

    it += 1
