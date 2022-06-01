from turtle import Turtle
import random

class food_spawner(Turtle):
    def __init__(self):
        super().__init__()
        self.food = Turtle(shape = "circle")
        self.color("blue")
        self.penup()
        self.spawn()

    def spawn(self):
        self.goto(random.randint(-390,390), random.randint(-390,390))