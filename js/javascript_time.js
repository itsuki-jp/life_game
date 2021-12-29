//  配列のコピー
function copyMatrix(base) {
    const result = [];
    for (const line of base) {
        result.push([...line]);
    }
    return result;
}



// ---------- HTMLに出力するための準備 ----------
const life_game = document.getElementById("life_game");
const canvas = document.createElement("canvas");
canvas.width = 500;
canvas.height = 500;
life_game.appendChild(canvas)
const ctx = canvas.getContext("2d");



// ---------- 変数 ----------
const h = 5;
const w = 5;
const size_w = 40;
const size_h = 40;
const dead = 0;
const alive = 1;
const max_loop = 100;
const direction = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [-1, -1],
    [1, -1],
    [-1, 1],
    [1, 1]
];



// ---------- 色を指定 ----------
ctx.strokeStyle = "black"; // 線の色
ctx.fillStyle = "red"; // 塗りつぶしの色



// ---------- 初期化 ----------
let alive_count = 0;
let cells = Array(h).fill().map(() => Array(w).fill(dead));

for (let i = 0; i < h; i++) {
    let ny = i * size_h;
    for (let j = 0; j < w; j++) {
        let nx = j * size_w;
        let dead_or_alive = Math.floor(Math.random() * 2);
        if (dead_or_alive) {
            // 輪郭, ctx.strokeRect(x, y, width, height)
            // ctx.strokeRect(j * size_w, i * size_h, size_w, size_h);

            // 塗りつぶし, ctx.fillRect(x, y, width, height)
            ctx.fillRect(j * size_w, i * size_h, size_w, size_h);
            cells[i][j] = alive;
            alive_count += 1;
        }
    }
}



// mainの処理
let cnt = 0;
while ((cnt != max_loop) && (alive_count != 0)) {
    console.log("start");
    let new_cells = copyMatrix(cells);
    for (let i = 0; i < h; i++) {
        let temp_i = i * size_h;
        for (let j = 0; j < w; j++) {
            let temp_j = j * size_w;
            let temp = 0
            for (let txty = 0; txty < 8; txty++) {
                let nx = direction[txty][0] + j;
                let ny = direction[txty][0] + i;
                if ((0 <= nx && nx < w) && (0 <= ny && ny < h)) {
                    if ((cells[ny][nx] == alive)) {
                        temp += 1;
                    }
                }
            }
            if (cells[i][j] == dead) {
                if (temp == 3) {
                    new_cells[i][j] = alive;
                    alive_count += 1;
                    // 輪郭, ctx.strokeRect(x, y, width, height)
                    // ctx.strokeRect(temp_j, temp_i, size_w, size_h);

                    // 塗りつぶし, ctx.fillRect(x, y, width, height)
                    ctx.fillRect(temp_j, temp_i, size_w, size_h);
                }
            } else {
                if (!(temp in [2, 3])) {
                    new_cells[i][j] = dead;
                    alive_count -= 1;
                    // 四角形の削除
                    // clearRect(x, y, width, height)
                    ctx.clearRect(temp_j, temp_i, size_w, size_h);
                }
            }
        }
    }
    cells = copyMatrix(new_cells);
    cnt += 1;
    //  ここらへんで0.2秒くらいsleepさせたい
};