import random

SIZE = 5
MINES = 6

def create_board():
    return [["■" for b in range(SIZE)] for b in range(SIZE)]

def place_mines(board):
    mines = set()
    while len(mines) < MINES:
        x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        mines.add((x, y))
    return mines

def count_adjacent(mines, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (x+dx, y+dy) in mines and (dx != 0 or dy != 0):
                count += 1
    return count

def reveal(board, mines, x, y):
    if (x, y) in mines:
        print("💥 Бомба! Игра окончена.")
        return False
    board[x][y] = str(count_adjacent(mines, x, y))
    return True

board = create_board()
mines = place_mines(board)

while True:
    for row in board:
        print(" ".join(row))
    try:
        x, y = map(int, input("Введите X Y: ").split())
    except:
        continue
    if not reveal(board, mines, x, y):
        break
