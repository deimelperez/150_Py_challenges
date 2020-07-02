word = input("word: ")
first = word[0]
rest =  word[1:len(word)]
if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
    word = rest + first + 'ay'
else:
    word = word + 'way'
print(word)
