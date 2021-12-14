def A():
    file = open("11/input", "r")
    lines = file.read().splitlines()

    octopi = list()
    for y, line in enumerate(lines):
        octopi.append(list())
        for x, val in enumerate(line):
            octopi[y].append(int(val))
                

    flash = list()
    flashed = list()
    next_flash = list()

    total = 0

    for step in range(101):
        total += len(flashed)
        flashed.clear()
        flash.clear()
        next_flash.clear()
        for y, row in enumerate(octopi):
            for x, o in enumerate(row):
                octopi[y][x] += 1
                if octopi[y][x] >= 10:
                    octopi[y][x] = 0
                    flash.append((y, x))

        while len(flash) > 0:
            for (y, x) in flash:
                if (y, x) not in flashed:
                    flashed.append((y, x))
                    for dy in range(-1, 2):
                        if y + dy < 0 or y + dy >= len(octopi): continue
                        for dx in range(-1, 2):
                            if dy == 0 and dx == 0: continue
                            if x + dx < 0 or x + dx >= len(octopi[y]): continue
                            octopi[y + dy][x + dx] += 1
                            if octopi[y + dy][x + dx] >= 10:
                                octopi[y + dy][x + dx] = 0
                                next_flash.append((y + dy, x + dx))
                
                for (y, x) in flashed:
                        octopi[y][x] = 0
            flash = next_flash.copy()
            next_flash.clear()

    print("A: %d" % total)



    file.close()


def B():
    file = open("11/input", "r")
    lines = file.read().splitlines()

    octopi = list()
    for y, line in enumerate(lines):
        octopi.append(list())
        for x, val in enumerate(line):
            octopi[y].append(int(val))
                

    flash = list()
    flashed = list()
    next_flash = list()

    step = 0

    while True:
        step += 1
        flashed.clear()
        flash.clear()
        next_flash.clear()
        for y, row in enumerate(octopi):
            for x, o in enumerate(row):
                octopi[y][x] += 1
                if octopi[y][x] >= 10:
                    octopi[y][x] = 0
                    flash.append((y, x))

        while len(flash) > 0:
            for (y, x) in flash:
                if (y, x) not in flashed:
                    flashed.append((y, x))
                    for dy in range(-1, 2):
                        if y + dy < 0 or y + dy >= len(octopi): continue
                        for dx in range(-1, 2):
                            if dy == 0 and dx == 0: continue
                            if x + dx < 0 or x + dx >= len(octopi[y]): continue
                            octopi[y + dy][x + dx] += 1
                            if octopi[y + dy][x + dx] >= 10:
                                octopi[y + dy][x + dx] = 0
                                next_flash.append((y + dy, x + dx))
                
                for (y, x) in flashed:
                        octopi[y][x] = 0
            flash = next_flash.copy()
            next_flash.clear()

        if len(flashed) == len(octopi) * len(octopi[0]):
            break

    print("B: %d" % step)



    file.close()


if __name__ == "__main__":
    A()
    B()
