b = input("")
a = b.upper()
counter = {}
max = 0
str = ''
cnt = 0

for i in range(len(a)) :
    if a[i] in counter :
        counter[a[i]] += 1
    else :
        counter[a[i]] = 1
        
for key in counter :
    if int(counter[key]) > max :
        max = int(counter[key])
        str = key

for key in counter : 
    if int(counter[key]) == max : 
        cnt += 1
    if cnt == 2 : str = '?'
    
print(str)
