from itertools import combinations

a, b = map(int, input("").split())
cardlist = list(map(int, input("").split()))
sumlist = []

for element in combinations(cardlist, 3) :
    if sum(element) <= b : sumlist.append(sum(element))

print(max(sumlist))