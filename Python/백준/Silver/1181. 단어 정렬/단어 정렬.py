
n = int(input(""))
word = []
for i in range(n) :
    word.append(str(input("")))

unique_word = list(set(word))
unique_word.sort(key=lambda x : (len(x), x))
for element in unique_word :
    print(element)