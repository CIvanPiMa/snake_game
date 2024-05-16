import time
from snake_game.snake import Snake
from snake_game.screen_setup import set_screen, set_listeners

game_is_on = True

if __name__ == "__main__":
    snake = Snake()
    screen = set_screen()
    set_listeners(screen, snake)

    while game_is_on:
        screen.update()
        snake.move()
        time.sleep(0.1)
