import random

arr = []

for c in range(1, 46):
    arr.append(c)

for i in range(1000):
    rnd = int(random.random()*45)
    a = arr[0]
    b = arr[rnd]
    arr[0] = b
    arr[rnd] = a

print(arr)