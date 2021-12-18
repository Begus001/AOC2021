def A():
    file = open("12/input", "r")
    lines = file.read().splitlines()

    points = []
    connections = {}
    paths = set()

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
    exclude = set()

    while len(path) > 0:
        current = path[len(path) - 1]
        while current != "end" and len(path) > 0:
            for p in connections[current]:
                if p == "start":
                    continue
                
                if p not in visited and tuple(path + [p]) not in exclude:
                    if p != "end" and p.islower(): visited.append(p)
                    if p == "end" and tuple(path + ["end"]) in paths: continue
                    path.append(p)
                    break

            if current == path[len(path) - 1]:
                if current.islower() and len(visited) > 0: visited.pop()
                exclude.add(tuple(path))
                path.pop()

            if len(path) > 0: current = path[len(path) - 1]

        if len(path) == 0:
            break

        paths.add(tuple(path))
        path.pop()

    print("A: %d" % len(paths))

    file.close()


def B():
    file = open("12/input", "r")
    lines = file.read().splitlines()

    points = []
    connections = {}
    paths = set()
    small_cave_cnt = {}

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

    for p in points:
        if p.islower() and p != "start" and p != "end": small_cave_cnt[p] = 0

    for c in connections.values():
        if "end" in c:
            c.append(c.pop(c.index("end")))

    path = ["start"]
    current = path[len(path) - 1]
    exclude = set()
    cave_two = False

    while len(path) > 0:
        for p in connections[current]:
            if p == "start":
                continue

            if tuple(path + [p]) not in exclude:
                if p.islower():
                    if p == "end":
                        if tuple(path + [p]) not in paths:
                            path.append(p)
                            break
                        else: break
                    else:
                        if small_cave_cnt[p] == 1 and not cave_two:
                            path.append(p)
                            cave_two = True
                            small_cave_cnt[p] += 1
                            break
                        elif small_cave_cnt[p] == 0:
                            path.append(p)
                            small_cave_cnt[p] += 1
                            break
                else:
                    path.append(p)
                    break
            
        if p == "end":
            paths.add(tuple(path))
            path.pop()
        if current == path[len(path) - 1]:
            if current == "start": break
            exclude.add(tuple(path))
            if current.islower():
                if small_cave_cnt[current] == 2:
                    cave_two = False
                small_cave_cnt[current] -= 1
            path.pop()
            

        current = path[len(path) - 1]

    print("B: %d" % len(paths))

    file.close()


if __name__ == "__main__":
    A()
    B()
