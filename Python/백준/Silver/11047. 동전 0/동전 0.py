
n, k = map(int, input("").split(" "))
coins = []
count = 0
for _ in range(n) :
    c = int(input(""))
    coins.append(c)

for i in range(len(coins)-1, -1, -1) :
    while 1 :
        if k >= coins[i] :
            count += (k // coins[i])
            k = k % coins[i]
        else : break

print(count)