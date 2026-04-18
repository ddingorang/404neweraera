n = input("").rstrip()
string = []

for i in range(len(n)) :
    for j in range(len(n)-i) :
        string.append(n[i:i+j+1])

print(len(set(string)))