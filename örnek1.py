#mor renkli kare çizdirdi
"""import turtle
t=turtle.Turtle()
t.shape("turtle")
t.begin_fill() #bundan sonra gelecek fonkları uygula
t.fillcolor("purple")
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
turtle.mainloop()"""

#circle ve poligon karışık
"""import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("burlywood")
turtle_screen.title("circle")

turtle_instance=turtle.Turtle()
turtle_instance.color("black")
turtle.speed(10)
turtle_instance.circle(150)
turtle_instance.circle(150,90)
turtle_instance.circle(120)
turtle_instance.circle(120,90)
turtle_instance.circle(90)
turtle_instance.circle(90,steps=8)
turtle_instance.circle(60,steps=6)
turtle_instance.circle(60,90)
turtle_instance.circle(30,steps=5)
turtle_instance.circle(30,90)
turtle.mainloop()"""

"""import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("gray")
t.speed(6)
for i in range(50):
    if i%2==0:
        t.color("red")
        t.circle(i,steps=8)
    elif i%5==0:
        t.color("pink")
        t.circle(i,steps=8)
    else:
        t.color("blue")
        t.circle(i,steps=8)
turtle.mainloop()"""

#örnek
"""import turtle
t=turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.up()
t.goto(100,100)
t.down()
turtle.mainloop()"""

#örnek
"""import turtle
t=turtle.Turtle()
t.circle(50)
t.up()
t.goto(100,-100)
t.down()
t.circle(50)
turtle.mainloop()"""
import time
import turtle

window = turtle.Screen()
window.tracer(0)

player = turtle.Turtle()
timer_text = turtle.Turtle()

start = time.time()
while time.time() - start < 5:
    player.forward(1)
    player.left(1)
    timer_text.clear()
    timer_text.write(int(time.time() - start), font=("Courier", 30))

    window.update()

turtle.done()
import time
junk = time.clock()
pause_at_bottom = 0.5
## code till it hits the bottom
at_bottom = time.clock()
while time.clock() < (at_bottom + pause_at_bottom):
    ## code to run while at the bottom
## code to run once time has elapsed at bottom