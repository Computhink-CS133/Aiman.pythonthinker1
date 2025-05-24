import turtle
def moveBall(ball,dx,dy):
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
    

def create_balls():
    ball=turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.up() 
    return ball

def setupwindow(width,height):
    window=turtle.Screen()
    window.setup(width,height)
    # return the window here
    return window

screen=setupwindow(300,500)
balls=create_balls()

for i in range(100)
    moveBall(balls,100,100)

screen.mainloop()