n, b = input("").split()
num = []

for i in range(len(n)) :
    try :
        num.append(int(n[i]))
    except ValueError as exception :
        num.append(n[i])

sum = 0
for i in range(len(n)) :
    if type(num[i]) == str:
        sum += (ord(n[i])-55)*(int(b)**(len(n)-1-i))
    else :
        sum += num[i]*(int(b)**(len(n)-1-i))

print(sum)