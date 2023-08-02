"""import turtle
turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.pensize(5)

for i in range(10):
    t.begin_fill()
    t.color("blue")
    t.rt(90)
    t.pencolor("green")
    t.circle(60,360)
    t.rt(120)
    t.pencolor("brown")
    t.circle(90,360)
    t.rt(120)
    t.pencolor("orange")
    t.circle(150)

turtle_screen.mainloop()"""


#örnek
"""import turtle
wn=turtle.Screen()
wn.bgcolor("#A5F2C8")

t=turtle.Turtle()
t.speed(0)

for i in range(100):
    t.circle(5*i)
    t.circle(-5*i)
    turtle.left(i)"""

#square
"""import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("square")

turtle_instance=turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)"""

"""for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)

drawing_board.mainloop()"""

#star çizme
#import turtle
#drawing_board=turtle.Screen()
#drawing_board.bgcolor("light blue")
#drawing_board.title("square")

#urtle_instance=turtle.Turtle()
#for i in range(5):
    #turtle_instance.left(144)
    #turtle_instance.forward(100)

#çokgenler çizme
#kenar=6
#derece=360.0/kenar
#side_lenght=80
# for i in range(kenar):
    #turtle_instance.left(derece)
    #turtle_instance.forward(side_lenght)

#drawing_board.mainloop()

#örnek
import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("#3EF2BC")
turtle_screen.title("Turtle Python")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

def squareFonk(size):
    for i in range(5):
      turtle_instance.forward(size)
      turtle_instance.left(90)
      size=size-5

squareFonk(150)
squareFonk(130)
squareFonk(110)
squareFonk(90)
squareFonk(70)
squareFonk(50)
squareFonk(30)
squareFonk(10)
turtle.done()