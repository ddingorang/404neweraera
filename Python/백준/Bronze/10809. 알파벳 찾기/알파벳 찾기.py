a = input("")
list = [0]*26
for i in range(97, 123) :
    if chr(i) not in a : list[i-97] = -1
    else : list[i-97] = a.find(chr(i)) 
    
for i in range(26) :
    print(list[i], end=" ")
