import tkinter

# ウィンドウの生成
root = tkinter.Tk()
root.attributes("-topmost", True)
root.minsize(width=200, height=200)

# Frameウィジェットの生成
frame = tkinter.Frame(root, width=300, height=300, bg="black")
frame.propagate(False)
frame.pack()

# Canvasウィジェットの生成
canvas = tkinter.Canvas(frame, width=300, height=300, bg="gray")
canvas.pack()

size_w, size_h = 10, 10
for y in range(30):
    for x in range(30):
        nx = x * size_w
        ny = y * size_h
        canvas.create_rectangle(nx, ny, nx + size_w, ny + size_h, tag=f"{y}_{x}", outline="white", fill="red")

for _ in range(30):
    canvas.itemconfig(f"{_}_{_}", fill="blue")

# ウィジェットが配置されたウィンドウを表示
root.mainloop()
