from turtle import Screen

from pong_main import start_pong_game
from snake_main import start_snake_game


if __name__ == '__main__':
    screen = Screen()
    screen.title('Snake and Pong')
    screen.bgcolor('black')
    screen.setup(width=450, height=350)
    user_choice = screen.textinput('Select your game', prompt='Type "pong" or "snake": ')

    if user_choice == 'pong':
        try:
            start_pong_game()
        except Exception:
            pass
    elif user_choice == 'snake':
        try:
            start_snake_game()
        except Exception:
            pass
