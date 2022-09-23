import time
from turtle import Screen

from pong_ball import Ball
from pong_control import WatchedKey
from pong_paddle import Paddle
from pong_scoreboard import Scoreboard


def start_pong_game():
    screen = Screen()
    screen.title('Pong')
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.title('Pong')
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    watched_keys = [WatchedKey(key) for key in ['Up', 'Down', 'w', 's']]

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Move right paddle
        if watched_keys[0].down and not watched_keys[1].down and not r_paddle.ycor() > 240:
            r_paddle.go_up()
        elif not watched_keys[0].down and watched_keys[1].down and not r_paddle.ycor() < -220:
            r_paddle.go_down()

        # Move left paddle
        if watched_keys[2].down and not watched_keys[3].down and not l_paddle.ycor() > 240:
            l_paddle.go_up()
        elif not watched_keys[2].down and watched_keys[3].down and not l_paddle.ycor() < -220:
            l_paddle.go_down()

        # Detect r_paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        # Detect l_paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()

        # Stop the game when one player's score is 10
        if score.l_score == 10 or score.r_score == 10:
            game_is_on = False
            score.game_over()

    screen.exitonclick()
