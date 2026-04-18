import math

a, b, c = list(tuple(map(int, input("").split(" "))))
days = math.ceil((c-a) / (a-b)) + 1
print(days)