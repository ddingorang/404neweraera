from re import S


while 1:
    try:
        x = input("")
        n = input("")
        sum = 0
        int_x = int(x)
        int_n = int(n)
        
        while int_n > 0:
            a, b = input("").split()
            sum += (int(a) * int(b))
            int_n -= 1
        
        if sum == int_x:
            print("Yes")
        else :
            print("No")
            
        break
            
    except EOFError : 
        break