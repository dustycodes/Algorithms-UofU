#!/usr/bin/env python
from heapq import *

temp = input()
temp_arr = temp.split()
number_of_people = int(temp_arr[0])
time_until_close = int(temp_arr[1])

customers = {}

for i in range(number_of_people):
    temp = input()
    temp_arr = temp.split()
    money = int(temp_arr[0])
    time_until_leaving = int(temp_arr[1])
    if time_until_leaving not in customers.keys():
        customers[time_until_leaving] = []
    customers[time_until_leaving].append(money)

potentials = []
max_money = 0
for i in reversed(range(time_until_close)):
    if i in customers.keys():
        for m in customers[i]:
            heappush(potentials, m*-1)
        if len(potentials):
            max_money += heappop(potentials)

max_money *= -1
print(max_money)