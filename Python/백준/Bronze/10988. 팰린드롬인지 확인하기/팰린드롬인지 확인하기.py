word = input("")

if len(word) % 2 == 0 :
    tomato = 1
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-1-i] :
            tomato = 0
            break

if len(word) % 2 == 1 :
    tomato = 1
    for i in range(int((len(word)-1)/2)):
        if word[i] != word[len(word)-1-i] :
            tomato = 0
            break

print(tomato)