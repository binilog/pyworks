# 거북이 대포 게임
# 각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임

import turtle
import random as r

n = 100

turtle.speed(0)  # 1 ~ 10, 가장 빠른 속도 - 0
turtle.bgcolor('black')  # 무대 배경 색
turtle.color('blue')  # 거북이 색

turtle.shape('turtle') #거북이 쉐키 모양
turtle.pensize(8)
turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(114)
turtle.forward(400)
turtle.left(200)
turtle.forward(450)
turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(210)
turtle.forward(480)
turtle.left(130)
turtle.forward(600)
turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(140)
turtle.forward(600)
turtle.right(140)
turtle.forward(700)
turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(220)
turtle.forward(700)
turtle.left(165)
turtle.forward(600)
turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)

turtle.left(160)
turtle.forward(600)
turtle.left(140)
turtle.forward(350)

turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)

turtle.right(36)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.right(72)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)

turtle.left(62)
turtle.forward(600)

for i in range(n):
    turtle.circle(800)
    turtle.left(360 / n)
#
#
# def turn_right():
#     turtle.setheading(0)
#     turtle.forward(10)
#
#
# def turn_up():
#     turtle.setheading(90)
#     turtle.forward(10)
#
#
# def turn_left():
#     turtle.setheading(180)
#     turtle.forward(10)
#
#
# def turn_down():
#     turtle.setheading(270)
#     turtle.forward(10)
#
#
# def clear():
#     turtle.clear()
#

turtle.shape('turtle')
# turtle.onkeypress(turn_right, "Right")
# turtle.onkeypress(turn_up, "Up")
# turtle.onkeypress(turn_left, "Left")
# turtle.onkeypress(turn_down, "Down")
# turtle.onkeypress(clear, "Escape")
# turtle.listen()
# 땅그리기
# 좌표이동

# turtle.shape('turtle')
# turtle.up()
# turtle.goto(0, 200)  #1 = X좌표 / 2 = Y좌표
# turtle.goto(0, -200)
# turtle.goto(200, 0)
# turtle.goto(-200, 0)

# #땅땅그리기
# turtle.goto(-200, 0)
# turtle.goto(200, 0)

turtle.goto(-300, 0)
turtle.goto(300, 0)
turtle.color('purple')

def turn_up():
    turtle.left(2)
def turn_down():
    turtle.right(2)
def fire():
    ang = turtle.heading()

    while turtle.ycor() > 0: #거북이의 y좌표가 0보다 크면
        turtle.forward(25)
        turtle.right(5)

    #while 반복문을 빠져나오면 땅에 닿은 상태임
    d = turtle.distance(target, 0)   #거북이와 목표지점과의 거리 저장
    turtle.sety(r.randint(10, 100))
    if d < 25:
        turtle.color('blue')
        turtle.write("Good!", False, "center", ("", 15)) #명중
        turtle.goto(-200, 10)
        turtle.setheading(ang)
    else: #그렇지 않으면 실패한 것으로 처리
        turtle.color('red')
        turtle.write("Bad!", False, "center", ("", 15))
        turtle.goto(-200, 10)
        turtle.setheading(ang)





#목표지점
target = r.randint(50, 150) #목표지점은 50~150 사이의 임의의 수
turtle.color('white')
turtle.bgcolor('white')
turtle.pensize(10)
turtle.up()
turtle.goto(target - 25, 2)
turtle.down()
turtle.goto(target + 25, 2)

turtle.color('white')
turtle.up()
turtle.goto(-200, 10)
turtle.setheading(20)

turtle.onkeypress(turn_up, "Up")
turtle.onkeypress(turn_down, "Down")
turtle.onkeypress(fire, "space")
turtle.listen()





turtle.mainloop()