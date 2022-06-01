from turtle import Screen
from time import sleep
import snake
import food

GAME_IS_ON = True

mainapp = Screen()
mainapp.bgcolor("white")
mainapp.screensize(canvheight = 800, canvwidth = 800)
mainapp.tracer(0)
mainapp.listen()
snake_body = snake.Segment_Creator()
snake_food = food.food_spawner()
while GAME_IS_ON:
    sleep(.01)
    mainapp.update()
    snake_body.move()
    mainapp.onkeypress(fun = snake_body.up, key = "Up")
    mainapp.onkeypress(fun = snake_body.down, key = "Down")
    mainapp.onkeypress(fun = snake_body.left, key = "Left")
    mainapp.onkeypress(fun = snake_body.right, key = "Right")
    if snake_food.distance(snake_body.segment_container[0]) <= 15:
        snake_food.spawn()
        snake_body.score()