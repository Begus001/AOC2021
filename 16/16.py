def A():
    file = open("16/input", "r")
    line = file.readline()

    binary = ""

    for c in line:
        binary += bin(int(c, 16))[2:].zfill(4)

    i = 0
    current = None
    pkts = [{"ltid": -1, "val": -1, "done": 0}]
    pkti = [1]

    while i < len(binary):
        current = pkts
        if len(pkti) > 1:
            for j in pkti[:len(pkti)-1]:
                current = current[j]["sub"]

        curi = pkti[len(pkti) - 1]
        current.append({})

        if i >= len(binary): break
        current[curi]["ver"] = int(binary[i:i+3], 2)
        i += 3

        if i >= len(binary): break
        current[curi]["typ"] = int(binary[i:i+3], 2)
        i += 3

        if i >= len(binary): break
        if current[curi]["typ"] != 4:
            current[curi]["sub"] = []
            current[curi]["sub"].append({})
            current[curi]["sub"][0]["ltid"] = int(binary[i], 2)
            i += 1

            if i >= len(binary): break
            if current[curi]["sub"][0]["ltid"] == 0:
                current[curi]["sub"][0]["val"] = int(binary[i:i+15], 2)
                i += 15
            else:
                current[curi]["sub"][0]["val"] = int(binary[i:i+11], 2)
                i += 11

            if i >= len(binary): break
            current[curi]["sub"][0]["done"] = 0
            pkti.append(1)
        else:
            ltid = current[0]["ltid"]
            val = current[0]["val"]
            current[curi]["dat"] = ""
            current[0]["done"] += 6 if ltid == 0 else 0
            while True:
                if binary[i] == "1":
                    i += 1
                    if i >= len(binary): break
                    current[curi]["dat"] += binary[i:i+4]
                    i += 4
                    if i >= len(binary): break
                    if ltid == 0: current[0]["done"] += 5
                    continue
                else:
                    i += 1
                    if i >= len(binary): break
                    current[curi]["dat"] += binary[i:i+4]
                    i += 4
                    current[curi]["dat"] = int(current[curi]["dat"], 2)
                    if ltid == 0: current[0]["done"] += 5
                    else: current[0]["done"] += 1
                    if i >= len(binary): break
                    break
            if current[0]["done"] >= val:
                pkti.pop()

            pkti[len(pkti) - 1] += 1

    versum = 0
    todo = [pkts]
    while len(todo) > 0:
        current = todo.pop()
        for i in current:
            if "ver" in i:
                versum += i["ver"]
            if "sub" in i:
                todo.append(i["sub"])

    print("A: %d" % (versum))

    file.close()


def B():
    file = open("16/input", "r")
    line = file.readline()

    binary = ""

    for c in line:
        binary += bin(int(c, 16))[2:].zfill(4)

    # my own example
    # binary = "10000000000000011011011001111000000000100100001000000000100101000000110010000011110001100000000010000100000100101000001011110000100"
    
    pkts = [""]
    pkti = []
    sublen = []
    sublentyp = []
    sublendone = []
    current = pkts
    i = 0
    while True:

        if len(sublentyp) > 0:
            if sublendone[len(sublendone)-1] >= sublen[len(sublen)-1]:
                if len(pkti) > 0:
                    pkti.pop()
                    sublen.pop()
                    sublentyp.pop()
                    sublendone.pop()
                    if len(sublentyp) > 0 and sublentyp[len(sublentyp)-1] == 1: sublendone[len(sublendone)-1] += 1
                    continue
                else:
                    break
        if i >= len(binary): break

        current = pkts
        if len(pkti) > 0:
            for j in pkti:
                current = current[j]
        
        i += 3  # skip ver
        if i >= len(binary): break
        
        typ = int(binary[i:i+3], 2)
        i += 3
        if i >= len(binary): break
        for j, _ in enumerate(sublendone[:len(sublendone)]):
                if sublentyp[j] == 0: sublendone[j] += 6

        if typ == 4:
            dat = ""
            while True:
                if binary[i] == "1":
                    i += 1
                    if i >= len(binary): break
                    dat += binary[i:i+4]
                    i += 4
                    for j, _ in enumerate(sublendone[:len(sublendone)]):
                        if sublentyp[j] == 0: sublendone[j] += 5
                    if i >= len(binary): break
                else:
                    i += 1
                    if i >= len(binary): break
                    dat += binary[i:i+4]
                    i += 4
                    dat = int(dat, 2)
                    for j, _ in enumerate(sublendone[:len(sublendone)]):
                        if sublentyp[j] == 0: sublendone[j] += 5
                    if i >= len(binary): break
                    break

            current.append(dat)
            if len(sublentyp) > 0 and sublentyp[len(sublentyp)-1] == 1: sublendone[len(sublendone)-1] += 1
        else:
            current.append([])
            pkti.append(len(current) - 1)
            sublentyp.append(int(binary[i]))
            sublendone.append(0)
            if binary[i] == "0":
                i += 1
                if i >= len(binary): break
                for j, _ in enumerate(sublendone[:len(sublendone)-1]):
                        if sublentyp[j] == 0: sublendone[j] += 16
                sublen.append(int(binary[i:i+15], 2))
                i += 15
                if i >= len(binary): break
            else:
                i += 1
                if i >= len(binary): break
                for j, _ in enumerate(sublendone[:len(sublendone)-1]):
                        if sublentyp[j] == 0: sublendone[j] += 12
                sublen.append(int(binary[i:i+11], 2))
                i += 11
                if i >= len(binary): break
            if typ == 0:
                current[len(current)-1].append("+")
            elif typ == 1:
                current[len(current)-1].append("*")
            elif typ == 2:
                current[len(current)-1].append("min")
            elif typ == 3:  
                current[len(current)-1].append("max")
            elif typ == 5:
                current[len(current)-1].append(">")
            elif typ == 6:
                current[len(current)-1].append("<")
            elif typ == 7:
                current[len(current)-1].append("=")
        
    parent = None
    while True:
        current = pkts
        while True:
            foundlist = False
            for item in current:
                if type(item) == list:
                    foundlist = True
                    parent = current
                    current = item
                    break
            if not foundlist:
                break
        
        stack = []
        while len(current) > 1:
            stack.append(current.pop())
        op = current.pop()

        result = -1

        if op == "":
            break
        elif op == "+":
            result = sum(stack)
        elif op == "*":
            product = 1
            for val in stack:
                product *= val
            result = product
        elif op == "min":
            result = min(stack)
        elif op == "max":
            result = max(stack)
        elif op == ">":
            result = int(stack[1] > stack[0])
        elif op == "<":
            result = int(stack[1] < stack[0])
        elif op == "=":
            result = int(stack[0] == stack[1])
        
        parent[parent.index([])] = result

    print("B: %d" % (stack[0]))

    file.close()


if __name__ == "__main__":
    A()
    B()
