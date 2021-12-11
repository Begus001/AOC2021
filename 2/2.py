def A():
    file = open("2/input", "r")
    lines = file.readlines()
    pos = 0
    depth = 0

    for line in lines:
        split_line = line.split(" ")
        val = int(split_line[1])
        if split_line[0] == "forward":
            pos += val
        elif split_line[0] == "down":
            depth += val
        elif split_line[0] == "up":
            depth -= val
        else:
            print("Something went wrong lol")

    file.close()

    print("A: %d" % (pos * depth))


def B():
    file = open("2/input", "r")
    lines = file.readlines()
    pos = 0
    depth = 0
    aim = 0

    for line in lines:
        split_line = line.split(" ")
        val = int(split_line[1])
        if split_line[0] == "forward":
            pos += val
            depth += val * aim
        elif split_line[0] == "down":
            aim += val
        elif split_line[0] == "up":
            aim -= val
        else:
            print("Something went wrong lol")

    file.close()

    print("B: %d" % (pos * depth))


if __name__ == "__main__":
    A()
    B()
