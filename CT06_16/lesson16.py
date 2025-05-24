import turtle
def create_balls():
    ball=turtle.Turtle()
    ball.shape("ball")
    ball.col

def setupwindow(width,height):
    window=turtle.Screen()
    window.setup(width,height)
    # return the window here
    return window

screen=setupwindow(300,500)

screen.mainloop()