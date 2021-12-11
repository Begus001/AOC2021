def A():
    file = open("1/input", "r")
    lines = file.readlines()
    last_value = 0
    num_increase = 0

    for line in lines:
        if last_value == 0:
            last_value = int(line)
            continue

        if int(line) > last_value:
            num_increase += 1
        last_value = int(line)

    file.close()

    print("A: %d" % num_increase)


def B():
    file = open("1/input", "r")
    lines = file.readlines()
    last_value = 0
    num_increase = 0

    for i in range(len(lines)-2):
        if last_value == 0:
            last_value = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
            continue

        if int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]) > last_value:
            num_increase += 1

        last_value = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])

    file.close()

    print("B: %d" % num_increase)


if __name__ == "__main__":
    A()
    B()
