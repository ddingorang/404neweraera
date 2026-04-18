letters = []
for i in range(5) : # 한 줄씩 다섯번 받음
    line = input("")
    letters.append(line)

for i in range(15) : # 열
    for j in range(5) : # 행
        try :
            print(letters[j][i], end="") # 세로로 읽기
        except IndexError as exception : # 빈 칸을 마주하면 그냥 이어가기
            continue