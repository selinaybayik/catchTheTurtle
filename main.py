import turtle
import random
import time


turtle_screen=turtle.Screen()
turtle_screen.title("Catch the Turtle Game")
turtle_screen.bgcolor("#F1CAAB")
turtle_screen.setup(width=600,height=600)
turtle_screen.tracer(0)

kaplumbaga=turtle.Turtle()
kaplumbaga.speed(0)
kaplumbaga.shape("turtle")
kaplumbaga.color("black","green")
kaplumbaga.shapesize(1)
kaplumbaga.penup()
kaplumbaga.goto(random.randint(-400,300),random.randint(-400,300))

def puan(x,y): #click yapılan konumun değerlerini gönderir
    global p
    p=p+1
    score.clear()
    score.write("Score:{}".format(p), move=False, align="center", font=("Cambria", 20, "normal"))
    kaplumbaga.goto(random.randint(-300, 300), random.randint(-300, 300))


score=turtle.Turtle()
score.shape("square")
score.color("black")
score.speed(0)
score.penup()
score.goto(0,260)
score.hideturtle()
score.write("Start:",move=False,align="center",font=("Cambria",20,"normal"))

start = time.time()
p=0
sure=turtle.Turtle()
sure.shape("square")
sure.color("black")
sure.speed(10)
sure.penup()
sure.goto(0,220)
sure.hideturtle()
sure.write("Time",move=False,align="center",font=("Cambria",20,"normal"))


while True:
      start = time.time()
      while time.time()-start <21:
        sure.clear()
        sure.write("Time:{}".format(int(time.time()-start)), align="center", font=("Cambria", 20, "normal"))
        sure.hideturtle()
        turtle_screen.update()
        kaplumbaga.onclick(puan)
      else:
        score.clear()
        score.write("Score:{}".format(p), move=False, align="center", font=("Cambria", 20, "normal"))
        time.sleep(2)
        p=0
        score.clear()
        score.write("Start:", move=False, align="center", font=("Cambria", 20, "normal"))
        kaplumbaga.onclick(puan)

turtle.mainloop()