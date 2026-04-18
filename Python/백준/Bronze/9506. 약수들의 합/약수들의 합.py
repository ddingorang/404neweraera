import sys

n = 0
result = []
while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == -1 : break
    yaksu = []
    for i in range(1, int(n/2)+1) :
        if n % i == 0:
            yaksu.append(i)
    if sum(yaksu) == n :
        strforcn = f'{n} = {yaksu[0]} '
        for j in range(1, len(yaksu)) :
            strforcn += f'+ {yaksu[j]} '
        result.append(strforcn)
    else :
        result.append(f'{n} is NOT perfect.')

for e in result :
    print(e)