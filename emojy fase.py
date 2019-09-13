import turtle


scn = turtle.Screen()
fas = turtle.Turtle()
ies = turtle.Turtle()
mawth = turtle.Turtle()
mawth2 = turtle.Turtle()


iesball = turtle.Turtle()
mawth.speed(.5)

def fase():
    fas.color("Yellow")
    fas.begin_fill()
    fas.circle(150)
    fas.end_fill()

def iese():
    ies.penup()
    ies.right(-90)
    ies.forward(190)
    ies.right(-90)
    ies.forward(40)
    ies.right(90)
    ies.color("white")
    ies.begin_fill()
    ies.circle(20)
    ies.end_fill()
    ies.goto(0, 0,)


def mowth2():
    mawth2.penup()
    mawth2.right(-90)
    mawth2.forward(110)
    mawth2.pendown()
    mawth2.right(-90)
    mawth2.forward(90)
    mawth2.right(180)
    mawth2.forward(170)
    mawth2.right(90)
    mawth2.color("white")
    mawth2.begin_fill()
    mawth2.forward(10)
    mawth2.right(90)
    mawth2.forward(165)
    mawth2.right(90)
    mawth2.forward(10)
    mawth2.end_fill()
    mawth2.penup()
    mawth2.goto(0, 0)



def mowth():
    mawth.penup()
    mawth.right(-90)
    mawth.forward(110)
    mawth.pendown()
    mawth.right(-90)
    mawth.forward(90)
    mawth.right(180)
    mawth.forward(180)
    mawth.right(90)
    mawth.begin_fill()
    for i in range(360):
        mawth.right(.5)
        mawth.forward(.8)
    mawth.right(90)
    mawth.forward(180)
    mawth.color("Peru")
    mawth.end_fill()
    mawth.penup()
    mawth.goto(0, 0)


def iesbolls():
    iesball.right(-90)
    iesball.forward(190)
    iesball.right(-90)
    iesball.forward(50)
    iesball.right(90)
    iesball.begin_fill()
    iesball.circle(10)
    iesball.end_fill()
    iesball.penup()
    iesball.right(90)
    iesball.forward(97)
    iesball.pendown()
    iesball.pensize(7)
    iesball.forward(35)
    iesball.penup()
    iesball.goto(0, 0)





fase()
iese()
mowth()
mowth2()
iesbolls()



turtle.exitonclick()