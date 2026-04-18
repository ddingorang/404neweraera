a, b = map(int, input('').split(' '))

mul = a*b
while b != 0: # 유클리드 호제법(최대공약수 구하기)
    a, b = b, a%b

print(int(mul/a))