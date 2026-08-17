from turtle import Turtle

class Ball(Turtle): # creates ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.colourList = ["red","green","blue","orange","yellow","pink","white"]

    def ball_movement(self): # ball movement
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def bounce_y(self): # ball bounce if it touches roof or floor
        self.y_move *= -1



    def bounce_x(self): # ball bounce for touching paddles
        self.x_move *= -1


    def reset_position(self): # reset position after score
        self.goto(0,0)
        self.bounce_x()


