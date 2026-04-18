n = input("")
m = [0]*len(n)

for i in range(len(n)) :
    m[i] = int(n[i])
m.sort(reverse = 1)
for element in m :
    print(element, end='')