t1, b1 = map(int, input('').split(' '))
t2, b2 = map(int, input('').split(' '))

sumb = b1*b2
sumt = t1*b2 + t2*b1

rstt, rstb = sumt, sumb
while sumb != 0: # 유클리드 호제법(최대공약수 구하기)
    sumt, sumb = sumb, sumt % sumb
print(int(rstt / sumt), int(rstb / sumt))