import numpy as np
import copy
import time

def arrayPrint(a):
    for x in range(len(a)):
        for y in range(len(a[x])):
            print a[x][y],

        print()


def checkBoard(a):
    xp = a[0][0]
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] != xp:
                return True
            xp = a[x][y]

    return False


def bruteForce(array):
    count = 0
    while checkBoard(array):
        x = np.random.randint(4)
        y = np.random.randint(4)

        flip(array, x, y)
        count += 1
    return array, count


def flip(array, xPos, yPos):
    if array[xPos][yPos] == "b":
        array[xPos][yPos] = "w"
    else:
        array[xPos][yPos] = "b"

    if xPos < 3 and array[xPos + 1][yPos] == "b":
        array[xPos + 1][yPos] = "w"
    elif xPos < 3:
        array[xPos + 1][yPos] = "b"

    if xPos < 0 and array[xPos - 1][yPos] == "b":
        array[xPos - 1][yPos] = "w"
    elif xPos < 0:
        array[xPos - 1][yPos] = "b"

    if yPos < 3 and array[xPos][yPos + 1] == "b":
        array[xPos][yPos + 1] = "w"
    elif yPos < 3:
        array[xPos][yPos + 1] = "b"

    if yPos < 0 and array[xPos][yPos - 1] == "b":
        array[xPos][yPos - 1] = "w"
    elif yPos < 0:
        array[xPos][yPos - 1] = "b"

    return array


playBoard = [[0 for x in range(4)] for y in range(4)]  # initalize array
colorSet = "b", "w"
for x in range(len(playBoard)):
    for y in range(len(playBoard[x])):
        playBoard[x][y] = colorSet[np.random.randint(2)]
myCount=101
tries = 0
arrayPrint(playBoard)
tic = time.clock()
while myCount > 100:
    tmp = copy.deepcopy(playBoard)
    myArray, myCount = bruteForce(tmp)
    tries += 1
toc = time.clock()
print toc-tic,
print ' seconds'
print'completed in ',
print myCount,
print 'tries'
print tries
arrayPrint(playBoard)
