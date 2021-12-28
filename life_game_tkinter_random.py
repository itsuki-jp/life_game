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
size_w, size_h = 4, 4
init_pos = [0, 0]  # [y,x]
max_loop = 1000

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
        if dead_or_alive:  # aliveの場合のみ、四角を生成する->描写量の削減
            canvas.create_rectangle(nx, ny, nx + size_w, ny + size_h, tag=f"{ty}_{tx}", fill="red")
            cells[ty][tx] = alive
            alive_count += 1

# -------------------- 更新パート --------------------
cnt = 0
while cnt != max_loop and alive_count != 0:
    new_cells = copy_cells(cells)
    for i in range(h):  # y
        temp_i = i * size_h
        for j in range(w):  # x
            temp_j = j * size_w
            #  noteより、あるマスに隣接してる生きているマスの数が重要なので、それを数える
            temp = 0
            for tx, ty in direction:
                nx, ny = tx + j, ty + i
                if not 0 <= nx < w or not 0 <= ny < h:
                    continue
                if cells[ny][nx] == alive:
                    temp += 1

            if cells[i][j] == dead:
                if temp == 3:  # 死んでいるセルに隣接する生きたセルが3個→誕生
                    new_cells[i][j] = alive
                    alive_count += 1
                    canvas.create_rectangle(temp_j, temp_i, temp_j + size_w, temp_i + size_h, tag=f"{i}_{j}",
                                            fill="red")
            else:
                if temp not in (2, 3):  # 生きているセルに隣接する生きたセルが2,3個以外→死滅
                    new_cells[i][j] = dead
                    alive_count -= 1
                    canvas.delete(f"{i}_{j}")
    cells = copy_cells(new_cells)
    cnt += 1
    sleep(0.1)
    root.update()

# ウィジェットが配置されたウィンドウを表示
root.mainloop()
