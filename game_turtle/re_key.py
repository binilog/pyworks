import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
        t.setheading(180)
        t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()

t.shape('turtle')
t.onkeypress(turn_right, "Right") #오른쪽
t.onkeypress(turn_up, "Up") #위
t.onkeypress(turn_left, "Left") #왼
t.onkeypress(turn_down, "Down") #아래
t.onkeypress(clear, "Escape") #esc
t.listen() #대기






t.mainloop()