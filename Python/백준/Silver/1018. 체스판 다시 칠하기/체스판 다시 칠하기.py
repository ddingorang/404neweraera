def check(n, m, arr) :
    count = 0
    countlist = []
    for i in range(n - 7):
        for j in range(m - 7):
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if chess[k][l] != arr[k - i][l - j]:
                        count += 1
            if count == 0:
                countlist.append(count)
                break
            countlist.append(count)
            count = 0

    return min(countlist)

n, m = map(int, input("").split())
chess = []
bw = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
wb = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

for _ in range(n) :
    s = input("")
    chess.append(s)

print(min(check(n, m, bw), check(n, m, wb)))