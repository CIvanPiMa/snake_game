from turtle import Turtle


ALIGN = ("center",)
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self._write_score()

    def refresh(self):
        self.clear()
        self.score += 1
        self._write_score()

    def _write_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over (Click to close!)", align=ALIGN, font=FONT)
