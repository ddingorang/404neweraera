from re import S


while 1:
    try:
        n = input("")
        a = []
        int_n = int(n)
        
        a = list(map(int, input("").split()))
        
        m = max(a)
        
        while int_n > 0:
            a[int_n-1] = a[int_n-1] / m * 100
            int_n -= 1
            
        avg = sum(a) / len(a)
        
        print(avg)
            
        break
            
    except EOFError : 
        break