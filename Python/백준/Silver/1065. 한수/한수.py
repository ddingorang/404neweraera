a = input("") # 값 입력 받음

if len(a) == 3 or len(a) == 4: # 세 자리수 일때(1000까지의 한수 개수 = 999까지의 한수 개수)
    count = 99 # 일단 1부터 99까지는 전부 한수임
    for i in range(100, int(a)+1) :
        int_i = str(i)
        if int(int_i[2]) - int(int_i[1]) == int(int_i[1]) - int(int_i[0]) : count += 1
        # 1의 자리수 - 10의 자리수 = 10의 자리수 - 100의 자리수이면 한수임
else : count = a # 한 자리수, 두 자리수일 때에는 1부터 입력한 숫자까지 전부 한수임

print(count)