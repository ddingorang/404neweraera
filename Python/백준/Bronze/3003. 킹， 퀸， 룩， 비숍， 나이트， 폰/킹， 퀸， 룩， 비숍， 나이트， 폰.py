from re import S


while 1:
    try:
        king = 1
        queen = 1
        look = 2
        bishop = 2
        knight = 2
        pawn = 8
        
        k, q, l, b, kn, p = input("").split()
        
        format_a = "{} {} {} {} {} {}".format(king-int(k), queen-int(q), look-int(l), bishop-int(b), knight-int(kn), pawn-int(p))
        print(format_a)
        
        break
            
    except EOFError : 
        break