n = input("")
intn = int(n)
for i in range(int(n)) :
    stri = str(i)
    num = [int(stri[k]) for k in range(len(stri))]

    if i + sum(num) == intn:
        print(i)
        break
    if i == intn-1 : print(0)