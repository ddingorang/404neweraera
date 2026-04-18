n = int(input())
members=[]
for _ in range(n) :
    age, name = input('').split(' ')
    members.append((int(age), name))

members.sort(key=lambda x : x[0])
for e in members:
    print(str(e[0]) + ' ' + e[1])