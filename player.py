from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.color("white")
        self.penup()
        self.left(90)
        self.go_to_starting_position()

        self.finish_line = 280
        self.move_distance = 10

    def move_up(self):
        self.forward(self.move_distance)

    def go_to_starting_position(self):
        self.goto(0, -280)

    def reached_top(self):
        if self.ycor() >= 300:
            self.go_to_starting_position()
            return True
        else: 
            return False
