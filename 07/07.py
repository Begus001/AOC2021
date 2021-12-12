def A():
    file = open("07/input", "r")
    input = file.readline().split(",")

    positions = list()
    for pos in input:
        positions.append(int(pos))

    min_fuel = 0xFFFFFFFFFFFFFFFF
    for i in range(min(positions), max(positions)):
        sum = 0
        for pos in positions:
            sum += max(pos, i) - min(pos, i)
        min_fuel = min(sum, min_fuel)

    print("A: %d" % (min_fuel))

    file.close()


def B():
    file = open("07/input", "r")
    input = file.readline().split(",")

    positions = list()
    for pos in input:
        positions.append(int(pos))

    min_fuel = 0xFFFFFFFFFFFFFFFF
    for i in range(min(positions), max(positions)):
        sum = 0
        for pos in positions:
            n = max(pos, i) - min(pos, i)
            sum += (n * (n + 1)) / 2
        min_fuel = min(sum, min_fuel)

    print("B: %d" % (min_fuel))

    file.close()


if __name__ == "__main__":
    A()
    B()
