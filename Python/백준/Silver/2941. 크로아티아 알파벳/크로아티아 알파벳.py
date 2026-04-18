a = input("")
length = len(a)

for i in range(1, len(a)) :
    if i >= 2 : 
        if 'dz=' in a[i-2: i+1] : length -= 1
    if 'c=' in a[i-1 : i+1] : length -= 1
    if 'c-' in a[i-1 : i+1] : length -= 1
    if 'd-' in a[i-1 : i+1] : length -= 1
    if 'lj' in a[i-1 : i+1] : length -= 1
    if 'nj' in a[i-1 : i+1] : length -= 1
    if 's=' in a[i-1 : i+1] : length -= 1
    if 'z=' in a[i-1 : i+1] : length -= 1

print(length)