# 거북이 대포 게임
# 각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임

import turtle
import random as r

turtle.bgcolor('white')
# 땅그리기
# 좌표이동

turtle.shape('turtle')
# turtle.up()
# turtle.goto(0, 200)  #1 = X좌표 / 2 = Y좌표
# turtle.goto(0, -200)
# turtle.goto(200, 0)
# turtle.goto(-200, 0)

def turn_up():
    turtle.left(2)

# #땅땅그리기
# turtle.goto(-200, 0)
# turtle.goto(200, 0)

def turn_up():
    turtle.left(2)
def turn_down():
    turtle.right(2)
def fire():
    ang = turtle.heading()

    while turtle.ycor() > 0: #거북이의 y좌표가 0보다 크면
        turtle.forward(50)
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


turtle.goto(-950, 0)
turtle.goto(950, 0)


#목표지점
target = r.randint(300, 700) #목표지점은 50~150 사이의 임의의 수
turtle.color('black')
turtle.pensize(10)
turtle.up()
turtle.goto(target - 25, 2)
turtle.down()
turtle.goto(target + 25, 2)

turtle.color('black')
turtle.up()
turtle.goto(-200, 10)
turtle.setheading(20)

turtle.onkeypress(turn_up, "Up")
turtle.onkeypress(turn_down, "Down")
turtle.onkeypress(fire, "space")
turtle.listen()





turtle.mainloop()