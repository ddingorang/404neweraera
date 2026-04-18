a = int(input(""))
prlist = []

for i in range(2, a+1) :
    while a % i == 0 :
        prlist.append(i)
        a /= i

for element in prlist :
    print(element)