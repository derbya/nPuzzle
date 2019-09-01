import sys
import random

argumentDictionary = {}
theRoot = 5

def moveLeft(puzzle):
    index = puzzle.index(0)
    if index >= len(puzzle) - theRoot:
        pass
    else:
        puzzle[index], puzzle[index + 1] = puzzle[index + 1], puzzle[index]
    return puzzle

def moveRight(puzzle):
    index = puzzle.index(0)
    if index % theRoot == 0:
        pass
    else:
        puzzle[index], puzzle[index - 1] = puzzle[index - 1], puzzle[index]
    return puzzle

def moveUp(puzzle):
    index = puzzle.index(0)
    if index < theRoot:
        pass
    else:
        puzzle[index], puzzle[int(index - theRoot)] = puzzle[int(index - theRoot)], puzzle[index]
    return puzzle

def moveDown(puzzle):
    index = puzzle.index(0)
    if index >= len(puzzle) - theRoot:
        pass
    else:
        puzzle[index], puzzle[int(index + theRoot)] = puzzle[int(index + theRoot)], puzzle[index]
    return puzzle

moveDictionary = {
        1 : moveLeft,
        2 : moveRight,
        3 : moveUp,
        4 : moveDown
        }

def hamming():
    pass

def manhattan():
    pass

def printUsage():
    print("\nUsage: python3 nPuzzle [-f filename] | [-r size] [-h heuristic]\n")
    print("All flags are optional, and defaults to '-r 4' '-h manhattan'\n")
    print("-f flag must be followed by a valid file name:                   -f file")
    print("-r flag must be followed by the size of the random puzzle:       -r 4")
    print("-h flag must be followed by a valid heuristic:                   -h manhattan")
    print("\nvalid heuristics: manhattan, hamming, third option\n")

heuristicDictionary = {
        "hamming" : hamming,
        "manhattan" : manhattan
        }

def updateDictionary(argNum, arg):
    global argumentDictionary
    try:
        argumentDictionary.update( { arg : sys.argv[argNum + 1]  } )
    except IndexError:
        printUsage()
        exit()

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-f" or sys.argv[i] == "-h" or sys.argv[i] == "-r":
        updateDictionary(i, sys.argv[i])

path = None
size = 4
heuristic = "manhattan"


def generateRandomPuzzle(size):
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]#returnSolvedPuzzle(size)
    randomMoveNumber = random.randint(0, 250)
    print(randomMoveNumber)
    for i in range(randomMoveNumber):
        puzzle = moveDictionary[random.randint(1, 4)](puzzle)
    return puzzle
    

def getPuzzleFromFile(filename):
    tab = generateRandomPuzzle(2)
    print(filename)
    return tab


def start():
    global path
    global size
    global heuristic
    try:
        path = argumentDictionary["-f"]
    except KeyError:
        pass
    try:
        size = int(argumentDictionary["-r"])
    except KeyError:
        pass
    try:
        heuristic = argumentDictionary["-h"]
    except KeyError:
        pass
    if path:
        filename = open(path, "r")
        print("this is a file arg")
        startingPuzzle = getPuzzleFromFile(filename)
    else:
        print(size)
        startingPuzzle = generateRandomPuzzle(size)
        print(startingPuzzle)

start()
print(argumentDictionary)
