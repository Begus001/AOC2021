def A():
    file = open("09/input", "r")
    lines = file.readlines()
    hmap = list(list())
    lowpoints = {}

    for i, line in enumerate(lines):
        hmap.append(list())
        for c in line.strip("\n"):
            hmap[i].append(int(c))

    for i, row in enumerate(hmap):
        for j, val in enumerate(row):
            if i > 0 and hmap[i - 1][j] <= val:
                continue
            if i < len(hmap) - 1 and hmap[i + 1][j] <= val:
                continue
            if j > 0 and hmap[i][j - 1] <= val:
                continue
            if j < len(row) - 1 and hmap[i][j + 1] <= val:
                continue
            lowpoints[i, j] = 1

    sum = 0
    for i, row in enumerate(hmap):
        for j, val in enumerate(row):
            if (i, j) in lowpoints:
                sum += hmap[i][j] + 1

    print("A: %d" % sum)

    file.close()


def B():
    file = open("09/input", "r")
    lines = file.readlines()
    hmap = list(list())
    basins = {}

    for i, line in enumerate(lines):
        hmap.append(list())
        for c in line.strip("\n"):
            hmap[i].append(int(c))

    for y, row in enumerate(hmap):
        for x, val in enumerate(row):
            if y > 0 and hmap[y - 1][x] <= val:
                continue
            if y < len(hmap) - 1 and hmap[y + 1][x] <= val:
                continue
            if x > 0 and hmap[y][x - 1] <= val:
                continue
            if x < len(row) - 1 and hmap[y][x + 1] <= val:
                continue
            basins[y, x] = 1

    todo = list()
    done = list()
    for (y, x) in basins:
        todo.clear()
        if y > 0 and hmap[y - 1][x] != 9:
            todo.append((y - 1, x))
        if y < len(hmap) - 1 and hmap[y + 1][x] != 9:
            todo.append((y + 1, x))
        if x > 0 and hmap[y][x - 1] != 9:
            todo.append((y, x - 1))
        if x < len(hmap[y]) - 1 and hmap[y][x + 1] != 9:
            todo.append((y, x + 1))
        done.append((y, x))
        import os
        while len(todo) > 0:
            cy, cx = todo.pop()
            if (cy, cx) in done or hmap[cy][cx] == 9:
                done.append((cy, cx))
                continue
            basins[y, x] += 1
            if cy > 0 and hmap[cy - 1][cx] != 9:
                todo.append((cy - 1, cx))
            if cy < len(hmap) - 1 and hmap[cy + 1][cx] != 9:
                todo.append((cy + 1, cx))
            if cx > 0 and hmap[cy][cx - 1] != 9:
                todo.append((cy, cx - 1))
            if cx < len(hmap[cy]) - 1 and hmap[cy][cx + 1] != 9:
                todo.append((cy, cx + 1))
            done.append((cy, cx))

    result = sorted(basins.values())

    print("B: %d" % (result.pop() * result.pop() * result.pop()))

    file.close()


if __name__ == "__main__":
    A()
    B()
