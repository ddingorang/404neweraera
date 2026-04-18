import sys
input1 = sys.stdin.readline().rstrip()
a, b = map(int, input1.split(" "))

if a > b : print(">")
elif a < b : print("<")
elif a == b : print("==")