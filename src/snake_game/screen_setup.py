from turtle import Screen, _Screen
from snake_game.snake import Snake


def set_screen() -> _Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def set_listeners(screen: _Screen, snake: Snake) -> None:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
