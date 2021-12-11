def A():
    file = open("8/input")
    input = file.readlines()
    output_vals = list()

    for line in input:
        for str in line.split(" | ")[1].split(" "):
            output_vals.append(str.replace("\n", ""))
            
    sum = 0
    for val in output_vals:
        if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            sum += 1
    
    print("A: %d" % sum)

    file.close()


def B():
    pass


if __name__ == "__main__":
    A()
    B()