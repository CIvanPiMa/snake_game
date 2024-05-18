import time
from snake_game.snake import Snake
from snake_game.screen_setup import set_screen, set_listeners
from snake_game.food import Food
from snake_game.score import Score


if __name__ == "__main__":
    game_is_on = True
    snake = Snake()
    food = Food()
    score = Score()
    screen = set_screen()
    set_listeners(screen, snake)

    while game_is_on:
        screen.update()
        snake.move()
        time.sleep(0.1)
        if snake.head.distance(food) < 20:
            score.refresh()
            food.refresh()
            snake.extend()
        if snake.is_game_over():
            game_is_on = False
            score.game_over()

    screen.exitonclick()
