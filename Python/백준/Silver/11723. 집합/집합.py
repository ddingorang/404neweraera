import sys

n = int(sys.stdin.readline().rstrip())
result = []
alllist = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
s = set()
for _ in range(n) :
    c = sys.stdin.readline().rstrip()
    if c == 'all' :
        s = set(alllist)
    elif c == 'empty' :
        s = set()
    else :
        cmd, num = c.split(' ')
        if cmd == 'add' :
            s.add(num)
        elif cmd == 'check' :
            if num in s :
                print(1)
            else :
                print(0)
        elif cmd == 'remove' :
            s.discard(num)
        elif cmd == 'toggle' :
            if num in s :
                s.discard(num)
            else :
                s.add(num)
