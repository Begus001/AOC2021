def A():
    file = open("4/input", "r")
    lines = file.readlines()

    draws = lines.pop(0).replace("\n", "").split(",")

    # print(lines)
    boards = {}
    marked = {}

    for i in range(len(lines)):
        lines[i] = lines[i].removeprefix(" ").replace("  ", " ").split(" ")

    new_lines = [i for i in lines if "\n" not in i]
    lines = new_lines

    board_index = 0

    while board_index * 5 < len(lines):
        for row in range(5):
            for col in range(5):
                boards[board_index, row, col] = int(
                    lines[board_index * 5 + row][col])
        board_index += 1

    bingo_draw = 0
    bingo_board = 0

    num_boards = int(len(boards) / 25)

    for draw in range(len(draws)):
        for i in range(num_boards):
            for row in range(5):
                for col in range(5):
                    if boards[i, row, col] == int(draws[draw]):
                        marked[i, row, col] = 1

        combo = 0
        bingo = False

        for i in range(num_boards):
            for row in range(5):
                for col in range(5):
                    if (i, row, col) in marked:
                        combo += 1
                        if combo == 5:
                            print("row bingo at draw %d(%d) board %d row %d col %d" % (int(draw), int(draws[draw]), i, row, col))
                            bingo_draw = int(draws[draw])
                            bingo_board = i
                            bingo = True
                            break
                    if bingo:
                        break
                combo = 0
                if bingo:
                    break
            if bingo:
                break
        if bingo:
            break
        
        combo = 0

        for i in range(num_boards):
            for col in range(5):
                for row in range(5):
                    if (i, row, col) in marked:
                        combo += 1
                        if combo == 5:
                            print("col bingo at draw %d(%d) board %d row %d col %d" % (int(draw), int(draws[draw]), i, row, col))
                            bingo = True
                            bingo_draw = int(draws[draw])
                            bingo_board = i
                            break
                    if bingo:
                        break
                combo = 0
                if bingo:
                    break
            if bingo:
                break
        if bingo:
            break
    
    print("bingo board %d bingo draw %d" % (bingo_board, bingo_draw))

    sum = 0
    mul = 0
    
    for row in range(5):
        for col in range(5):
            if (i, row, col) not in marked:
                sum += boards[i, row, col]

    mul = sum * bingo_draw
    print("sum %d mul %d" % (sum, mul))


    file.close()


def B():
    file = open("4/input", "r")
    lines = file.readlines()

    draws = lines.pop(0).replace("\n", "").split(",")

    # print(lines)
    boards = {}
    marked = {}

    for i in range(len(lines)):
        lines[i] = lines[i].removeprefix(" ").replace("  ", " ").split(" ")

    new_lines = [i for i in lines if "\n" not in i]
    lines = new_lines

    board_index = 0

    while board_index * 5 < len(lines):
        for row in range(5):
            for col in range(5):
                boards[board_index, row, col] = int(
                    lines[board_index * 5 + row][col])
        board_index += 1

    bingo_draw = 0
    bingo_board = 0

    boards_won = []
    num_boards = int(len(boards) / 25)

    for draw in range(len(draws)):
        for i in range(num_boards):
            for row in range(5):
                for col in range(5):
                    if boards[i, row, col] == int(draws[draw]):
                        marked[i, row, col] = 1

        combo = 0
        bingo = False

        for i in range(num_boards):
            for row in range(5):
                for col in range(5):
                    if (i, row, col) in marked:
                        combo += 1
                        if combo == 5:
                            # print("row bingo at draw %d(%d) board %d row %d col %d" % (int(draw), int(draws[draw]), i, row, col))
                            if i not in boards_won:
                                boards_won.append(i)
                            # print("boards left: %d" % (num_boards - len(boards_won)))
                            if len(boards_won) == num_boards:
                                bingo_draw = int(draws[draw])
                                bingo_board = i
                                bingo = True
                                break
                    if bingo:
                        break
                combo = 0
                if bingo:
                    break
            if bingo:
                break
        if bingo:
            break
        
        combo = 0

        for i in range(num_boards):
            for col in range(5):
                for row in range(5):
                    if (i, row, col) in marked:
                        combo += 1
                        if combo == 5:
                            # print("col bingo at draw %d(%d) board %d row %d col %d" % (int(draw), int(draws[draw]), i, row, col))
                            if i not in boards_won:
                                boards_won.append(i)
                            # print("boards left: %d" % (num_boards - len(boards_won)))
                            if len(boards_won) == num_boards:
                                bingo = True
                                bingo_draw = int(draws[draw])
                                bingo_board = i
                            break
                    if bingo:
                        break
                combo = 0
                if bingo:
                    break
            if bingo:
                break
        if bingo:
            break
    
    print("bingo board %d bingo draw %d" % (bingo_board, bingo_draw))

    sum = 0
    mul = 0
    for row in range(5):
        for col in range(5):
            if (i, row, col) not in marked:
                sum += boards[i, row, col]

    mul = sum * bingo_draw
    print("sum %d mul %d" % (sum, mul))


    file.close()


if __name__ == "__main__":
    A()
    B()
