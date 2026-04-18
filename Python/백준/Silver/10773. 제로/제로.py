
n = int(input(""))
q = []

for i in range(n) :
    k = int(input(""))
    if k == 0 : q.pop()
    else : q.append(k)

print(sum(q))