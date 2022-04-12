import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gameover import Gameover
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
screen.listen()
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_straight, key="Up")

scoreboard = Scoreboard()

car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()
    if player.ypos >= player.final_line_y:
        car_manager.delete_last_level_car()
        player.finish_a_turn()
        car_manager.level_up()
        scoreboard.level_update()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            gameover = Gameover()
            gameover.show_end()
            game_is_on = False

screen.exitonclick()