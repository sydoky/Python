import random
fields = ["K", "Q", "Q", "Q", "Q", "Q"]

#board = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", \
#         "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
board = []
for n in range(8):
    row = []
    for c in range(8):
        row.append(".")
    board.append(row)

i = 0
l = len(fields)
while i < l:
    x = random.randint(0, 7)  # random is object like
    y = random.randint(0, 7)
    if board[y][x] != ".":  # we use [] index , list inside of list, to target
        continue
    board[y][x] = fields.pop()
    i += 1
for row in range(8):
    for colon in range(8):
        print(board[row][colon], end=" ")
    print()




