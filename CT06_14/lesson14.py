
import turtle as t

window = t.Screen()

window.setup(width=600,height=400)
turtle=t.Turtle()
turtle.shape("turtle")
turtle.fillcolor("orange")
turtle.seth(180)
for i in range(100):
    turtle.down(10)
    turtle.forward(4)
    turtle.left(1)
window.mainloop()

