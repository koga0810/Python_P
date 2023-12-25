import turtle as t
from random import *

t.setup(1300, 600, 30, 35) # ウインドウサイズ
t.bgcolor('black') #背景色
t.shape('turtle') # 亀出現
t.speed(5) # 描く速さ
t.pensize(2) # ペンの太さ

# 描き始めたい場所へ移動
t.hideturtle() # カーソル非表示
t.left(90)
t.forward(200)
t.left(90)
t.forward(500)
t.right(180)
t.showturtle() # カーソル表示

# 星1
t.color('yellow') # 線の色（色名指定）
t.begin_fill() # 塗りつぶし開始

t.right(50)
t.forward(40)
t.left(70)
t.forward(50)
t.right(130)
t.forward(50)
t.left(60)
t.forward(50)
t.right(130)
t.forward(50)
t.left(40)
t.forward(50)
t.right(130)
t.forward(50)
t.left(60)
t.forward(50)
t.right(130)
t.forward(40)
t.left(65)
t.forward(45)

t.end_fill() # 塗りつぶし終了

# 移動
t.penup() # ペンを上げる
t.right(80)
t.forward(100)
t.pendown() # ペンを下ろす

# 星の軌道1_1
t.left(30)
t.forward(30)
t.pensize(3)
t.forward(30)
t.pensize(4)
t.forward(30)
t.pensize(5)
t.forward(30)
t.pensize(6)
t.forward(30)

# 移動
t.penup() # ペンを上げる
t.right(180)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.pendown() # ペンを下ろす

# 星の軌道1_2
t.pensize(2)
t.forward(30)
t.pensize(3)
t.forward(30)
t.pensize(4)
t.forward(30)
t.pensize(5)
t.forward(30)
t.pensize(6)
t.forward(30)

# 移動
t.penup() # ペンを上げる
t.right(180)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.pendown() # ペンを下ろす

# 星の軌道1_3
t.pensize(2)
t.forward(30)
t.pensize(3)
t.forward(30)
t.pensize(4)
t.forward(30)
t.pensize(5)
t.forward(30)
t.pensize(6)
t.forward(30)

# 移動
t.penup() # ペンを上げる
t.right(180)
t.forward(500)
t.left(55)
t.forward(200)
t.left(90)
t.pendown() # ペンを下ろす

# 地面
t.colormode(255) # RGBカラーモード
t.color(255,255,255) # RGB（白）
t.forward(1250)

# 移動
t.penup()
t.left(180)
t.forward(300)
t.pendown()

# ツリー（木の部分）
t.color(210,105,30) # RGB（茶）
t.begin_fill() # 塗りつぶし開始

t.pensize(5)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)

t.end_fill() # 塗りつぶし終了

# 移動
t.penup() # ペンを上げる
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.pendown() # ペンを下ろす

# 木の部分（葉の部分）
t.color(0,255,0) # RGB（緑）
t.begin_fill() # 塗りつぶし開始

t.pensize(2)
t.forward(150) # 1段目の下線（左）
t.right(150)
t.forward(150) # 2段目へ上る斜線（左）
t.left(150)
t.forward(100) # 2段目の下線（左）
t.right(150)
t.forward(125) # 3段目へ上る斜線（左）
t.left(150)
t.forward(75) # 3段目の下線（左）
t.right(150)
t.forward(80) # 4段目へ上る斜線（左）
t.left(150)
t.forward(45) # 4段目の下線（左）
t.right(140)
t.forward(140) # 頂点の線（左）
t.right(80) # 頂点で方向転換
t.forward(140) # 頂点の線（右）
t.right(140)
t.forward(45) # 4段目の下線（右）
t.left(150)
t.forward(80) # 3段目へ下りる斜線（右）
t.right(150)
t.forward(75) # 3段目の下線（右）
t.left(150)
t.forward(125) # 2段目へ下りる斜線（右）
t.right(150)
t.forward(100) # 2段目の下線（右）
t.left(150)
t.forward(150) # 1段目へ下りる斜線（右）
t.right(150)
t.forward(250) # 1段目の下線（右）

t.end_fill() # 塗りつぶし終了

# 移動
t.penup() # ペンを上げる
t.left(90)
t.forward(50)
t.right(90)
t.forward(500)
t.left(180)
t.pendown() # ペンを下ろす

# 雪だるま
t.color(255,255,255) # RGB（白）
t.begin_fill() # 塗りつぶし開始

t.circle(50) # 雪だるまの体（下）

t.end_fill() # 塗りつぶし修了

t.left(90)
t.penup() # ペンを上げる
t.forward(90)
t.pendown() # ペンを下ろす

t.begin_fill() # 塗りつぶし開始

t.right(90)
t.circle(35) # 雪だるまの体（上）

t.end_fill() # 塗りつぶし終了

t.penup() # ペンを上げる
t.forward(10)
t.left(90)
t.forward(15)
t.pendown() # ペンを下ろす
t.left(60)

t.pensize(4) # ペンサイズ変更
t.color(0,0,0) # RGB（黒）
t.forward(25) # 雪だるまの口

t.penup() # ペンを上げる
t.right(145)
t.forward(15) # 鼻へ移動
t.pendown() # ペンを下ろす

t.left(80)
t.forward(10) # 雪だるまの鼻

t.penup() # ペンを上げる
t.right(55)
t.forward(15) # 左目へ移動
t.pendown() # ペンを下ろす

t.pensize(10) # ペンサイズ変更
t.circle(1) # 雪だるまの左目

t.penup() # ペンを上げる
t.left(145)
t.forward(30) # 右目へ移動
t.pendown() # ペンを下ろす

t.right(180)
t.circle(1) # 雪だるまの右目

t.penup() # ペンを上げる
t.left(110)
t.forward(15) # 頭へ移動
t.pendown() # ペンを下ろす

t.pensize(6) # ペンサイズ変更
t.color(255,0,0) # RGB（赤）
t.begin_fill() # 塗りつぶし開始
t.right(30)
t.forward(30) # 帽子（左辺）
t.right(75)
t.forward(30) # 帽子（上辺）
t.right(80)
t.forward(30) # 帽子（右辺）
t.right(100)
t.forward(40) # 帽子（下辺）

t.end_fill() # 　塗りつぶし終了

t.penup() # ペンを上げる
t.left(75)
t.forward(95) # 右手へ移動
t.right(80)
t.pendown() # ペンを下ろす

 # 雪だるまの右手
t.color(210,105,30) # RGB（茶）
t.right(10)
t.forward(50)
t.left(30)
t.forward(20)
t.penup() # ペンを上げる
t.right(180)
t.forward(20)
t.left(120)
t.pendown() # ペンを下ろす
t.forward(20)

# 移動
t.penup() # ペンを上げる
t.right(145)
t.forward(140)
t.left(40)
t.pendown() # ペンを下ろす

# 雪だるまの左手
t.forward(50)
t.left(45)
t.forward(20)
t.penup() # ペンを上げる
t.left(180)
t.forward(20)
t.left(120)
t.pendown() # ペンを下ろす
t.forward(20)

# 移動
t.penup() # ペンを上げる
t.left(180)
t.forward(105)
t.pendown() # ペンを下ろす

# 雪だるまのボタン
t.color(255,255,0) # RGB（黄）
t.circle(3)
t.left(68)
t.penup() # ペンを上げる
t.forward(20)
t.pendown() # ペンを下ろす
t.circle(3)
t.left(8)
t.penup() # ペンを上げる
t.forward(20)
t.pendown() # ペンを下ろす
t.circle(3)

# 移動
t.penup() # ペンを上げる
t.goto(249,50) # 座標指定移動
t.pendown() # ペンを下ろす
t.left(88)

# ツリーの星
for i in range(50): # 引数分動作を繰り返す
    r = 255
    g = 50 + i * 4
    b = 0
    t.pencolor(r, g, b) # 変数宣言した(r,g,b)をcolorの数値として呼び出す
    t.forward(30 + 2 * i)
    t.right(144)

# 雪
t.speed(0) # 速さ変更
t.color(255,255,255) # RGB（白）
for i in range(300): # 引数分動作を繰り返す
    t.penup() # ペンを上げる
    x = uniform(-1000,1000) # 指定した範囲の乱数を取得
    y = uniform(-300,300)
    t.goto(x,y) # xとyそれぞれの取得した値へ座標移動
    t.pendown() # ペンを下ろす
    t.circle(1)
    
t.done()