testnum = input("")
word = [''] * 100
counter = {}
gwordnum = int(testnum)

for i in range(int(testnum)) :
    word = input("")
    for j in range(len(word)) :
        if word[j] in counter :
            if word[j-1] == word[j] : pass
            else : 
                gwordnum -= 1
                break
        elif word[j] not in counter :
            counter[word[j]] = 1
    counter = {}

print(gwordnum)