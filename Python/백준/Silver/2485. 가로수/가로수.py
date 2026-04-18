n = int(input())
tree = []
gap = []
curr = 0
need = 0

def euc(a, b) :
    while b != 0:
        a, b = b, a%b
    return a

for _ in range(n) :
    tree.append(int(input()))
for i in range(1, len(tree)) :
    g = tree[i] - tree[i-1]
    gap.append(g)

curr = euc(gap[1], gap[0])
for j in range(2, len(gap)) :
    curr = euc(curr, gap[j])

for k in range(len(gap)) :
    need += gap[k] / curr - 1
print(int(need))