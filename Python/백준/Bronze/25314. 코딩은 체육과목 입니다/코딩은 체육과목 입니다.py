import sys
input1 = sys.stdin.readline().rstrip()
a = int(input1)
string = ''

for _ in range(a // 4) :
    string += 'long '
string += 'int'

print(string)