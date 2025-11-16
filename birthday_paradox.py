import math

arr = []

for i in range(0, 23):
    arr.append((365-i)/365)

prob = 1

for i in arr:
    prob = prob * i

print(prob)