from turtle import Turtle

STARTING_SNAKE_SEGMENTS = 3

class Segment_Creator(Turtle):
    def __init__(self):
        self.segment_container = []
        for segment_count in range(STARTING_SNAKE_SEGMENTS):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.segment_container.append(self)
    
    def move(self):
        print(self.segment_container)
        self.segment_container[0].forward(1)