from collections import defaultdict
n = int(input(""))
cards = defaultdict(int)
having = list(input("").split(" "))

for element in having :
    cards[element] += 1

m = int(input(""))
enquire = list(input("").split(" "))

for element in enquire :
    print(cards[element], end=" ")