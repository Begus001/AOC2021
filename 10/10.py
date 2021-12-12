def A():
    file = open("10/input", "r")
    lines = file.read().splitlines()

    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    state = []
    illegal = []

    for i, line in enumerate(lines):
        state.clear()
        for c in line:
            if c in brackets.keys():
                state.append(brackets[c])
                continue
            pop = state.pop()
            if pop != c:
                illegal.append(c)
                continue
    result = 0
    for b in illegal:
        result += points[b]

    print("A: %d" % result)
    file.close()


def B():
    file = open("10/input", "r")
    lines = file.read().splitlines()

    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    state = []
    scores = []
    new_lines = []

    for i, line in enumerate(lines):
        state.clear()
        corrupted = False
        for j, c in enumerate(line):
            if c in brackets.keys():
                state.append(brackets[c])
            elif state.pop() != c: corrupted = True
                
        if not corrupted:
            new_lines.append(line)
    
    lines = new_lines

    for i, line in enumerate(lines):
        state.clear()
        scores.append(0)
        for j, c in enumerate(line):
            if c in brackets.keys():
                state.append(brackets[c])
            else: state.pop()
            if j >= len(line) - 1:
                if len(state) > 0:
                    for bracket in reversed(state):
                        scores[i] *= 5
                        scores[i] += points[bracket]
                break

    sorted_scores = list(sorted(scores))

    print("B: %d" % list(sorted(scores))[int(len(scores) / 2)])
    file.close()


if __name__ == "__main__":
    A()
    B()
