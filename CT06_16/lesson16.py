import turtle
def check_x(ball,screenwidth):
    return ball.xcor()>(screenwidth/2) or ball.xcor()<(-screenwidth/2)
def moveBall(ball,dx,dy):

    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
def check_y(ball,screenheight):
    return ball.ycor()>(screenheight/2) or ball.ycor()<(-screenheight/2)
def drawBorder(ball,width,height):
    ball.setx(width)
    ball.sety(height)
    ball.forward()

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

dx=2
dy=2


while True:
    moveBall(balls,dx,dy)
    if check_x(balls,300):
        dx*=-1
    if check_y(balls,500):
        dy*=-1
screen.mainloop()