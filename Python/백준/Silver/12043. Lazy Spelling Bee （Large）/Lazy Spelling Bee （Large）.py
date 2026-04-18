
t = int(input())
result = []
for _ in range(t):
    w = input()
    if len(w) == 1:
        result.append(1)
    else :
        possible = []
        for c in range(len(w)) :
            if c == 0:
                if w[0] == w[1] :
                    possible.append(1)
                else :
                    possible.append(2)
            elif c == len(w)-1:
                if w[-1] == w[-2] :
                    possible.append(1)
                else :
                    possible.append(2)
            else :
                l = set()
                l.add(w[c-1])
                l.add(w[c])
                l.add(w[c+1])
                possible.append(len(l))

        temp = 1
        for p in possible:
            temp *= p
            temp %= 1000000007
        result.append(temp)

for idx, e in enumerate(result):
    print(f'Case #{idx+1}: {e}')