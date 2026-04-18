testnum = int(input(""))
b = [0] * testnum
result = [''] * testnum
repnum = 0

for i in range(testnum) :
    b = input("").split()
    repnum = int(b[0])
    for j in range(len(b[1])) :
        result[i] += repnum*b[1][j]

for element in result :
    print(element)

