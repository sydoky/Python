'''board = []
for n in range(8):
    row = []
    for l in range(8):
        if (n + l) % 2 == 0:
            row.append("A")
        else:
            row.append("B")
    board.append(row)
for row in board:
    for l in row:
        print(l, end=" ")

    print()'''

board = []
for n in range(8):
    row = []
    for l in range(8):
        if (n + l) % 2 == 0:
            row.append("A")
        else:
            row.append("B")
    board.append(row)
for row in board:
    for l in row:
        print(l, end=" ")

    print()