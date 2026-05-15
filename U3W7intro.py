import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Asteroid")
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()

speed = 0

def turn_left():
    player.left(10)

def turn_right():
    player.right(10)

def accelerate():
    global speed
    speed += 0.15
  
screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(accelerate, "Up")

while True:
    player.forward(speed)
    speed *= 0.99

    x = player.xcor()
    y = player.ycor()

    if x > 400:
        player.setx(-400)
    if x < -400:
        player.setx(400)
    if y > 300:
        player.sety(-300)
    if y < -300:
        player.sety(300)

    screen.update()
