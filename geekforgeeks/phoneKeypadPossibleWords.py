#Possible words from Phone KeyPad

keypad = ['','',
          ['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i'],
          ['j', 'k', 'l'],
          ['m', 'n', 'o'],
          ['p', 'q', 'r', 's'],
          ['t', 'u', 'v'],
          ['w', 'x', 'y', 'z']]

wordList = list()

def getOutput(word):
    print(word, end=' ')
    return

def getLetters(number):
    return keypad[number]

def printPossibleWordsUtil1(l1, l2):
    tempList = list()
    for w1 in l1:
        for w2 in l2:
            tempList.append(w1+w2)
    return tempList


def printPossibleWords(numList):
    global wordList
    wordList.extend(numList.pop())
    while numList:
        wordList = printPossibleWordsUtil1(numList.pop(), wordList)
        #print(wordList)
#endfunc


t = int(input())
for tc in range(t):
    n = int(input())
    nList = list(map(int, input().strip().split(' ')))
    wList = list(map(getLetters, nList))
    printPossibleWords(wList)
    list(map(getOutput, wordList))
    