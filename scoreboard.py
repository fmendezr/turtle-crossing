from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.level = 1

        self.penup()
        self.hideturtle()
        self.color("white")

        self.goto(-280,260)
        self.write_level()
    
    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increment_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 60, "normal"))