yaksu = []
a, b = map(int, input("").split())

for i in range(1, int(a/2)+1) :
    if a % i == 0 : yaksu.append(i)
yaksu.append(a)

try :
    print(yaksu[b-1])
except IndexError as exception :
    print(0)