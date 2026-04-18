while 1:
    try:
        def solve(a):
            ans = sum(a)
            return ans

        b = input()
        a = []
        int_b = int(b)

        for i in range(1, int_b+1) :
            a.append(i)
            
        print(solve(a))
        
    except EOFError : 
        break