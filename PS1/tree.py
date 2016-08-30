#!/usr/bin/python3

#Config
DEBUG = False
DAY   = 0
#N = "4" # sample 1
#tis = "2 3 4 3" # sample 1
#solution = 7

#N = "6" # sample 2
#tis = "39 38 9 35 39 20" #sample 2
#solution = 42

#  read Input lines
# === sample input ===
# 4
# 2 3 4 3
# ====================
#  read line one, single integer N (# of seedlings)
#  read line two, N integers ti (number of days for the tree to grow)
N = input("Input the number of seedlings: ")
tis = input("Input the number of days for each seedling: ")


#Farmer Jon has recently bought nn tree seedlings that he wants to plant in his
#yard. It takes 1 day for Jon to plant a seedling, and for each tree Jon knows
#exactly in how many days after planting it grows to full maturity. Jon would
#also like to throw a party for his farmer friends, but in order to impress them
#he would like to organize the party only after all the trees have grown. More
#precisely, the party can be organized at earliest on the next day after the
#last tree has grown up.

#Help Jon to find out when is the earliest day when the party can take place.
#Jon can choose the order of planting the trees as he likes, so he wants to
#plant the trees in such a way that the party will be as soon as possible.

### Input ###
# The input consists of two lines. The first line contains a single integer
# N (1 <= N <= 100,000) denoting the number of seedlings. Then a line with N integers
# ti follows (1 <= ti <= 1,000,000), where ti denotes the number of days it takes for
# the ith tree to grow.

# Output
# Your program should output exactly one line containing one integer, denoting
# the earliest day when the party can be organized.
# The days are numbered 1,2,3,... beginning from the current moment.

class Seedling:
    def __init__(self, maturity):
        self.maturity = int(maturity)

    def mature(self):
        if self.maturity < -1:
            return False

        self.maturity -= 1
        if self.maturity < 0:
            return True
        return False

# begin program
tiarray = tis.split()
tiarray.sort()
tiarray.reverse()
numberofseeds = int(N)
# TODO check if valid input

if DEBUG:
    print("-> Calculating with # of seedlings: " + str(N))
    print("-> Days for each seedling: " + str(tiarray))

# Assuming input is valid for now
seedlings = []
finished = 0
# planting loop
for maturity in tiarray:
    DAY += 1
    # maturing already planted seedlings loop
    for seedling in seedlings:
        if seedling.mature():
            finished += 1

    seedlings.append(Seedling(maturity))

# all seeds have been planted, wait until the trees mature
while finished < numberofseeds:
    # maturing already planted seedlings loop
    DAY += 1
    for seedling in seedlings:
        if seedling.mature():
            finished += 1
print(DAY)