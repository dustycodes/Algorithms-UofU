#!/usr/bin/python3
from array import *

compares = 0

def addCompare():
    global compares
    compares += 1
    return True

def insertionSort(alist, element, arrayindex):
    global compares
    n = str(alist.index(element))
    for index in range(1,len(alist)):

        currentValue = alist[index]
        position = index
        while position>0 and (alist[position-1] < currentValue and addCompare()):
            alist[position] = alist[position-1]
            position = position  - 1

        alist[position] = currentValue
        if arrayindex >= 0 and alist[arrayindex] == element:
            print("Found " + str(element) + " ==> " + str(alist) + " w/ compares: " + str(compares) + " n is " + n)
            break


    if(arrayindex < 0):
        print("Fully sorted array: " + str(alist))
        print("Total Compares: " + str(compares))


original = [0,7,8,5,6,3,4,1,2]
#original = [0,1,2,3,4,5,6,7,8]
#original = [0,8,7,6,5,4,3,2,1]
sortedlist = list(original)
sortedlist.sort()
sortedlist.reverse()
print("SORTED LIST: " + str(sortedlist))
print("ORIGINAL LIST: " + str(original))

for i in range(0, len(sortedlist)):
    alist = list(original)
    compares = 0
    print("---- Searching for value " + str(sortedlist[i]) + " at index " + str(i) + " -----")
    insertionSort(alist, sortedlist[i], i)

compares = 0
alist = list(original)
insertionSort(alist, 0, -1)
