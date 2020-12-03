#Libary enable you to make moving object in python
import turtle
#We will create our screen which we can play the game in
windo = turtle.Screen()
#Now we will give our screen a title
windo.title("Pong Game")
#now we will set our background color
windo.bgcolor("black")
#Now we will set the hight and width of our screen
windo.setup(width=800, height=600)
#We will use .tracer() to prevent our screen to update itself
windo.tracer(0)
#Now we will create our game loop -_-
#Wall1
score1 = 0
score2 = 0
wall = turtle.Turtle()
wall.speed(0)
wall.shape("square")
wall.color("blue")
wall.shapesize(stretch_wid=5, stretch_len=1)
wall.penup()
wall.goto(-350, 0)
#wall2
wall2 = turtle.Turtle()
wall2.speed(0)
wall2.shape("square")
wall2.color("red")
wall2.shapesize(stretch_wid=5, stretch_len=1)
wall2.penup()
wall2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player 1:{score1} palyer 2:{score2}",
            align="center",
            font=("courier", 24, "normal"))


#functions
def wall_up():
    y = wall.ycor()
    y += 20
    wall.sety(y)


def wall_down():
    y = wall.ycor()
    y -= 20
    wall.sety(y)


def wall2_up():
    y = wall2.ycor()
    y += 20
    wall2.sety(y)


def wall2_down():
    y = wall2.ycor()
    y -= 20
    wall2.sety(y)


#keyboard bindings
windo.listen()
windo.onkeypress(wall_up, "w")
windo.onkeypress(wall_down, "s")
windo.onkeypress(wall2_up, "Up")
windo.onkeypress(wall2_down, "Down")
while True:
    windo.update()  #update the screan the loope runs
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1:{score1} palyer 2:{score2}",
                    align="center",
                    font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1:{score1} palyer 2:{score2}",
                    align="center",
                    font=("courier", 24, "normal"))
    #collosion
    if (ball.xcor() > 340 and ball.xcor() < 350 and
        (ball.ycor() < wall2.ycor() + 40 and ball.ycor() > wall2.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350 and
        (ball.ycor() < wall.ycor() + 40 and ball.ycor() > wall.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1
