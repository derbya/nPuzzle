import math

area = 4
width = 2
height = 2

tab = []
for i in range(area):
    x = (i % width)
    y = int(i / width)
    if x >= y:
        depth = min(y, width - 1 - x)
        offset = (x - depth) + (y - depth)
    else:
        depth = min(x + 1, height - y)
        offset = (depth - x - 1) + (depth - y - 1)
    f = (width - 2 * depth)
    tab.append(area - f * f + offset)
print(tab)
for y in range(height):
    for x in range(width):
        t = tab[width * y + x]
        if t < 10:
            print("   " + str(t), end="")
        elif t < 100:
            print("  " + str(t), end="")
        else:
            print(" " + str(t), end="")
    print()
