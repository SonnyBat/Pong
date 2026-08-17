from turtle import Turtle, Screen
from paddles import Paddles
from ball import Ball
import time
from scoreboard import Scoreboard
import random

# screen settings
screen = Screen() # creates screen object
screen.setup(width=800, height=600) # sets screen size and height
screen.bgcolor("black") # sets background black
screen.title("Pong") # sets title gui Pong
screen.tracer(0) # turns off starting animation to hide drawing


# creates two paddles and puts location
paddleRight = Paddles(y = 350,x = 0)
paddleLeft = Paddles(y = -350,x = 0)

ball = Ball()
scoreboard = Scoreboard()

# screen listeners checking for key presses for both paddles
screen.listen()
screen.onkey(paddleRight.go_up, "Up")
screen.onkey(paddleRight.go_down, "Down")
screen.onkey(paddleLeft.go_up, "w")
screen.onkey(paddleLeft.go_down, "s")





game_is_on = True # keeps game active via while loop while True
while game_is_on:
    ball.ball_movement() # calls ball movement from ball object
    time.sleep(0.1) # sets sleep timer to slow down ball
    screen.update() # manually updates game while active

    # collission checks
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddleRight.paddle) < 50 and ball.xcor() > 320 or ball.distance(paddleLeft.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.color(random.choice(ball.colourList))
    # check if right paddle misses
    if ball.xcor() > 380:
        scoreboard.r_score_point()
        ball.reset_position()

    # check if left paddle misses
    if ball.xcor() < -380:
        scoreboard.l_score_point()
        ball.reset_position()
screen.exitonclick()