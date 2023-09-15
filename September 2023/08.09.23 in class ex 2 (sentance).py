sentence = str(input("Please enter a sentence: "))
sentence = sentence.split(" ")
print(sentence)

for word in sentence:
    word = list(word)
    print(word[0])