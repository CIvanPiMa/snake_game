from turtle import Turtle
from typing import List


SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snake_segments: List[Turtle] = []
        self._create_snake()
        self.head = self.snake_segments[0]

    def _create_snake(self) -> None:
        for position in SNAKE_STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_index - 1].xcor()
            new_y = self.snake_segments[segment_index - 1].ycor()
            self.snake_segments[segment_index].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
