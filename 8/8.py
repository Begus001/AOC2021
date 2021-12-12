def A():
    file = open("8/input")
    lines = file.readlines()
    output_vals = list()

    for line in lines:
        for str in line.split(" | ")[1].split(" "):
            output_vals.append(str.replace("\n", ""))

    sum = 0
    for val in output_vals:
        if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            sum += 1

    print("A: %d" % sum)

    file.close()


def B():
    file = open("8/input")
    lines = file.readlines()
    vals = list()

    for i, line in enumerate(lines):
        vals.append(list())
        vals[i].append(list())
        vals[i].append(list())
        line = line.split(" | ")
        for val in line[0].split(" "):
            vals[i][0].append(val.strip("\n"))
        for val in line[1].split(" "):
            vals[i][1].append(val.strip("\n"))

    sum = 0
    for pair in vals:
        cfg = {}
        nums = {}
        while len(nums) < 10:
            for val in pair[0] + pair[1]:
                if len(val) == 2:
                    nums[1] = val
                elif len(val) == 3:
                    nums[7] = val
                elif len(val) == 4:
                    nums[4] = val
                elif len(val) == 7:
                    nums[8] = val
                elif len(val) == 6 and 1 in nums and 4 in nums and (nums[1][0] not in val or nums[1][1] not in val):
                    nums[6] = val
                    cfg[1] = list(set(nums[1]) - set(nums[6]))[0]
                    cfg[2] = nums[1][0] if cfg[1] is not nums[1][0] else nums[1][1]
                elif len(val) == 5 and 1 in nums and nums[1][0] in val and nums[1][1] in val:
                    nums[3] = val
                elif len(val) == 5 and 1 in cfg and cfg[1] in val:
                    nums[2] = val
                elif len(val) == 5 and 2 in cfg and 2 in nums and cfg[2] in val:
                    nums[5] = val
                    cfg[4] = list(
                        set(nums[2]) - set(nums[1]) - set(nums[5]))[0]
                elif len(val) == 6 and 4 in cfg and cfg[4] in val:
                    nums[0] = val
                elif len(val) == 6 and 4 in cfg and cfg[4] not in val:
                    nums[9] = val

        for digitidx, val in enumerate(pair[1]):
            for i in range(10):
                if set(nums[i]) == set(val):
                    sum += i * pow(10,  3 - digitidx)

    print("B: %d" % sum)

    file.close()


if __name__ == "__main__":
    A()
    B()
