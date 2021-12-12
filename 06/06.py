def A():
    file = open("06/input")
    init_state_str = file.readline().split(",")
    state = list()
    for str in init_state_str:
        state.append(int(str))

    for day in range(80):
        for i in range(len(state)):
            state[i] -= 1
            if state[i] < 0:
                state[i] = 6
                state.append(8)
    
    print("A: %d" % (len(state)))

    file.close()

def B():
    file = open("06/input")
    init_state_str = file.readline().split(",")
    state = list()
    for str in init_state_str:
        state.append(int(str))

    alt_state = [0] * 9

    for fish in state:
        alt_state[fish] += 1

    for day in range(256):
        new_fish = alt_state[0]
        for i in range(1, len(alt_state)):
            alt_state[i - 1] = alt_state[i]
            alt_state[i] = 0
        alt_state[8] = new_fish
        alt_state[6] += new_fish

    sum = 0
    for i in alt_state:
        sum += i
    print("B: %d" % (sum))

    file.close()


if __name__ == "__main__":
    A()
    B()