casenumber = int(input("")) # 테스트 케이스 수
test = [0]*casenumber # 학생의 수, 점수 저장
avg = [0]*casenumber # 평균
sum = [0]*casenumber # 합
ratio = [0] * casenumber # 평균 넘는 학생 비율
count = 0 # 평균 넘는 학생 수

for i in range(casenumber) : 
    test = input("").split(" ") # 학생 수와 점수들을 공백을 사이에 두고 입력
    for j in range(1, len(test)) : # 학생 점수는 인덱스 1부터
        test[j] = int(test[j])
        sum[i] += test[j]
    avg[i] = sum[i] / float(test[0]) # 평균 계산
    for k in range(1, len(test)) :
        if(test[k] > avg[i]) : count += 1 # 평균보다 점수가 큰 학생이라면 카운트 하나 올림
        ratio[i] = count / float(test[0]) # 비율 = 평균보다 높은 학생 수 / 전체 학생 수
    count = 0

for l in range(casenumber) :
    print("{:.3f}%".format(100 * ratio[l])) # 출력
    
