from turtle import Turtle
class Paddles(Turtle): # paddles size shape stopping pen
    def __init__(self, y , x):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(y, x)

    def go_up(self): # method that makes paddle move up when key pressed
        new_y = self.paddle.ycor() + 25
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self): # method that makes it go down when key pressed
        new_y = self.paddle.ycor() - 25
        self.paddle.goto(self.paddle.xcor(), new_y)


