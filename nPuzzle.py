from enum import Enum
import calendar
import time
import math
import sys
import heapq

identityCounter = 0

startTime = calendar.timegm(time.gmtime())

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

#"""
example = [ 0, 2, 1, 3,
            4, 5, 6, 7,
            8, 9, 10, 11,
            12, 13, 14, 15 ]
#"""

#example = [1, 14, 3, 0,
#            11, 2, 12, 5,
#            10, 13, 8, 15,
#            9, 6, 7, 4]

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

"""           1  2  3  4
           5  6  7  8
           9  10 11 12
           13 14 15 0

           1  2  3  4
           12 13 14 5
           11 0  15 6
           10 9  8  7"""

"""
example = [2, 3, 4, 5,
           1, 12, 14, 6,
           13, 15, 7, 0,
           11, 10, 9, 8]
#"""

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
        if i != 0:
#            print("i = " + str(i))
#            print(movePiece)
#            print(" column: " + str(abs((puzzle.index(i) % theRoot) - (solved.index(i) % theRoot))))
#            print("row: " + str(abs(int(puzzle.index(i) / theRoot) - int(solved.index(i) / theRoot))))
            column = abs((puzzle.index(i) % theRoot) - (solved.index(i) % theRoot))
            row = abs(int(puzzle.index(i) / theRoot) - int(solved.index(i) / theRoot))
            weight += row + column#(abs((puzzle.index(i) % theRoot) - (solved.index(i) % theRoot) + abs(int(puzzle.index(i) / theRoot) - int(solved.index(i) / theRoot))))
#            print("Weight: " + str(weight))
#            print()
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
    index = puzzle.index(0)
    newPuzzle = puzzle.copy()
    if index < theRoot:
        return None
    else:
        newPuzzle[index], newPuzzle[int(index - theRoot)] = newPuzzle[int(index - theRoot)], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def moveDown(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(0)
    newPuzzle = puzzle.copy()
    if index >= len(puzzle) - theRoot:
        return None
    else:
        newPuzzle[index], newPuzzle[int(index + theRoot)] = newPuzzle[int(index + theRoot)], newPuzzle[index]
        return (Puzzle(newPuzzle,
            getWeight(newPuzzle, solved, moves),
            identity,
            moves + 1))

def moveRight(puzzle, identity, moves, solved):
    global identityCounter
    index = puzzle.index(0)
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
    index = puzzle.index(0)
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


def printPuzzle(puzzle):
#    puzzle = remapEndSolution(oldPuzzle)
    for i in range(len(puzzle)):
        if i % theRoot == 0:
            print("")
        print(str(puzzle[i]), end = " ")
        if puzzle[i] < 10:
            print(end = " ")

def printStateOrder(start, end, poppedPuzzles):
    endPuzzle = end
    puzzleCount = 0
    printPuzzle(endPuzzle.puzzle)
    print("\n=====================================================\n")
    while True:
        puzzleCount += 1
        popped = poppedPuzzles[endPuzzle.owner]
        if popped.puzzle == start:
            print(endPuzzle.puzzle)
            print(popped.puzzle)
            break
        print(endPuzzle.puzzle)
        endPuzzle = popped
    print("\n=====================================================")
    print(str(puzzleCount) + " Steps to solve puzzle")

def solvePuzzle(queue, solved):
    global identityCounter
    startingPuzzle = queue[0][2].puzzle.copy()
    heapq.heapify(queue)
    poppedPuzzles = {}
    queuedPuzzles = {}
    while True:
#        input("step?")
        popped = heapq.heappop(queue)
#        print("h = " + str(popped[2].moves))
#        print("g = " + str(popped[2].weight - popped[2].moves))
#        print(popped.puzzle)
#        popped[2].printPuzzleClass()
        if ifSolved(popped[2].puzzle, solved):
            printStateOrder(startingPuzzle, popped[2], poppedPuzzles)
            print(str(len(poppedPuzzles) + len(queuedPuzzles) + len(queue)) + " Total States in Memory")
            print(str(len(poppedPuzzles)) + " States Expanded")
            print(str(calendar.timegm(time.gmtime()) - startTime) + " Seconds")
            exit()
        if not duplicatePuzzle(popped[2], poppedPuzzles):
            currentMoves = []
            currentMoves.append(moveDown(popped[2].puzzle, popped[2].id, popped[2].moves, solved))
            currentMoves.append(moveRight(popped[2].puzzle, popped[2].id, popped[2].moves, solved))
            currentMoves.append(moveLeft(popped[2].puzzle, popped[2].id, popped[2].moves, solved))
            currentMoves.append(moveUp(popped[2].puzzle, popped[2].id, popped[2].moves, solved))
            for i in currentMoves:
                if i:
                    if not duplicatePuzzle(i, poppedPuzzles):
                        if not duplicatePuzzle(i, queuedPuzzles):
                            heapq.heappush(queue, (i.weight, i.id,  i))
                            queuedPuzzles.update( { i.id : i  } )
            poppedPuzzles.update( { popped[2].id : popped[2] } )

puzzleQueue = []
newPuzzle = example
"""don't hard code things"""
solvedPuzzle = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]
puzzleQueue.append((getWeight(newPuzzle, solvedPuzzle, 0), arrayToString(newPuzzle), Puzzle(newPuzzle, getWeight(newPuzzle, solvedPuzzle, 0), arrayToString(newPuzzle), 0)))
solvePuzzle(puzzleQueue, solvedPuzzle)
