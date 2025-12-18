import turtle
import time

hareket_yon = None
hareket_yon2 = None
hiz = 2
mermi_hizi = 7

tus_basili1 = False
tus_basili2 = False

mermi_var1 = False
mermi_var2 = False

can1 = 5
can2 = 5

ekran = turtle.Screen()
ekran.title("İKİ KİŞİLİK SAVAŞ OYUNU")
ekran.bgcolor("wheat")
ekran.setup(width=600, height=600)
ekran.tracer(0)

yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.color("black")


def canlari_guncelle():
    yazi.clear()
    yazi.goto(-250, 260)
    yazi.write(f"K2 (Kırmızı) Can: {can2}", align="left", font=("Arial", 14, "bold"))
    yazi.goto(250, 260)
    yazi.write(f"K1 (Mavi) Can: {can1}", align="right", font=("Arial", 14, "bold"))


k1 = turtle.Turtle()
k1.speed(0)
k1.shape("turtle")
k1.turtlesize(2)
k1.color("blue")
k1.penup()
k1.goto(250, -250)

k2 = turtle.Turtle()
k2.speed(0)
k2.shape("turtle")
k2.turtlesize(2)
k2.color("red")
k2.penup()
k2.goto(-250, 250)

mermiler1 = []
mermiler2 = []


def k1_ates_bas():
    global mermi_var1, tus_basili1
    if not mermi_var1 and not tus_basili1:
        m = turtle.Turtle()
        m.shape("arrow")
        m.turtlesize(0.5)
        m.color("blue")
        m.penup()
        m.goto(k1.xcor(), k1.ycor())
        m.setheading(k1.heading())
        mermiler1.append(m)
        mermi_var1 = True
        tus_basili1 = True


def k1_ates_birak():
    global tus_basili1
    tus_basili1 = False


def k2_ates_bas():
    global mermi_var2, tus_basili2
    if not mermi_var2 and not tus_basili2:
        m = turtle.Turtle()
        m.shape("arrow")
        m.turtlesize(0.5)
        m.color("red")
        m.penup()
        m.goto(k2.xcor(), k2.ycor())
        m.setheading(k2.heading())
        mermiler2.append(m)
        mermi_var2 = True
        tus_basili2 = True


def k2_ates_birak():
    global tus_basili2
    tus_basili2 = False


def saga_bas(): global hareket_yon; hareket_yon = 0


def sola_bas(): global hareket_yon; hareket_yon = 180


def yukari_bas(): global hareket_yon; hareket_yon = 90


def asagi_bas(): global hareket_yon; hareket_yon = 270


def dur1(): global hareket_yon; hareket_yon = None


def saga_bas2(): global hareket_yon2; hareket_yon2 = 0


def sola_bas2(): global hareket_yon2; hareket_yon2 = 180


def yukari_bas2(): global hareket_yon2; hareket_yon2 = 90


def asagi_bas2(): global hareket_yon2; hareket_yon2 = 270


def dur2(): global hareket_yon2; hareket_yon2 = None


ekran.listen()
ekran.onkeypress(saga_bas, "6")
ekran.onkeypress(sola_bas, "4")
ekran.onkeypress(yukari_bas, "8")
ekran.onkeypress(asagi_bas, "5")
ekran.onkeyrelease(dur1, "6")
ekran.onkeyrelease(dur1, "4")
ekran.onkeyrelease(dur1, "8")
ekran.onkeyrelease(dur1, "5")
ekran.onkeypress(k1_ates_bas, "0")
ekran.onkeyrelease(k1_ates_birak, "0")

ekran.onkeypress(saga_bas2, "d")
ekran.onkeypress(sola_bas2, "a")
ekran.onkeypress(yukari_bas2, "w")
ekran.onkeypress(asagi_bas2, "s")
ekran.onkeyrelease(dur2, "d")
ekran.onkeyrelease(dur2, "a")
ekran.onkeyrelease(dur2, "w")
ekran.onkeyrelease(dur2, "s")
ekran.onkeypress(k2_ates_bas, "space")
ekran.onkeyrelease(k2_ates_birak, "space")

oyun_devam = True
canlari_guncelle()

while oyun_devam:
    ekran.update()

    if hareket_yon is not None:
        k1.setheading(hareket_yon)
        k1.forward(hiz)
    if k1.xcor() > 280: k1.setx(280)
    if k1.xcor() < -280: k1.setx(-280)
    if k1.ycor() > 280: k1.sety(280)
    if k1.ycor() < -280: k1.sety(-280)

    if hareket_yon2 is not None:
        k2.setheading(hareket_yon2)
        k2.forward(hiz)
    if k2.xcor() > 280: k2.setx(280)
    if k2.xcor() < -280: k2.setx(-280)
    if k2.ycor() > 280: k2.sety(280)
    if k2.ycor() < -280: k2.sety(-280)

    for m in mermiler1[:]:
        m.forward(mermi_hizi)
        if m.distance(k2) < 25:
            can2 -= 1
            canlari_guncelle()
            m.hideturtle()
            mermiler1.remove(m)
            mermi_var1 = False
        elif abs(m.xcor()) > 300 or abs(m.ycor()) > 300:
            m.hideturtle()
            mermiler1.remove(m)
            mermi_var1 = False

    for m in mermiler2[:]:
        m.forward(mermi_hizi)
        if m.distance(k1) < 25:
            can1 -= 1
            canlari_guncelle()
            m.hideturtle()
            mermiler2.remove(m)
            mermi_var2 = False
        elif abs(m.xcor()) > 300 or abs(m.ycor()) > 300:
            m.hideturtle()
            mermiler2.remove(m)
            mermi_var2 = False

    if can1 <= 0 or can2 <= 0:
        oyun_devam = False
        yazi.goto(0, 0)
        kazanan = "K1 (MAVİ)" if can2 <= 0 else "K2 (KIRMIZI)"
        yazi.write(f"OYUN BİTTİ\nKAZANAN: {kazanan}", align="center", font=("Arial", 24, "bold"))

    time.sleep(0.01)

turtle.done()