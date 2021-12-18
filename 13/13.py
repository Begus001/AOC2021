def A():
    file = open("13/input", "r")
    lines = file.read().splitlines()

    dots = []
    folds = []

    for line in lines:
        if line == "": continue
        if line.startswith("fold"):
            line = line.strip("fold along ").split("=")
            line[1] = int(line[1])
            folds.append(line)
        else:
            line = line.split(",")
            dots.append((int(line[0]), int(line[1])))

    for i, fold in enumerate(folds):
        if i == 1: break
        foldpos = fold[1]
        if fold[0] == "x":
            for i, (x, y) in enumerate(dots):
                if x > foldpos:
                    dots[i] = (foldpos - (x - foldpos), y)
        else:
            for i, (x, y) in enumerate(dots):
                if y > foldpos:
                    dots[i] = (x, foldpos - (y - foldpos))
    
    dots = list(dict.fromkeys(dots))
    
    print("A: %d" % len(dots))

    file.close()


def B():
    file = open("13/input", "r")
    lines = file.read().splitlines()

    dots = []
    folds = []

    for line in lines:
        if line == "": continue
        if line.startswith("fold"):
            line = line.strip("fold along ").split("=")
            line[1] = int(line[1])
            folds.append(line)
        else:
            line = line.split(",")
            dots.append((int(line[0]), int(line[1])))

    for i, fold in enumerate(folds):
        foldpos = fold[1]
        if fold[0] == "x":
            for i, (x, y) in enumerate(dots):
                if x > foldpos:
                    dots[i] = (foldpos - (x - foldpos), y)
        else:
            for i, (x, y) in enumerate(dots):
                if y > foldpos:
                    dots[i] = (x, foldpos - (y - foldpos))


    dots = list(dict.fromkeys(dots))
    print("B:")
    
    maxx = 0
    maxy = 0
    for x, y in dots:
        maxx = x if x > maxx else maxx
        maxy = y if y > maxy else maxy
    
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            print("#" if (x, y) in dots else ".", end="")
        print()

    file.close()


if __name__ == "__main__":
    A()
    B()