import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Asteroids")
screen.tracer(0)

# PLAYER
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()

# BULLET
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("white")
bullet.shapesize(0.25, 0.25)
bullet.penup()
bullet.hideturtle()

bullet_speed = .2
bullet_state = "ready"

player_speed = 0


def accelerate():
    global player_speed
    player_speed += 0.15


def turn_left():
    player.left(10)


def turn_right():
    player.right(10)


def fire_bullet():
    global bullet_state
    
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor())
        bullet.setheading(player.heading())
        bullet.showturtle()


screen.listen()
screen.onkey(accelerate, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(fire_bullet, "space")


while True:

    # Move player
    player.forward(player_speed)

    # Friction
    player_speed *= 0.99

    # Move bullet
    if bullet_state == "fire":
        bullet.forward(bullet_speed)

    # Reset bullet if off screen
    if (
        bullet.xcor() > 400 or bullet.xcor() < -400 or
        bullet.ycor() > 300 or bullet.ycor() < -300
    ):
        bullet.hideturtle()
        bullet_state = "ready"

    screen.update()

