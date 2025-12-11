import turtle
import random

gecikme_ms = 100
skor = 0

ekran = turtle.Screen()
ekran.title("Yılan Oyunu (Duvardan Geçen)")
ekran.bgcolor("lightgreen")
ekran.setup(width=600, height=600)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("darkblue")
kafa.penup()
kafa.goto(0, 0)
kafa.yon = "dur"

yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0, 100)

t_yazi = turtle.Turtle()
t_yazi.speed(0)
t_yazi.shape("square")
t_yazi.color("black")
t_yazi.penup()
t_yazi.hideturtle()
t_yazi.goto(0, 260)
t_yazi.write("Skor: 0", align="center", font=("Arial", 24, "normal"))

vucut_parcalari = []


def yukari_git():
    if kafa.yon != "asagi":
        kafa.yon = "yukari"


def asagi_git():
    if kafa.yon != "yukari":
        kafa.yon = "asagi"


def saga_git():
    if kafa.yon != "sol":
        kafa.yon = "saga"


def sola_git():
    if kafa.yon != "saga":
        kafa.yon = "sol"


ekran.listen()
ekran.onkey(yukari_git, "Up")
ekran.onkey(asagi_git, "Down")
ekran.onkey(saga_git, "Right")
ekran.onkey(sola_git, "Left")


def oyun_dongusu():
    global skor, gecikme_ms

    if kafa.xcor() > 290:
        kafa.setx(-290)
    elif kafa.xcor() < -290:
        kafa.setx(290)
    elif kafa.ycor() > 290:
        kafa.sety(-290)
    elif kafa.ycor() < -290:
        kafa.sety(290)

    if kafa.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        yeni_parca = turtle.Turtle()
        yeni_parca.speed(0)
        yeni_parca.shape("square")
        yeni_parca.color("blue")
        yeni_parca.penup()
        vucut_parcalari.append(yeni_parca)

        skor = skor + 10
        t_yazi.clear()
        t_yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 24, "normal"))

        gecikme_ms = int(gecikme_ms * 0.98)

    for i in range(len(vucut_parcalari) - 1, 0, -1):
        x = vucut_parcalari[i - 1].xcor()
        y = vucut_parcalari[i - 1].ycor()
        vucut_parcalari[i].goto(x, y)

    if len(vucut_parcalari) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        vucut_parcalari[0].goto(x, y)

    if kafa.yon == "yukari":
        y = kafa.ycor()
        kafa.sety(y + 20)

    if kafa.yon == "asagi":
        y = kafa.ycor()
        kafa.sety(y - 20)

    if kafa.yon == "saga":
        x = kafa.xcor()
        kafa.setx(x + 20)

    if kafa.yon == "sol":
        x = kafa.xcor()
        kafa.setx(x - 20)

    for parca in vucut_parcalari:
        if parca.distance(kafa) < 20:

            final_skor = skor

            kafa.goto(0, 0)
            kafa.yon = "dur"

            for p in vucut_parcalari:
                p.goto(1000, 1000)
            vucut_parcalari.clear()

            skor = 0
            t_yazi.clear()

            t_yazi.write("Oyun Bitti! Final Skor: {}".format(final_skor),
                         align="center", font=("Arial", 24, "normal"))

            gecikme_ms = 100

    ekran.ontimer(oyun_dongusu, gecikme_ms)


oyun_dongusu()
turtle.done()
