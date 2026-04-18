import sys

n = list(sys.stdin.readline().rstrip().split('-')) # 일단 '-' 기준으로 split함
for j in range(len(n)) :
    if n[j][0] == '0' : # 숫자 앞에 0이 있을 때
        s = ''
        for l in n[j] :
            if l != '0' : s += l # 0만 빼고 배열에 추가
    if '+' in n[j] : # '+'가 사이에 있으면
        n[j] = sum(map(int, n[j].split('+'))) 
        # '+' 기준으로 split 후
        # 문자를 정수로 변환
        # 그리고 합을 구함
    else :
        n[j] = int(n[j]) # 숫자 혼자 있는 경우 : 정수로만 변환시켜 줌
        
s = n[0] # 첫 수는 더하고
for i in range(1, len(n)) :
    s -= int(n[i]) # 뒤부터는 다 빼주면 됨
print(s) # 결과 출력

# 앞에 '-'를 두고, 그 뒤로는 최대한 '+'끼리 뭉치게 해야 최소값이 됨 -> 그리디
# 먼저 '-'를 기준으로 쪼개 보면, 1)숫자 한 개만 남는 경우와 2)'+'를 기준으로 뭉친 숫자들로 쪼개짐