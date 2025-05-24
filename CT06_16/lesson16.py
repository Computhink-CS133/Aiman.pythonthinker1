import turtle
def moveBall(ball,dx,dy):
    right=True
    if ball.xcor()>=300:
        right=False
    else:
        right=True
    if right:
        ball.setx(ball.xcor()+dx)
    else:
        ball.setx(ball.xcor()-dx)
    ball.sety(ball.ycor()+dy)
    

def create_balls():
    ball.setx=0
    ball.sety=0
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

while True:
    moveBall(balls,2,2)

screen.mainloop()