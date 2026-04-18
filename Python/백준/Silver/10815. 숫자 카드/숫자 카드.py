import sys
input1 = sys.stdin.readline().rstrip()
n = int(input1)
input2 = sys.stdin.readline().rstrip()
s = list(input2.split(" "))
dict = {}
for element in s :
    dict[element] = 1

input3 = sys.stdin.readline().rstrip()
m = int(input3)
input4 = sys.stdin.readline().rstrip()
k = list(input4.split(" "))

for i, element in enumerate(k) :
    try:
        if dict[element] - 1 == 0 : k[i] = 1
    except KeyError as exception:
        k[i] = 0

for element in k :
    print(f'{element} ', end="")