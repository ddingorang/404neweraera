testnumber = int(input(""))
quiz = [0]*testnumber
points = [0]*testnumber
temp = 0
for i in range(testnumber) :
    quiz[i] = input("")

for j in range(testnumber) : 
    for k in range(len(quiz[j])) :
        if quiz[j][k] == 'O' :
            points[j] += 1
            if k != 0 and quiz[j][k-1] == 'O' :
                temp += 1
                points[j] += temp
        else : temp = 0
    temp = 0
    
for element in points :
    print(element)
