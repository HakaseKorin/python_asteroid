import turtle
bullet_speed = 20
bullet_state = "ready"

speed = 0


def accelerate():
    global speed
    speed += 0.15


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


def is_collision(t1, t2):
    distance = t1.distance(t2)

    if distance < 20:
        return True
    else:
        return False


screen.listen()
screen.onkey(accelerate, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(fire_bullet, "space")

while True:
    player.forward(speed)

    speed *= 0.99

    if bullet_state == "fire":
        bullet.forward(bullet_speed)

    if bullet.ycor() > 300 or bullet.ycor() < -300:
        bullet.hideturtle()
        bullet_state = "ready"

    if is_collision(bullet, asteroid):
        asteroid.goto(1000, 1000)

        bullet.hideturtle()
        bullet_state = "ready"

    screen.update()
