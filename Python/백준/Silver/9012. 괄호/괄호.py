n = int(input(""))
q = []
result = []

for i in range(n) :
    vps = str(input(""))
    for c in vps :
        if c == '(' :
            q.append(0)
        elif c == ')' :
            if not q :
                q.append(0)
                break
            elif q : q.pop()
    if q : result.append('NO')
    else : result.append('YES')
    q.clear()

for element in result :
    print(element)
