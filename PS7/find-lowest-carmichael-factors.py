import math
count = 0

for i in range(2, 561):
    if math.gcd(i, 651) == 1:
        count += 1

print(count)