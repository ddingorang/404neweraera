
result = []
while True:
    word = input()
    if word == "end" : break

    acceptable = True
    vowel = ['a', 'e', 'i', 'o', 'u']
    hasVowel = False
    for v in vowel:
        if v in word:
            hasVowel = True
            break
    if not hasVowel:
        result.append((word, False))
        acceptable = False
    if not acceptable: continue

    for i in range(len(word)-2) :
        sliced = word[i:i+3]
        vowelCount = 0
        for j in range(len(sliced)) :
            if sliced[j] in vowel : vowelCount += 1
        if vowelCount == 3 or vowelCount == 0 :
            result.append((word, False))
            acceptable = False
            break
    if not acceptable: continue

    for k in range(len(word)-1) :
        sliced = word[k:k+2]
        if sliced == 'ee' or sliced == 'oo' : continue
        elif sliced[0] == sliced[1] :
            result.append((word, False))
            acceptable = False
            break
    if not acceptable: continue

    result.append((word, True))

for e in result :
    if e[1]:
        print(f'<{e[0]}> is acceptable.')
    else :
        print(f'<{e[0]}> is not acceptable.')


