import random


def randomWordFromTxt():
    allWords = list()
    with open("word_list.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.split()
            allWords.append(line[0])
    randomWord = allWords[random.randint(0, len(allWords) - 1)]

    return randomWord


secretWord = randomWordFromTxt()
secretWordWithStars = "*" * len(secretWord)
currentStatus = str()
guessLetterList = list()
howManyTry = int()

for letter in secretWordWithStars: guessLetterList.append(letter)

print("The word contains {} letters.".format(len(secretWord)))

while secretWord.upper() != currentStatus:
    indexOfArray = 0
    letterCounter = 0
    howManyTry += 1
    anyLetter = input("Please enter one letter or a {}-letter word:".format(len(secretWord)))

    if len(anyLetter) == 1:
        for e in secretWord:
            if e.upper() == anyLetter.upper():
                guessLetterList[indexOfArray] = anyLetter.upper()
                letterCounter += 1

            indexOfArray += 1
        currentStatus = str()

        for e in guessLetterList: currentStatus += e

        if letterCounter == 1:
            print("Yes! The word contains the letter '{}'\n{}".format(anyLetter, currentStatus))
        elif letterCounter == 0:
            print("The letter {} is not found.\n{}".format(anyLetter, currentStatus))
        else:
            print("Yes the word contains '{}'s.\n{}".format(anyLetter, currentStatus))
    else:
        currentStatus = str()
        tempList = list()
        for e in anyLetter: tempList.append(e)
        for e in [x.upper() for x in tempList]: currentStatus += e
        if secretWord.upper() != currentStatus:
            print("Wrong guess.")

print("Yes, the word is {}! You got it {} tries.".format(secretWord, howManyTry))
input()
