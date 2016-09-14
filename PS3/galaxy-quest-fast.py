# Galaxy Quest
# NASA recently confirmed the discovery of parallel universes (PUs) occupying
# alternate dimensions. These universes are quite different from our own
# universe, in the following ways:
#
# Each PU is a two-dimensional square that stretches 109109 light years from
# left to right and from top to bottom.
# Each PU has a galactic diameter of dd light years.
# Each star is exactly xx light years from its universe’s left edge and yy
# light years from its universe’s bottom edge, where xx and yy are non-negative
# integers.
# Stars are clustered into galaxies. Each galaxy consists of one or more stars.
# Each star is at most dd light years from every other star in its galaxy.
# Any two stars from different galaxies are more than dd light years apart.
# For each PU, NASA has obtained all of its stellar coordinates and has
# measured its value of dd.
#
# Given the description of a PU, NASA would like to be able to determine
# whether that PU has a galaxy that contains more than half of the stars in
# the PU. NASA has turned to you.
#
# Input
# The input describes a single PU.
#
# The first line of the input contains the PU’s galactic
# diameter dd (1<=d<=1061<=d<=106) and star count kk (1<=k<=1061<=k<=106).
#
# There are exactly kk more lines. Each line contains
# the xx (0<=x<=1090<=x<=109) and yy (0<=y<=1090<=y<=109) coordinates
# of a star in the PU. No two of these lines are identical, as a black hole
# would result!
#
# Output
# If the PU described by the input has a galaxy containing more than half of
# the stars, display the number of stars in that galaxy. Otherwise, display NO.

# Input:
# 10 4
# 45 46
# 90 47
# 45 54
# 90 43
# Output:
# NO

# Input:
# 20 7
# 1 1
# 100 100
# 1 3
# 101 101
# 3 1
# 102 102
# 3 3
# Output:
# 4

class Star:

    def __init__(self, x_c, y_c, diameter):
        self.x = x_c
        self.y = y_c
        self.diameter = diameter ** 2
        self.close_stars = 1

    def close_enough(self, star):
        distance = (self.x - star.x) ** 2 + (self.y - star.y) ** 2
        if distance <= self.diameter:
            return True
        else:
            return False


def find_majority(A):
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]
    else:
        half = len(A) / 2
        left = find_majority(A[0:half])
        right = find_majority(A[half+1:len(A)])
        if left is None and right is None:
            return None
        elif right is None:
            nombre = 0
            for s in A:
                if s.close_enough(left):
                    nombre += 1
            if nombre > half:
                left.close_stars = nombre
                return left
            else:
                return None
        elif left is None:
            nombre = 0
            for s in A:
                if s.close_enough(right):
                    nombre += 1
            if nombre > half:
                right.close_stars = nombre
                return right
            else:
                return None
        else:
            nombreL = 0
            nombreR = 0
            for s in A:
                if s.close_enough(left):
                    nombreL += 1
                if s.close_enough(right):
                    nombreR += 1
            if nombreL > half:
                left.close_stars = nombreL
                return left
            if nombreR > half:
                right.close_stars = nombreR
                return right
            else:
                return None


stars = []
diameter, star_count = map(int, raw_input().split())

# read in stuff
while len(stars) < star_count:
    x, y = map(int, raw_input().split())
    new_star = Star(x, y, diameter)
    stars.append(new_star)

largest_galaxy = find_majority(stars)

if largest_galaxy is None:
    print("NO")
elif star_count == 1:
    print("1")
else:
    print(largest_galaxy.close_stars)
