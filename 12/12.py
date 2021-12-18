def A():
    file = open("12/input", "r")
    lines = file.read().splitlines()

    points = []
    connections = {}
    paths = []

    for line in lines:
        line = line.split("-")
        for i in range(2):
            if line[i] not in points:
                points.append(line[i])
                connections[line[i]] = []

    for line in lines:
        line = line.split("-")
        connections[line[0]].append(line[1])
        connections[line[1]].append(line[0])

    path = ["start"]
    current = path[len(path) - 1]
    visited = []
    exclude = []

    while len(path) > 0:
        current = path[len(path) - 1]
        while current != "end" and len(path) > 0:
            for p in connections[current]:
                if p == "start":
                    continue

                if p not in visited and path + [p] not in exclude:
                    if p != "end" and p.islower(): visited.append(p)
                    if p == "end" and path + ["end"] in paths: continue
                    path.append(p)
                    break

            if current == path[len(path) - 1]:
                if current.islower() and len(visited) > 0: visited.pop()
                exclude.append(path.copy())
                path.pop()

            if len(path) > 0: current = path[len(path) - 1]

        if len(path) == 0:
            break

        paths.append(path.copy())
        path.pop()

    print("A: %d" % len(paths))

    file.close()


def B():
    pass


if __name__ == "__main__":
    A()
    B()
