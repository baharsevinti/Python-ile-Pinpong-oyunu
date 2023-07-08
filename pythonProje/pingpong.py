import turtle
windows=turtle.Screen()
windows.title("PingPong")
windows.bgcolor("black")
windows.setup(width=800,height=600)
windows.tracer(0)


racket_1=turtle.Turtle()
racket_1.speed(0)
racket_1.shape('square')
racket_1.color('green')
racket_1.penup()
racket_1.goto(-350,0)
racket_1.shapesize(5,1)


racket_2=turtle.Turtle()
racket_2.speed(0)
racket_2.shape('square')
racket_2.color('red')
racket_2.penup()
racket_2.goto(350,0)
racket_2.shapesize(5,1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx=0.15
ball.dy=0.15

writing=turtle.Turtle()
writing.speed(0)
writing.color('white')
writing.penup()
writing.goto(0,260)
writing.write("PLAYER A:0  PLAYER B:0",align='center',font=('Courier',24,'bold'))
writing.hideturtle()
score_1=0
score_2=0
def racket_1_up():
    y =racket_1.ycor()
    y= y+20
    racket_1.sety(y)

def racket_1_down():
    y =racket_1.ycor()
    y= y-20
    racket_1.sety(y)


def racket_2_up():
    y = racket_2.ycor()
    y = y + 20
    racket_2.sety(y)


def racket_2_down():
    y = racket_2.ycor()
    y = y - 20
    racket_2.sety(y)




windows.listen()
windows.onkeypress(racket_1_up,'w')
windows.onkeypress(racket_1_down,'s')
windows.onkeypress(racket_2_up,'Up')
windows.onkeypress(racket_2_down,'Down')



while True:
    windows.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy=ball.dy*-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_1=score_1+1
        writing.clear()
        writing.write("PLAYER A:{}  PLAYER B:{}".format(score_1,score_2), align='center', font=('Courier', 24, 'bold'))
    if ball.xcor() <- 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_2 = score_2 + 1
        writing.clear()
        writing.write("PLAYER A:{}  PLAYER B:{}".format(score_1,score_2), align='center', font=('Courier', 24, 'bold'))

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<racket_2.ycor()+60 and ball.ycor()>racket_2.ycor()-60):
        ball.setx(340)
        ball.dx=ball.dx*-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<racket_1.ycor()+60 and ball.ycor()>racket_1.ycor()-60):
        ball.setx(340)
        ball.dx=ball.dx*-1
