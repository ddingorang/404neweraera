m, n = map(int, input("").split(" "))
prlist = []
flag = 0

for i in range(m, n+1) :
    if i == 1 : continue # 1은 소수가 아님
    elif i % 2 == 0 and i != 2 : continue # 2를 제외한 짝수는 소수가 아님
    for j in range(3, int(i**0.5) + 1, 2) :
        if i % j == 0 : 
            flag = 1
            break
    if flag == 0 : prlist.append(i)
    flag = 0

for element in prlist :
    print(element)