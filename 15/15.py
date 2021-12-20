def A():
    file = open("15/input", "r")
    lines = file.read().splitlines()

    map = []

    for y, line in enumerate(lines):
        map.append([])
        for c in line:
            map[y].append(int(c))

    mapsize = len(map)
    dest = (mapsize - 1, mapsize - 1)
    unvisited = {}
    visited = {}
    for y, row in enumerate(map):
        for x, val in enumerate(row):
            unvisited[y, x] = 0xFFFFFFFF

    unvisited[0, 0] = 0
    smalls = {}

    y, x = current = (0, 0)
    while True:
        for dxy in [-1, 1]:
            if (y + dxy, x) in unvisited:
                unvisited[y + dxy, x] = min(unvisited[y + dxy, x], unvisited[current] + map[y + dxy][x])
                smalls[y + dxy, x] = unvisited[y + dxy, x]
            if (y, x + dxy) in unvisited:
                unvisited[y, x + dxy] = min(unvisited[y, x + dxy], unvisited[current] + map[y][x + dxy])
                smalls[y, x + dxy] = unvisited[y, x + dxy]
        visited[current] = unvisited[current]
        unvisited.pop(current)
        if current in smalls:
            smalls.pop(current)
        if dest in visited:
            break

        y, x = current = min(smalls, key=smalls.get)

    print("A: %d" % (visited[dest]))

    file.close()


def B():
    file = open("15/input", "r")
    lines = file.read().splitlines()

    map = []
    for wrapy in range(5):
        for y, line in enumerate(lines):
            map.append([])
            for wrapx in range(5):
                for c in line:
                    cint = int(c) + wrapx + wrapy
                    if cint > 9:
                        cint -= 9
                    map[y + wrapy * len(lines)].append(cint)

    mapsize = len(map)
    dest = (mapsize - 1, mapsize - 1)
    unvisited = {}
    visited = {}
    nodes = {}
    for y, row in enumerate(map):
        for x, val in enumerate(row):
            unvisited[y, x] = 0xFFFFFFFF
            nodes[y, x] = False

    unvisited[0, 0] = 0
    smalls = {}

    import time
    y, x = current = (0, 0)
    while True:
        for dxy in [-1, 1]:
            if y + dxy >= 0 and y + dxy < mapsize and not nodes[y + dxy, x]:
                unvisited[y + dxy, x] = min(unvisited[y + dxy, x], unvisited[current] + map[y + dxy][x])
                smalls[y + dxy, x] = unvisited[y + dxy, x]
            if x + dxy >= 0 and x + dxy < mapsize and not nodes[y, x + dxy]:
                unvisited[y, x + dxy] = min(unvisited[y, x + dxy], unvisited[current] + map[y][x + dxy])
                smalls[y, x + dxy] = unvisited[y, x + dxy]
        
        visited[current] = unvisited[current]
        nodes[current] = True
        unvisited.pop(current)
        if current in smalls:
            smalls.pop(current)

        if dest in visited:
            break

        y, x = current = min(smalls, key=smalls.get)

    print("B: %d" % (visited[dest]))

    file.close()


if __name__ == "__main__":
    A()
    B()
