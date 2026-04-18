a = input("")
time = 0

for i in range(len(a)) :
    time += 2
    b = ord(a[i]) - 65
    if b >= 18 : b -= 1
    if b == 24 : b -= 1
    time += (b//3 + 1)
    

print(time)