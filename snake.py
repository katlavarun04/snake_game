from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        else:
            pass
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        else:
            pass
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
        else:
            pass
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
        else:
            pass