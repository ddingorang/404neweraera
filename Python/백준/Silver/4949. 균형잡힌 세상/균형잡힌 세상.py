result = []
stack = []
bracket = ['(', ')', '[', ']']
while 1 :
    inputstr = input("")
    done = False
    if inputstr == '.' : break
    for i in range(len(inputstr)) :
        c = inputstr[i]
        if c in bracket :
            stack.append(c)

        if (c == ')' or c == ']') and len(stack) == 1 :
            done = True
            break
        elif c == ')' and stack[-2] == '(' :
            stack.pop()
            stack.pop()
        elif c == ']' and stack[-2] == '[' :
            stack.pop()
            stack.pop()
    if done == True : result.append('no')
    elif not stack : result.append('yes')
    else : result.append('no')
    stack.clear()

for element in result :
    print(element)