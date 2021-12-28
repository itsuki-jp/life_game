import tkinter
from time import sleep


def copy_cells( input_cells ):
    res = [_[::1] for _ in input_cells]
    return res


# -------------------- 変数 --------------------
h, w = 8, 8
dead = 0
alive = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
cells = [[dead for _ in range(w)] for _ in range(h)]
shape = {
    "octagon": [[0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0]]
}
size_w, size_h = 10, 10
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
canvas = tkinter.Canvas(frame, width=w * size_w, height=h * size_h, bg="gray")
canvas.pack()

# -------------------- 初期化 --------------------
# life_game
# 盤面の初期化     -----------------------------atode kaeru
now_shape = shape["octagon"]
tx = init_pos[1]
tx_max = min(tx + len(now_shape[0]), w)
for ty in range(init_pos[0], h):
    cells[ty:tx:tx_max] = now_shape[ty]

# tkinter
# とりあえず、キャンバスの各マスを真っ白にする
for ty in range(h):
    for tx in range(w):
        nx = tx * size_w
        ny = ty * size_h
        canvas.create_rectangle(nx, ny, nx + size_w, ny + size_h, tag=f"{ty}_{tx}", fill="white")

# -------------------- 頑張る --------------------
cnt = 0
while cnt != 10:
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
                    canvas.itemconfig(f"{i}_{j}", fill="white")
    cells = copy_cells(new_cells)
    cnt += 1
    sleep(0.5)
    root.update()

# ウィジェットが配置されたウィンドウを表示
root.mainloop()
