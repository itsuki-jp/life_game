# https://agirobots.com/python-lifegame-nyumon/
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

# ============================
# 初期状態の設定
# ============================

# 高さ、幅
h, w = 401, 401

# 任意の状態を用意
state = np.zeros((h, w))
state[200, :] = 1
state[:, 200] = 1

# フィールドのどこに置くか（左上点を指定）
p = (0, 0)

# 終了ステップ数
max_step = 135

# ============================
# メイン処理
# ============================

# フィールドの生成
f = np.zeros((h, w), dtype=bool)

# 任意の状態を置く
f[p[0]:p[0] + len(state), p[1]:p[1] + len(state[0])] = state

# 画像をスタックする配列の準備
fig = plt.figure()
ims = []

# 初期状態の表示（スタック）
im = plt.imshow(f, cmap='inferno')
ims.append([im])

# 状態の更新
for i in range(1, max_step + 1):
    # 周囲の生存マス数を記録するための配列
    mask = np.zeros((h, w))

    # 周囲の生存マスを足し込む
    mask[1:, :] += f[:-1, :]  # 上
    mask[:-1, :] += f[1:, :]  # 下
    mask[:, 1:] += f[:, :-1]  # 左
    mask[:, :-1] += f[:, 1:]  # 右
    mask[1:, 1:] += f[:-1, :-1]  # 左上
    mask[1:, :-1] += f[:-1, 1:]  # 右上
    mask[:-1, 1:] += f[1:, :-1]  # 左下
    mask[:-1, :-1] += f[1:, 1:]  # 右下

    # 未来のフィールド（すべて死状態）
    future = np.zeros((h, w), dtype=bool)

    # 生きているマスが生きる条件（＝生存）
    future[mask * f == 2] = 1
    future[mask * f == 3] = 1
    # 死んでいるマスが生きる条件（＝誕生）
    future[mask * ~f == 3] = 1

    # フィールドの更新（浅いコピーに注意）
    f = future

    # 表示（スタック）
    im = plt.imshow(f, cmap='inferno')
    ims.append([im])

# アニメーション表示の準備
print('making animation......')
print('len(ims) = ' + str(len(ims)))
ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)

plt.show()

# .gifや.mp4を保存する場合はこちらを有効に
ani.save('test2.gif', writer='imagemagick', fps=40)
# ani.save('bbb.mp4', writer="ffmpeg")
