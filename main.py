import turtle

#schermo
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Game")

#Border
border_pen =  turtle.Turtle()
border_pen.color("White")
border_pen.speed(0)
border_pen.penup()
border_pen.pensize(3)
border_pen.setpos(-300,-300)
border_pen.pendown()
for var in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#pleyer
playerspeed = 15
pl = turtle.Turtle()
pl.penup()
pl.hideturtle()
pl.color("Green")
pl.setpos(0, -200)
pl.setheading(90)
pl.shape("triangle")
pl.speed(0)
pl.showturtle()

#enemy
en = turtle.Turtle()
en.hideturtle()
en.penup()
en.shape("circle")
en.color("red")
en.setpos(-200, 250)
en.speed(0)
en.showturtle()
enemy_speed = 5

# Bullet
bl = turtle.Turtle()
bl.shape("triangle")
bl.shapesize(0.5, 0.5)
bl.color("Yellow")
bl.penup()
bl.speed(0)
bl.setheading(90)

bulletstate = "Fire"

#Key inputs
def move_left():
    x = pl.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    pl.setx(x)

def move_right():
    x = pl.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    pl.setx(x)


def bl_fire():
    global bulletstate
    if bulletstate == "Ready":
        bulletstate = "Fire"
        x = pl.xcor()
        y = pl.ycor() + 10
        bl.setpos(x, y)
        bl.showturtle()

# player movements

wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(bl_fire, "space")
wn.listen()


# main loop
en_height = 15
bl_speed = 20

while True:
    x = en.xcor()
    x += enemy_speed
    en.setx(x)
    
    if en.xcor() > 280:
        enemy_speed *= -1
        y = en.ycor()
        y-= en_height
        en.sety(y)
    if en.xcor() < -280:
        enemy_speed *= -1
        y = en.ycor()
        y -= en_height
        en.sety(y)
    if en.ycor() == pl.ycor():
        break

    if bulletstate == "Fire":
        y = bl.ycor()
        y += bl_speed
        bl.sety(y)

    if bl.ycor() > 275:
        bl.hideturtle()
        bulletstate = "Ready"

    




freeze = input("Press any key to quit")
wn.mainloop()
