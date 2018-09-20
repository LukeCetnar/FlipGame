import numpy as np
import sys

def arrayPrint(a):
    for x in range(len(a)):
        print(a[x])

def checkBoard(a):
    xp = a[0][0]
    for x in range(len(a)):
        if(x != xp):
            return True
    return False
#def flip(a):




posible = ("b", "w")
lineCount = 0
playBoard = [[0 for x in range(4)] for y in range(4)]  # initalize array

for i in range(16):  # generate random b/w
    playBoard[lineCount][i - (4 * lineCount)] = posible[np.random.randint(2)]
    var = playBoard[lineCount][i - 4 * lineCount]
    if (i + 1) % 4 == 0:
        lineCount += 1

arrayPrint(playBoard)

print(x,y)
while checkBoard(playBoard):
    x = np.random.randint(4)
    y = np.random.randint(4)


