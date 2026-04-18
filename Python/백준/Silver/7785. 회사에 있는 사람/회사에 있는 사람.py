from collections import defaultdict
n = int(input(""))
name = defaultdict(int)

for _ in range(n) :
    s = list(input("").split(" "))
    if s[1] == 'enter' :
        name[s[0]] += 1
    elif s[1] == 'leave' :
        name[s[0]] -= 1
        if name[s[0]] == 0 :
            del name[s[0]]

namesorted = sorted(name, reverse=True)
for element in namesorted :
    print(element)