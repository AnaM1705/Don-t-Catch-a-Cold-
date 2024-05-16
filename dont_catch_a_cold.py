import turtle
import random
import winsound

wn = turtle.Screen()
wn.title("Don't Catch a Cold! by Ana")
# wn.bgcolor("black")
wn.bgpic("winterbg.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("tea.gif")
wn.register_shape("soup.gif")
wn.register_shape("greengerm.gif")
wn.register_shape("purplegerm.gif")
wn.register_shape("penguin.gif")
# Score
score = 0

# Lives
lives = 10

# Player
player = turtle.Turtle()
player.shape("penguin.gif")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -250)

# lists of items

teas = []
soups = []
greengerms = []
purplegerms = []


# Tea
for x in range(15):
    tea = turtle.Turtle()
    tea.shape("tea.gif")
    tea.color("white")
    tea.penup()
    tea.speed(0)
    tea.goto(random.randint(-390, 390), random.randint(300, 400))
    teas.append(tea)

# Soup
for x in range(5):
    soup = turtle.Turtle()
    soup.shape("soup.gif")
    soup.color("white")
    soup.penup()
    soup.speed(0)
    soup.goto(random.randint(-390, 390), random.randint(300, 400))
    soups.append(soup)


# GermGreen
for y in range(15):
    greengerm = turtle.Turtle()
    greengerm.shape("greengerm.gif")
    greengerm.color("white")
    greengerm.penup()
    greengerm.speed(0)
    greengerm.goto(random.randint(-390, 390), random.randint(300, 400))
    greengerms.append(greengerm)

# PurpleGerms
for y in range(5):
    purplegerm = turtle.Turtle()
    purplegerm.shape("purplegerm.gif")
    purplegerm.color("white")
    purplegerm.penup()
    purplegerm.speed(0)
    purplegerm.goto(random.randint(-390, 390), random.randint(300, 400))
    purplegerms.append(purplegerm)

# Pen i.e. score display
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 260)
pen.write(f'Score = {score}   Lives = {lives}',
          align="center", font=("Chicago", 24, "bold"), )

# Player movement


def player_left():
    x = player.xcor()
    x -= 30
    player.setx(x)


def player_right():
    x = player.xcor()
    x += 30
    player.setx(x)


# Keyboard binding
wn.listen()
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_right, "Right")


while True:
    wn.update()

    # Move tea
    
    for tea in teas:
        tea_speed = random.uniform(0.1, 2)
        tea.sety(tea.ycor()-tea_speed)

        # tea border
        if tea.ycor() < -290:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            tea.goto(x, y)

        # tea colision
        if tea.distance(player) < 40:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            tea.goto(x, y)
            score += 1
            pen.clear()
            pen.write(f'Score = {score}   Lives = {lives}',
                      align="center", font=("Chicago", 24, "bold"), )
            winsound.PlaySound('ding.wav', winsound.SND_ASYNC)

    # Move soup
    for soup in soups:
        soup_speed = random.uniform(1, 2)
        soup.sety(soup.ycor()-soup_speed)

        # soup border
        if soup.ycor() < -290:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            soup.goto(x, y)

        # soup colision
        if soup.distance(player) < 40:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            soup.goto(x, y)
            lives += 1

            pen.clear()
            pen.write(f'Score = {score}   Lives = {lives}',
                      align="center", font=("Chicago", 24, "bold"), )
            winsound.PlaySound('slurp.wav', winsound.SND_ASYNC)

    # Move greengerm
    for greengerm in greengerms:
        greengerm_speed = random.uniform(0.1, 2)
        greengerm.sety(greengerm.ycor()-greengerm_speed)

        # greengerm border
        if greengerm.ycor() < -290:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            greengerm.goto(x, y)

        # greengerm colision
        if greengerm.distance(player) < 40:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            greengerm.goto(x, y)
            lives -= 1
            pen.clear()
            pen.write(f'Score = {score}   Lives = {lives}',
                      align="center", font=("Chicago", 24, "bold"), )
            winsound.PlaySound('ice.wav', winsound.SND_ASYNC)

    # Move purplegerm
    for purplegerm in purplegerms:
        purplegerm_speed = random.uniform(1, 2)
        purplegerm.sety(purplegerm.ycor()-purplegerm_speed)

        # purplegerm border
        if purplegerm.ycor() < -290:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            purplegerm.goto(x, y)

        # purplegerm colision
        if purplegerm.distance(player) < 40:
            y = random.randint(300, 400)
            x = random.randint(-390, 390)
            purplegerm.goto(x, y)
            lives -= 2
            pen.clear()
            pen.write(f'Score = {score}   Lives = {lives}',
                      align="center", font=("Chicago", 24, "bold"), )
            winsound.PlaySound('sneeze.wav', winsound.SND_ASYNC)

    # Win
    if lives > 1 and score > 100:
        pen.clear()
        pen.goto(0, 0)
        pen.write(f'You won!\nYour score is {score},\ncongratulations!',
                  align="center", font=("Chicago", 50, "bold"), )
        winsound.PlaySound('success.wav', winsound.SND_ASYNC)
        turtle.done()

    # Loose
    if lives <= 1:
        pen.clear()
        pen.goto(0, 0)
        pen.write(f'You lost and got a cold!\nYour score is {score}.\nGet well soon!',
                  align="center", font=("Chicago", 50, "bold"), )
        winsound.PlaySound('snuffings.wav', winsound.SND_ASYNC)
        turtle.done()


wn.mainloop()  
