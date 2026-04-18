n, b = map(int, input('').split(' '))
save = []
while n >= b :
    save.append(n%b)
    n = n // b
save.append(n)

for i in range(len(save)) :
    if save[i] >= 10 :
        save[i] = chr(save[i]-10+65)

s = ''
for j in range(len(save)-1, -1, -1) :
    s += str(save[j])
print(s)