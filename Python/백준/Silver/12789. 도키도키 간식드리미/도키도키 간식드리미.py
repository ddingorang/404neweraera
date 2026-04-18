target = 1
result = 'Nice'
n = int(input(""))
wait = list(map(int, input("").split()))
wait.reverse()
another = []

while len(wait) > 0 :
    if wait[-1] == target :
        wait.pop()
        target += 1
        if len(another) > 0:
            while target == another[-1] :
                another.pop()
                target += 1
                if len(another) == 0: break
    else :
       another.append(wait.pop())
       if len(another) > 1 :
           if another[-1] > another[-2] :
               result = 'Sad'

print(result)