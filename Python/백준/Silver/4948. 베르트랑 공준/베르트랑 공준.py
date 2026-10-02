prnum = [] # 테스트 케이스 별 소수의 개수 저장
flag = 0
index = 0 # 테스트 케이스의 인덱스

while True :
    n = int(input(""))
    if n == 0 : break
    prnum.append(0) # 배열 공간 추가
    for i in range(n+1, 2*n+1) :
        if i == 1 : continue # 1은 소수가 아님
        elif i % 2 == 0 and i != 2 : continue # 2를 제외한 짝수는 소수가 아님
        for j in range(3, int(i**0.5) + 1, 2) : # 3부터 홀수만 체크
            if i % j == 0 : 
                flag = 1 # 소수가 아닐 때 아래 if문에 들어가지 않도록 flag
                break
        if flag == 0 : prnum[index] += 1 # 위의 for문을 무사히 통과 : 소수임
        flag = 0
    index += 1 # 다음 케이스 진행
    
for element in prnum :
    print(element)