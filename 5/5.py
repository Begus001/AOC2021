def A():
    file = open("5/input", "r")
    lines = file.readlines()
    coordinates = {}
    diagram = {}

    for i, line in enumerate(lines):
        line = line.split(" -> ")
        for j in range(2):
            for k in range(2):
                coordinates[i, j, k] = int(line[j].split(",")[k])

    num_lines = int(len(coordinates) / 4)

    for i in range(num_lines):
        x1 = coordinates[i, 0, 0]
        y1 = coordinates[i, 0, 1]
        x2 = coordinates[i, 1, 0]
        y2 = coordinates[i, 1, 1]

        if x1 != x2 and y1 != y2:
            # print("continue")
            continue
        elif x1 == x2:
            # print("x1 == x2")
            for pos in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, pos) in diagram:
                    diagram[x1, pos] += 1
                else:
                    diagram[x1, pos] = 1
        elif y1 == y2:
            # print("y1 == y2")
            for pos in range(min(x1, x2), max(x1, x2) + 1):
                if (pos, y1) in diagram:
                    diagram[pos, y1] += 1
                else:
                    diagram[pos, y1] = 1
        else:
            print("unreachable")

        # for y in range(10):
        #     for x in range(10):
        #         if (x, y) in diagram:
        #             print(diagram[x, y], end=" ")
        #         else:
        #             print(".", end=" ")
        #     print("")

    # for y in range(10):
    #     for x in range(10):
    #         if (x, y) in diagram:
    #             print(diagram[x, y], end=" ")
    #         else:
    #             print(".", end=" ")
    #     print("")

    num_overlap = 0
    for i in diagram.items():
        if i[1] >= 2:
            num_overlap += 1

    print("A: %d" % num_overlap)

    file.close()


def B():
    file = open("5/input", "r")
    lines = file.readlines()
    coordinates = {}
    diagram = {}

    for i, line in enumerate(lines):
        line = line.split(" -> ")
        for j in range(2):
            for k in range(2):
                coordinates[i, j, k] = int(line[j].split(",")[k])

    num_lines = int(len(coordinates) / 4)

    for i in range(num_lines):
        x1 = coordinates[i, 0, 0]
        y1 = coordinates[i, 0, 1]
        x2 = coordinates[i, 1, 0]
        y2 = coordinates[i, 1, 1]
        # if input("next %d %d,%d -> %d,%d" % (i, x1, y1, x2, y2)) == "q":
        #     exit(0)
        if x1 != x2 and y1 != y2:
            # print("continue")
            if max(x1, x2) - min(x1, x2) == max(y1, y2) - min(y1, y2):
                # print("diag")
                if x1 > x2:
                    xstep = -1
                else:
                    xstep = 1
                if y1 > y2:
                    ystep = -1
                else:
                    ystep = 1
                # print("xstep %d ystep %d" % (xstep, ystep))
                y = y1
                for x in range(x1, x2 + xstep, xstep):
                    # print("setting %d,%d" % (x, y))
                    if (x, y) in diagram:
                        diagram[x, y] += 1
                    else:
                        diagram[x, y] = 1
                    y += ystep
            else:
                continue
        elif x1 == x2:
            # print("x1 == x2")
            for pos in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, pos) in diagram:
                    diagram[x1, pos] += 1
                else:
                    diagram[x1, pos] = 1
        elif y1 == y2:
            # print("y1 == y2")
            for pos in range(min(x1, x2), max(x1, x2) + 1):
                if (pos, y1) in diagram:
                    diagram[pos, y1] += 1
                else:
                    diagram[pos, y1] = 1
        else:
            print("unreachable")

        # for y in range(10):
        #     for x in range(10):
        #         if (x, y) in diagram:
        #             print(diagram[x, y], end=" ")
        #         else:
        #             print(".", end=" ")
        #     print("")

    # for y in range(10):
    #     for x in range(10):
    #         if (x, y) in diagram:
    #             print(diagram[x, y], end=" ")
    #         else:
    #             print(".", end=" ")
    #     print("")

    num_overlap = 0
    for i in diagram.items():
        if i[1] >= 2:
            num_overlap += 1

    print("B: %d" % num_overlap)

    file.close()


if __name__ == "__main__":
    A()
    B()
