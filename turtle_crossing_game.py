from turtle import Screen
from time import sleep
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

class TurtleCrossingGame():
    def __init__(self) -> None:

        self.game_still_on = True

        self.screen =  Screen()
        self.screen.title("Turtle Crossing Game")
        self.screen.bgcolor("black")
        self.screen.setup(600, 600)
        self.screen.tracer(0)

        self.scoreboard = Scoreboard()
        self.player = Player()
        self.car_manager = CarManager()

        self.screen.listen()
        self.screen.onkey(fun=self.player.move_up, key="w")

        self.main_loop()
    
        self.screen.exitonclick()
        
    def handle_finished_level(self):
        if self.player.reached_top():
            self.scoreboard.increment_level()
            self.car_manager.increase_speed()

    def handle_game_over(self):
        if self.car_manager.check_crash(self.player):
            self.game_still_on = False
            self.scoreboard.game_over()

    def main_loop(self):
        while self.game_still_on:
            sleep(0.1)
            self.screen.update()
            self.car_manager.generate_car()
            self.car_manager.move_cars()
            self.handle_game_over()
            self.handle_finished_level()
            
