def A():
    file = open("3/input", "r")
    lines = file.readlines()
    gamma = ""
    epsilon = ""
    ones_occurrence = [0] * (len(lines[0]) - 1)

    for line in lines:
        line = line.replace('\n', '')
        for i in range(len(line)):
            if line[i] == '1':
                ones_occurrence[i] += 1

    for i in ones_occurrence:
        if i > len(lines) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    file.close()
    print("A: %d" % (int(gamma, 2) * int(epsilon, 2)))


def B():
    file = open("3/input", "r")
    lines = file.readlines()

    for bit in range(len(lines[0])):
        if len(lines) <= 1:
            break
        ones = 0
        zeros = 0
        for line in lines:
            line = line.replace("\n", "")
            if line[bit] == "1":
                ones += 1
            else:
                zeros += 1

        if ones >= zeros:
            keep = "1"
        else:
            keep = "0"

        new_lines = list()
        for line in lines:
            if line[bit] == keep:
                new_lines.append(line)

        lines = new_lines

    oxy = int(lines[0], 2)
    file.seek(0)
    lines = file.readlines()

    for bit in range(len(lines[0])):
        if len(lines) <= 1:
            break
        ones = 0
        zeros = 0
        for line in lines:
            line = line.replace("\n", "")
            if line[bit] == "1":
                ones += 1
            else:
                zeros += 1

        if ones < zeros:
            keep = "1"
        else:
            keep = "0"

        new_lines = list()
        for line in lines:
            if line[bit] == keep:
                new_lines.append(line)

        lines = new_lines

    co2 = int(lines[0], 2)

    print("B: %d" % (oxy * co2))

    file.close()


if __name__ == "__main__":
    A()
    B()
