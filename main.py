import random

f = open("words.txt")


numWords = 0

while(f.readline()):
    numWords += 1

f.close()
f = open("words.txt")


wordIndex = random.randint(0,numWords-1)
currWordIndex = 0

while(currWordIndex != wordIndex):
    f.readline()
    currWordIndex += 1

print(currWordIndex)

word = f.readline()

word = word[0:9]

f.close()

# scramble word

wordList = [i for i in word]


scrambledWord = ""

while(not len(wordList) == 0):
    pos = random.randint(1,len(wordList)) - 1
    scrambledWord += wordList.pop(pos)
    

print(scrambledWord[0:3])
print(scrambledWord[3:6])
print(scrambledWord[6:9])





