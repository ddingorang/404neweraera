n = int(input("")) # 개수
l = list(map(int, input("").split(' '))) # 수열

s = [] # 스택
nge = [0 for _ in range(n)] # 오큰수 저장하는 배열
for i in range(n) :
    while s and l[i] > l[s[-1]] : # 현재 수가 스택에 있는 인덱스를 가지는 수보다 크면 = 오큰수
        nge[s.pop()] = l[i] # 스택에서 빼고, 그 수를 오큰수로 저장
    s.append(i) # 다음 원소 넣기

for e in s : # 스택에 남아있는 인덱스는 오큰수가 없는 경우
    nge[e] = -1

for element in nge:
    print(element, end=' ')