abc = input("").split(" ")
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])
n = 0

if b >= c : n = -1
else : n = a // (c-b) + 1

print(n)
