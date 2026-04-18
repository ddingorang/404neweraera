a = input("").split(" ")
total = int(a[0])
prize = int(a[1])

b = input("").split(" ")
b = list(map(int, b))
b.sort(reverse=True)

print(b[prize-1])