from re import S


while 1:
    try:
        a = []
        b = []
        c = []
        
        for i in range(0,10) :
            a.append(input(""))
            
        for i in range(0,10) :
            b.append(int(a[i]) % 42)
            
        for element in b:
            if element in c :
                pass
            else :
                c.append(element)
        
        print(len(c))
        break
            
    except EOFError : 
        break