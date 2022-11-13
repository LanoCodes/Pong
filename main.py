from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Let's Play Pong")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")




game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    #detection of wall,
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()





screen.exitonclick()

# All to-dos
# TODO 1. Create the screen
#   done
# TODO 2. Create and move a paddle
# TODO 3. Create another paddle
# TODO 4. Create the ball and make it move
# TODO 5. Detect collision with wall and bounce
# TODO 6. Detect collision with paddle
# TODO 7. Detect when paddle misses
# TODO 8. Keep score