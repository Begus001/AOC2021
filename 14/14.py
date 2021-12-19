from os import replace


def A():
    file = open("14/input", "r")
    lines = file.read().splitlines()

    rules = []
    template = lines[0]

    for line in lines[2:]:
        line = line.split(" -> ")
        rules.append((line[0], line[1]))

    insertrules = {}
    for _ in range(10):
        insertrules.clear()
        for pair, char in rules:
            for i in range(len(template) - 1):
                if template[i:i+2] == pair:
                    insertrules[i + 1] = char

        counter = 0
        for index, char in sorted(insertrules.items()):
            template = template[:index + counter] + \
                char + template[index + counter:]
            counter += 1
        dic = {}
        for i in range(len(template) - 1):
            if template[i:i+2] not in dic:
                dic[template[i:i+2]] = 1
            else:
                dic[template[i:i+2]] += 1

    occur = {}
    for c in template:
        if c in occur:
            occur[c] += 1
        else:
            occur[c] = 1

    print("A: %d" % (max(occur.values()) - min(occur.values())))

    file.close()


def B():
    file = open("14/input", "r")
    lines = file.read().splitlines()

    rules = {}
    template = lines[0]

    for line in lines[2:]:
        line = line.split(" -> ")
        rules[line[0]] = line[1]

    polymer = {}

    for j in range(len(template) - 1):
        if template[j:j+2] in polymer:
            polymer[template[j:j+2]] += 1
        else:
            polymer[template[j:j+2]] = 1

    for _ in range(40):
        polymernew = polymer.copy()
        for key in polymer.keys():
            if polymer[key] > 0 and key in rules:
                new = [key[0] + rules[key], rules[key] + key[1]]
                for n in new:
                    if n in polymernew:
                        polymernew[n] += polymer[key]
                    else:
                        polymernew[n] = polymer[key]
                polymernew[key] -= polymer[key]
        polymer = polymernew.copy()

    occur = {}
    for key, val in polymer.items():
        if key[1] in occur:
            occur[key[1]] += val
        else:
            occur[key[1]] = val

    occur[template[0]] += 1

    print("B: %d" % (max(occur.values()) - min(occur.values())))

    file.close()


if __name__ == "__main__":
    A()
    B()
