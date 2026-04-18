import sys
input1 = sys.stdin.readline().rstrip()
n, m = map(int, input1.split(" "))
string = {}
count = 0

for _ in range(n) :
    input2 = sys.stdin.readline().rstrip()
    string[input2] = 0

for _ in range(m) :
    input3 = sys.stdin.readline().rstrip()
    try :
        if string[input3] == 0 : count += 1
    except KeyError as exception :
        continue

print(count)