from turtle import Turtle 
from random import choice, randint

class Car(Turtle):
    def __init__(self, color, y_cord, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.turtlesize(1, 2)
        self.color(color)
        self.penup()
        self.goto(300, y_cord)
        self.left(180)

class CarManager:
    def __init__(self) -> None:

        self.cars = []

        self.y_coords = [x for x in range(-240, 260, 20)]
        self.colors  = ["red", "orange", "blue", "gold", "purple", "aquamarine", "green", "brown", "pink", "darkorchid", "cyan", "gray", "coral", "burlywood", "aliceblue"]
        self.speed = 5
        self.speed_increment = 5


    def generate_car(self):
        if randint(1, 6) == 1:
            car = Car(choice(self.colors), choice(self.y_coords))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
    
    def increase_speed(self):
        self.speed += self.speed_increment
    
    def check_crash(self, obj):
        for car in self.cars:
            if car.distance(obj) < 20:
                return True
        return False