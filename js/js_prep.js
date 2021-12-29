// HTMLに出力するための準備
const life_game = document.getElementById("life_game");
const canvas = document.createElement("canvas");
canvas.width = 500;
canvas.height = 500;
life_game.appendChild(canvas)
const ctx = canvas.getContext("2d");

// 色を指定
ctx.strokeStyle = "blue"; // 線の色を青に指定
ctx.fillStyle = "red"; // 塗りつぶしの色を赤に指定

// 四角形（輪郭）
// ctx.strokeRect(x, y, width, height)
ctx.strokeRect(100, 100, 100, 100);

// 四角形（塗りつぶし）
// ctx.fillRect(x, y, width, height)
ctx.fillRect(150, 10, 100, 100);

// 四角形の削除
// clearRect(x, y, width, height)
ctx.clearRect(150, 10, 100, 100);