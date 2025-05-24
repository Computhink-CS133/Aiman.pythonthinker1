import turtle

window=turtle.Screen()

t=turtle.Turtle()

def DrawShapes(length,num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.left(360/num_sides)

DrawShapes()

window.mainloop()