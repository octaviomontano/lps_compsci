import random

words = open('words.txt','r')
wordsList = []
word = words.readline()

while word != '':
    wordsList.append(word)
    word = words.readline()

num = random.randint(0, len(wordsList) - 1)
print(wordsList[num])
