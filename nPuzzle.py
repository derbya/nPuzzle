from enum import Enum
import calendar
import time
import math
import sys

identityCounter = 0

startTime = calendar.timegm(time.gmtime())

class Move(Enum):
    START   = 0
    LEFT    = 1
    RIGHT   = 2
    UP      = 3
    DOWN    = 4

class Puzzle:
    def __init__(self, puzzle, weight, owner, moves):
        self.puzzle = puzzle
        self.weight = weight
        self.id = arrayToString(puzzle)
        self.owner = owner
        self.moves = moves

    def printPuzzleClass(self):
        print(self.puzzle)
        printPuzzle(self.puzzle)
        print("\nWeight: " + str(self.weight))
        print("id: " + self.id)
        print("parent: " + self.owner)
        print("moves: " + str(self.moves))

#example = [  15, 2, 1, 12,
#        8, 5, 6, 11,
#        4, 9, 10, 7,
#        3, 14, 13, 0]

#example = [1, 2, 3, 4,
#        5, 6, 7, 8,
#        0, 10, 11, 12,
#        9, 13, 14, 15]

#example = [1, 8, 2,
#        0, 4, 3,
#        7, 6, 5,]

#example = [13, 2, 10, 3,
#        1, 12, 8, 4,
#        5, 0, 9, 6,
#        15, 14, 11, 7]

#example = [ 0, 5, 1, 4,
#            9, 6, 2, 8,
#            10, 14, 3, 11,
#            13, 15, 7, 12 ]

example = [ 0, 2, 1, 3,
            4, 5, 6, 7,
            8, 9, 10, 11,
            12, 13, 14, 15 ]

#example = [ 2, 1, 3, 4,
#            5, 6, 7, 8,
#            9, 10, 11, 0,
#            13, 14, 15, 12]

#example = [ 2,  3,  9,  4,  5,  6,
#            1,  8,  21,  10, 11, 12,
#            7, 13, 0, 15, 16, 17,
#            19, 14, 27, 22, 23, 18,
#            25, 20, 28, 29, 24, 30,
#            31, 26, 32, 33, 34, 35]

#example = [0, 1, 2, 3,
#            5, 6, 7, 4,
#            9, 10, 11, 8,
#            13, 14, 15, 12]

#example = [ 1, 3, 4, 0,
#            12, 2, 14, 5,
#            11, 13, 15, 6,
#            10, 9, 8, 7 ]

#example = [1, 2, 3, 4,
#            5, 6, 7, 8,
#            9, 10, 11, 12,
#            13, 14, 0, 15]

#example = [ 1, 7, 2, 3, 5,
#            6, 12, 8, 9, 4,
#            11, 17, 13, 10, 15,
#            16, 18, 14, 20, 0,
#            21, 22, 23, 19, 24]

theRoot = math.sqrt(len(example))

def returnSolvedExample(size):
    solvedPuzzle = []
    for i in range(size - 1):
        solvedPuzzle.append(i + 1)
    solvedPuzzle.append(0)
    return solvedPuzzle

def ifSolved(puzzle, solved):
    if puzzle == solved:
        return True
    else:
        return False

#"""
def getWeight(puzzle, solved, moves):
    weight = moves
    for i in range(len(puzzle)):
        if i != movePiece:
            weight += abs(abs((puzzle.index(i) % theRoot) - (i - 1 % theRoot)) + abs(int(abs(puzzle.index(i) / theRoot)) - int(abs((i - 1) / theRoot))))
    return weight 
#"""

#    for i in range(len(puzzle)):
#        try:
#            if puzzle.index(i) < puzzle.index(i + 1):
#                weight -= 5
#            else:
#                weight += 5
#        except ValueError:

""" hueuristic 2
def getWeight(puzzle, solved, moves):
    weight = moves
    for i in range(len(puzzle)):
        if puzzle[i] != solved[i]:
            weight += 5
    return weight
#"""
movePiece = 0
def moveUp(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(movePiece)
    newPuzzle = puzzle.copy()
    if index < len(puzzle) / len(puzzle):
        return None
    else:
        newPuzzle[index], newPuzzle[int(index - theRoot)] = newPuzzle[int(index - theRoot)], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def moveDown(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(movePiece)
    newPuzzle = puzzle.copy()
    if index > len(puzzle) - 1 - math.sqrt(len(puzzle)):
        return None
    else:
        newPuzzle[index], newPuzzle[int(index + theRoot)] = newPuzzle[int(index + theRoot)], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def moveRight(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(movePiece)
    newPuzzle = puzzle.copy()
    if index % math.sqrt(len(puzzle)) == 0:
        return None
    else:
        newPuzzle[index], newPuzzle[index - 1] = newPuzzle[index - 1], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def moveLeft(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(movePiece)
    newPuzzle = puzzle.copy()
    if (index + 1) % theRoot == 0:
        return None
    else:
        newPuzzle[index], newPuzzle[index + 1] = newPuzzle[index + 1], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def insertChild(Puzzle, queue):
    insertCheck = False
    if not queue:
        pass
    else:
        for i in range(len(queue)):
            if queue[i].weight >= Puzzle.weight:
                queue.insert(i, Puzzle)
                insertCheck = True
                break
    if not insertCheck:
        queue.append(Puzzle)

def duplicatePuzzle(popped, poppedPuzzles):
    try:
        if poppedPuzzles[popped.id]:
            return True
    except KeyError:
        return False

worldClock = 0

def arrayToString(array):
    return "'".join([str(num) for num in array])

def remapEndSolution(oldPuzzle):
    puzzle = []
    for i in range(len(oldPuzzle)):
        if oldPuzzle[i] == 5:
            puzzle.append(12)
        elif oldPuzzle[i] == 6:
            puzzle.append(13)
        elif oldPuzzle[i] == 7:
            puzzle.append(14)
        elif oldPuzzle[i] == 8:
            puzzle.append(5)
        elif oldPuzzle[i] == 9:
            puzzle.append(11)
        elif oldPuzzle[i] == 10:
            puzzle.append(0)
        elif oldPuzzle[i] == 11:
            puzzle.append(15)
        elif oldPuzzle[i] == 12:
            puzzle.append(6)
        elif oldPuzzle[i] == 13:
            puzzle.append(10)
        elif oldPuzzle[i] == 14:
            puzzle.append(9)
        elif oldPuzzle[i] == 15:
            puzzle.append(8)
        elif oldPuzzle[i] == 0:
            puzzle.append(7)
        else:
            puzzle.append(oldPuzzle[i])
    return puzzle

def printPuzzle(oldPuzzle):
    puzzle = remapEndSolution(oldPuzzle)
    for i in range(len(puzzle)):
        if i % theRoot == 0:
            print("")
        print(str(puzzle[i]), end = " ")
        if puzzle[i] < 10:
            print(end = " ")

def printStateOrder(start, end, poppedPuzzles):
    endPuzzle = end
    print("=====================================================")
    while True:
        print("\n")
        popped = poppedPuzzles[endPuzzle.owner]
        if popped.puzzle == start:
            printPuzzle(endPuzzle.puzzle)
            print("\n")
            printPuzzle(popped.puzzle)
            break
        printPuzzle(endPuzzle.puzzle)
        endPuzzle = popped
    print("\n\n\n=====================================================")

def remapPuzzle(oldPuzzle):
    puzzle = []
    global movePiece
    for i in range(len(oldPuzzle)):
        if oldPuzzle[i] == 0:
            puzzle.append(10)
            movePiece = 10
        elif oldPuzzle[i] == 12:
            puzzle.append(5)
        elif oldPuzzle[i] == 13:
            puzzle.append(6)
        elif oldPuzzle[i] == 14:
            puzzle.append(7)
        elif oldPuzzle[i] == 5:
            puzzle.append(8)
        elif oldPuzzle[i] == 11:
            puzzle.append(9)
        elif oldPuzzle[i] == 15:
            puzzle.append(11)
        elif oldPuzzle[i] == 6:
            puzzle.append(12)
        elif oldPuzzle[i] == 10:
            puzzle.append(13)
        elif oldPuzzle[i] == 9:
            puzzle.append(14)
        elif oldPuzzle[i] == 8:
            puzzle.append(15)
        elif oldPuzzle[i] == 7:
            puzzle.append(0)
        else:
            puzzle.append(oldPuzzle[i])
    return puzzle

def solvePuzzle(queue, solved):
    global identityCounter
    global worldClock
    startingPuzzle = queue[0].puzzle.copy()
    poppedPuzzles = {}
    queuedPuzzles = {}
    while True:
#        input("step?")
        worldClock += 1
        popped = queue.pop(0)
        identityCounter += 4
#        print(popped.puzzle)
#        popped.printPuzzleClass()
        if ifSolved(popped.puzzle, solved):
            printStateOrder(startingPuzzle, popped, poppedPuzzles)
            exit()
        if not duplicatePuzzle(popped, poppedPuzzles):
            currentMoves = []
            currentMoves.append(moveLeft(popped.puzzle, popped.id, popped.moves, solved))
            currentMoves.append(moveRight(popped.puzzle, popped.id, popped.moves, solved))
            currentMoves.append(moveDown(popped.puzzle, popped.id, popped.moves, solved))
            currentMoves.append(moveUp(popped.puzzle, popped.id, popped.moves, solved))
            for i in currentMoves:
                if i:
                    if not duplicatePuzzle(i, poppedPuzzles):
                        if not duplicatePuzzle(i, queuedPuzzles):
                            insertChild(i, queue)
                            queuedPuzzles.update( { i.id : i  } )
            poppedPuzzles.update( { popped.id : popped } )


puzzleQueue = []
newPuzzle = remapPuzzle(example)
solvedPuzzle = returnSolvedExample(len(newPuzzle))
print(newPuzzle)
puzzleQueue.append(Puzzle(newPuzzle, getWeight(newPuzzle, solvedPuzzle, 0), arrayToString(newPuzzle), 0))
solvePuzzle(puzzleQueue, solvedPuzzle)
print(startTime - calendar.timegm(time.gmtime()))
