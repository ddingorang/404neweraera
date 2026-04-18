from collections import defaultdict
n, m = map(int, input("").split(" "))
dbj = defaultdict(int)
results = []

for _ in range(n) :
    name1 = input("")
    dbj[name1] += 1

for _ in range(m) :
    name2 = input("")
    dbj[name2] += 1
    if dbj[name2] == 2 :
        results.append(name2)

print(len(results))
results.sort()
for element in results :
    print(element)