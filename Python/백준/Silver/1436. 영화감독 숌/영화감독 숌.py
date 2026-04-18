i = 666
k = 0
n = int(input(""))
while 1 :
    str_i = str(i)
    for j in range(len(str(i))-2) :
        if str_i[j:j+3] == '666' :
            k += 1
            break
    if n == k :
        print(i)
        break
    i += 1