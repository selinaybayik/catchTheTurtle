import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("#A7A5F2")
drawing_board.title("python uygulaması")

"""t=turtle.Turtle()
t.shape("square")
t.begin_fill()
t.fillcolor("black")
turtleColors=["blue","red","lightblue","yellow","coral","orange","black"]
for i in range(4):
      t.color(turtleColors[i%7]) #böyle içi en son hangi renkse onla doldu ama yanlarda renkli
      t.forward(100)
      t.left(90) #90 kare 120 üçgen

t.end_fill()
turtle.mainloop()"""

import turtle

t = turtle.Turtle()

for i in range(36):
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(100)

turtle.done()