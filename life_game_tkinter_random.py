import tkinter
from time import sleep
from random import randint
from collections import defaultdict


def copy_cells( input_cells ):
    res = [_[::1] for _ in input_cells]
    return res


# -------------------- 変数 --------------------
h, w = 200, 200
dead = 0
alive = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
shape = {
    "octagon": [[0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0]]
}
size_w, size_h = 4, 4
init_pos = [0, 0]  # [y,x]

# -------------------- Tkinter --------------------
# ウィンドウの生成
root = tkinter.Tk()
root.attributes("-topmost", True)
root.minsize(width=w * size_w, height=h * size_h)

# Frameウィジェットの生成
frame = tkinter.Frame(root, width=w * size_w, height=h * size_h, bg="black")
frame.propagate(False)
frame.pack()

# Canvasウィジェットの生成
canvas = tkinter.Canvas(frame, width=w * size_w, height=h * size_h)
canvas.pack()

# -------------------- 初期化 --------------------
# life game
alive_count = 0
cells = [[dead for _ in range(w)] for _ in range(h)]
for ty in range(h):
    for tx in range(w):
        dead_or_alive = randint(0, 2)
        nx = tx * size_w
        ny = ty * size_h
        if dead_or_alive:  # alive
            canvas.create_rectangle(nx, ny, nx + size_w, ny + size_h, tag=f"{ty}_{tx}",
                                    fill="red")
            cells[ty][tx] = alive
            alive_count += 1

# -------------------- 頑張る --------------------
cnt = 0
while cnt != 1000 and alive_count != 0:
    new_cells = copy_cells(cells)
    for i in range(h):  # y
        temp_i = i * size_h
        for j in range(w):  # x
            temp_j = j * size_w
            temp = 0
            if cells[i][j] == dead:
                for tx, ty in direction:
                    nx, ny = tx + j, ty + i
                    if not 0 <= nx < w or not 0 <= ny < h:
                        continue
                    if cells[ny][nx] == alive:
                        temp += 1
                if temp == 3:
                    new_cells[i][j] = alive
                    alive_count += 1
                    canvas.create_rectangle(temp_j, temp_i, temp_j + size_w, temp_i + size_h, tag=f"{i}_{j}",
                                            fill="red")
            else:
                for tx, ty in direction:
                    nx, ny = tx + j, ty + i
                    if not 0 <= nx < w or not 0 <= ny < h:
                        continue
                    if cells[ny][nx] == alive:
                        temp += 1
                if temp not in (2, 3):
                    new_cells[i][j] = dead
                    alive_count -= 1
                    canvas.delete(f"{i}_{j}")
    cells = copy_cells(new_cells)
    cnt += 1
    sleep(0.1)
    root.update()

# ウィジェットが配置されたウィンドウを表示
root.mainloop()
