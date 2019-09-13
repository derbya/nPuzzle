
def puzzleToPrettyString(puzzle, prevPuzzle, numWidth):
    numWidth = 2
    strPuzzle = []
    for i in range(0, len(puzzle)):
        if puzzle[i] == 0:
            s = numWidth * " "
        else:
            s = str(puzzle[i])
            s = (numWidth - len(s)) * " " + s
            if prevPuzzle and puzzle[i] != prevPuzzle[i]:
                s = "\u001b[7m" + s + "\u001b[0m"
            else:
                s = "\u001b[4m" + s + "\u001b[0m"
        strPuzzle.append(s)
    lines = []
    for y in range(0, 16, 4):
        lines.append("[ " + " ".join(strPuzzle[y : y + 4]) + " ]")
    return lines

def prettyPrintStateOrder(start, end, poppedPuzzles):
    solution = [end.puzzle]
    while end.puzzle != start:
        end = poppedPuzzles[end.owner]
        solution.append(end.puzzle)
    print("\n=====================================================\n")
    numWidth = len(str(16 - 1))
    puzzlePrintWidth = 4 * numWidth + 7
    solutionStrings = []
    for i in range(0, len(solution)):
        prev = solution[i - 1] if i > 0 else None
        solutionStrings.append(puzzleToPrettyString(solution[i], prev, numWidth))
    termHeight, termWidth = os.popen('stty size', 'r').read().split()
    puzzlesPerRow = int((int(termWidth) - 3) / (puzzlePrintWidth + 3))
    for y in range(0, len(solution), puzzlesPerRow):
        for i in range(0, 4):
            row = solutionStrings[y : y + puzzlesPerRow]
            print("   ".join([r[i] for r in row]))
        print()
    print("\n=====================================================")
    print(str(len(solution) - 1) + " Steps to solve puzzle")

