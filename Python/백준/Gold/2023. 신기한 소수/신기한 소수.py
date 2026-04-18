import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

def isPrime(x) :
    for i in range(2, int(x/2+1)) :
        if x % i == 0 : return False
    return True

def dfs(x) :
    if len(str(x)) == n : print(x)
    else :
        for i in range(1, 10, 2) :
            if isPrime(10 * x + i) :
                dfs(10 * x + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)