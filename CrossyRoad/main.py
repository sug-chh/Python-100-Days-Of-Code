import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
SPEED_MODIFIER = 0.5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)



game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    car.create_car()
    car.move_cars()



    #Detects the collision with the car

    for single_car in car.all_cars:
        if single_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

#Detects successful crossing
    if player.is_at_finish_line() :
        player.goto_to_start()
        scoreboard.increment_score()
        car.move_speed = car.move_speed * SPEED_MODIFIER


screen.exitonclick()