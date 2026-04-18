n = int(input(""))
result = []

for _ in range(n) :
    s = input("")
    result.append(s[0] + s[len(s)-1])

for element in result :
    print(element)