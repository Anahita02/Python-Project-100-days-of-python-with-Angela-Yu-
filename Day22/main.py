from turtle import Screen
from paddel import Paddel
from ball import Ball
import time
from scoreboard import Scoreboard

Screen = Screen()
Screen.setup(width=800, height=600)
Screen.bgcolor("black")
Screen.title("Pong")
Screen.tracer(0)

right_paddel = Paddel((350, 0))
left_paddel = Paddel((-350, 0))

Screen.listen()
Screen.onkey(right_paddel.up, "Up")
Screen.onkey(right_paddel.down, "Down")
Screen.onkey(left_paddel.up, "w")
Screen.onkey(left_paddel.down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    Screen.update()
    ball.move()

    # Detecting the collision with wall
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddels
    if ball.distance(right_paddel) < 50 and ball.xcor() > 320 or ball.distance(left_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddel misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_player_point()

    # Detect left paddel misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_player_point()


Screen.exitonclick()