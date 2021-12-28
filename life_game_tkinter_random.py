import tkinter
from time import sleep
from random import randint


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
size_w, size_h = 3, 3
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
cells = [[alive if randint(0, 2) else dead for _ in range(w)] for _ in range(h)]
alive_count = sum([sum(_) for _ in cells])

# tkinter
# とりあえず、キャンバスの各マスを真っ白にする
for ty in range(h):
    for tx in range(w):
        nx = tx * size_w
        ny = ty * size_h
        canvas.create_rectangle(nx, ny, nx + size_w, ny + size_h, tag=f"{ty}_{tx}",
                                fill="red" if cells[ty][tx] else "white")

# -------------------- 頑張る --------------------
cnt = 0
while cnt != 1000 and alive_count != 0:
    new_cells = copy_cells(cells)
    for i in range(h):  # y
        for j in range(w):  # x
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
                    canvas.itemconfig(f"{i}_{j}", fill="red")
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
                    canvas.itemconfig(f"{i}_{j}", fill="white")
    cells = copy_cells(new_cells)
    cnt += 1
    sleep(0.1)
    root.update()

# ウィジェットが配置されたウィンドウを表示
root.mainloop()
