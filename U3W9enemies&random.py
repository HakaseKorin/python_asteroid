import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Asteroids Prototype")
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()

bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()

bullet_speed = 20
bullet_state = "ready"

speed = 0

score = 0

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-380, 260)
score_pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

enemies = []

for i in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("gray")
    enemy.penup()

    x = random.randint(-390, 390)
    y = random.randint(-290, 290)

    enemy.goto(x, y)
    enemy.setheading(random.randint(0, 360))

    enemies.append(enemy)


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
    return t1.distance(t2) < 20


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

    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"

    for enemy in enemies:
        enemy.forward(2)

        if enemy.xcor() > 400:
            enemy.setx(-400)

        if enemy.xcor() < -400:
            enemy.setx(400)

        if enemy.ycor() > 300:
            enemy.sety(-300)

        if enemy.ycor() < -300:
            enemy.sety(300)

        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"

            x = random.randint(-390, 390)
            y = random.randint(-290, 290)

            enemy.goto(x, y)

            score += 10

            score_pen.clear()
            score_pen.write(
                f"Score: {score}",
                font=("Arial", 16, "normal")
            )

    screen.update()
