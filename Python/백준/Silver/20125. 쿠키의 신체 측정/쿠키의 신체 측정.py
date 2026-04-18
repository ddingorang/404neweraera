
n = int(input())
cookie = []
for _ in range(n) :
    cookie.append(input())

# 심장의 좌표
heart = ()
# 엉덩이(허리의 끝)의 좌표
hip = ()

# 심장 찾기
for i in range(n) :
    for j in range(n) :
        if 0 <= i < n-1 and 0 <= j < n-1 :
            if cookie[i][j] == '*' and cookie[i][j+1] == '*' \
                    and cookie[i+1][j] == '*' and cookie[i-1][j] == '*' and cookie[i][j-1] == "*":
                heart = (i, j)

# 왼쪽 팔 길이
leftarm = 0
curx, cury = heart
while True :
    if cury - 1 >= 0 :
        if cookie[curx][cury-1] == "*" :
            leftarm += 1
            cury -= 1
        else :
            break
    else :
        break

# 오른쪽 팔 길이
rightarm = 0
curx, cury = heart
while True :
    if cury + 1 < n :
        if cookie[curx][cury+1] == "*" :
            rightarm += 1
            cury += 1
        else :
            break
    else :
        break

# 허리 길이
waist = 0
curx, cury = heart
while True :
    if curx + 1 < n :
        if cookie[curx+1][cury] == "*" :
            waist += 1
            curx += 1
        else :
            hip = (curx, cury) # 엉덩이 위치 파악
            break
    else :
        break

# 왼쪽 다리 길이
leftleg = 1
curx, cury = hip[0] + 1, hip[1] - 1
while True :
    if curx + 1 < n :
        if cookie[curx+1][cury] == "*" :
            leftleg += 1
            curx += 1
        else :
            break
    else :
        break

# 오른쪽 다리 길이
rightleg = 1
curx, cury = hip[0] + 1, hip[1] + 1
while True :
    if curx + 1 < n :
        if cookie[curx+1][cury] == "*" :
            rightleg += 1
            curx += 1
        else :
            break
    else :
        break

print(heart[0]+1, heart[1]+1)
print(leftarm, rightarm, waist, leftleg, rightleg)