// ---------- HTMLに出力するための準備 ----------
const life_game = document.getElementById("life_game");
const canvas = document.createElement("canvas");
canvas.width = 500;
canvas.height = 500;
life_game.appendChild(canvas)
const ctx = canvas.getContext("2d");

// ---------- 変数 ----------
const h = 10;
const w = 10;
const size_w = 40;
const size_h = 40;
const dead = 0;
const alive = 1;
const max_loop = 1000
const direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

// ---------- 色を指定 ----------
ctx.strokeStyle = "black"; // 線の色
ctx.fillStyle = "red"; // 塗りつぶしの色

// ---------- とりあえず全部塗る ----------
for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
        // 輪郭, ctx.strokeRect(x, y, width, height)
        ctx.strokeRect(j * size_w, i * size_h, size_w, size_h);

        // 塗りつぶし, ctx.fillRect(x, y, width, height)
        ctx.fillRect(j * size_w, i * size_h, size_w, size_h);
    }
}



// 四角形の削除
// clearRect(x, y, width, height)
// ctx.clearRect(150, 10, 100, 100);