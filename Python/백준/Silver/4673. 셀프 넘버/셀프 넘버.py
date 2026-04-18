while 1:
    try:
        a = []
        b = []
        sum = 0
        for i in range(1, 10001) :
            a.append(i)
        
        for e in a:
            s = 0
            for element in str(e) :
                s += int(element)
            sum = int(e) + int(s)
            if sum in a :
                b.append(sum)
        
        for element in b:
            if element in a:
                a.remove(element)
        
        # print(a)
        # print(b)
        
        for element in a :
            print(element)
        
        break
            
    except EOFError : 
        break