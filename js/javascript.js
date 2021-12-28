const life_game = document.getElementById("life_game");
const canvas = document.createElement("canvas");
canvas.width = 500;
canvas.height = 500;
life_game.appendChild(canvas)

const ctx = canvas.getContext("2d");