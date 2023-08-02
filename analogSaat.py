import turtle
import time

turtleScreen=turtle.Screen()
turtleScreen.setup(width=450,height=450)
turtleScreen.bgcolor("light blue")
turtleScreen.title("analog saat")
turtleScreen.tracer(0)

kalem=turtle.Turtle()
kalem.speed(6)
kalem.pensize(3)


def cizim(saat,dakika,saniye,kalem):
    kalem.begin_fill()
    kalem.color("black")
    kalem.up()
    kalem.goto(0,210)
    kalem.setheading(180)
    kalem.color("black")
    kalem.pendown()
    kalem.circle(210)
    kalem.end_fill()

    kalem.penup()
    kalem.goto(0,0)
    kalem.setheading(90)
    kalem.begin_fill()
    kalem.color("white")
    for i in range(12):
        kalem.forward(190)
        kalem.pendown()
        kalem.forward(20)
        kalem.penup()
        kalem.goto(0,0)
        kalem.rt(30)
    kalem.end_fill()
   #saat
    kalem.penup()
    kalem.goto(0,0)
    kalem.color("yellow")
    kalem.setheading(90)
    bilgi=(saat/12)*360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(100)
    #dakika
    kalem.penup()
    kalem.goto(0, 0)
    kalem.color("purple")
    kalem.setheading(90)
    bilgi = (dakika / 60) * 360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(80)
    #saniye
    kalem.penup()
    kalem.goto(0, 0)
    kalem.color("orange")
    kalem.setheading(90)
    bilgi = (saniye / 60) * 360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(50)

while True:
    saat=int(time.strftime("%I"))
    dakika= int(time.strftime("%M"))
    saniye= int(time.strftime("%S"))

    cizim(saat, dakika, saniye, kalem)
    turtleScreen.update()
    kalem.clear()

turtleScreen.mainloop()




