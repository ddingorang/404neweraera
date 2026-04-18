n = int(input())
rslt = []
for _ in range(n) :
    a, b = map(int, input('').split(' '))
    mul = a * b
    while b != 0:  # 유클리드 호제법(최대공약수 구하기)
        a, b = b, a % b
    rslt.append(int(mul/a))

for e in rslt :
    print(e)