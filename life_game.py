import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def display_cells( input_cells ):
    for _ in input_cells:
        print(*_, sep="")
    print()


def copy_cells( input_cells ):
    res = [_[::1] for _ in input_cells]
    return res


h = 8
w = 8
dead = 0
alive = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
cells = [[dead for _ in range(w)] for _ in range(h)]
#  cells[1][0], cells[1][1], cells[1][2] = alive, alive, alive

cells[0][3], cells[0][4] = alive, alive
cells[1][2], cells[1][5] = alive, alive
cells[2][1], cells[2][6] = alive, alive
cells[3][0], cells[3][7] = alive, alive
cells[4][0], cells[4][7] = alive, alive
cells[5][1], cells[5][6] = alive, alive
cells[6][2], cells[6][5] = alive, alive
cells[7][3], cells[7][4] = alive, alive

display_cells(cells)
cnt = 0
while cnt != 10:
    new_cells = copy_cells(cells)
    for i in range(h):  # y
        for j in range(w):  # x
            temp = 0
            if cells[i][j] == dead:
                for x, y in direction:
                    nx, ny = x + j, y + i
                    if not 0 <= nx < w or not 0 <= ny < h:
                        continue
                    if cells[ny][nx] == alive:
                        temp += 1
                if temp == 3:
                    new_cells[i][j] = alive
            else:
                for x, y in direction:
                    nx, ny = x + j, y + i
                    if not 0 <= nx < w or not 0 <= ny < h:
                        continue
                    if cells[ny][nx] == alive:
                        temp += 1
                if temp not in (2, 3):
                    new_cells[i][j] = dead
    cells = copy_cells(new_cells)
    display_cells(cells)
    time.sleep(1)
    cnt += 1
