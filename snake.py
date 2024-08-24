from turtle import Turtle
POSITION = [(0, 0), (-15, 0), (-30, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :
        def __init__(self):
            self.blocks = []
            self.create_snake()
            self.head = self.blocks[0]
        def create_snake(self):
            for positions in POSITION:
               self.add_block(positions)

        def add_block(self,positions):
            block = Turtle('square')
            block.color('white')
            block.penup()
            block.goto(positions)
            self.blocks.append(block)
        def extend(self):
            self.add_block(self.blocks[-1].position())

        def move(self):

            for block_num in range(len(self.blocks) - 1, 0, -1):
                newX = self.blocks[block_num - 1].xcor()
                newY = self.blocks[block_num - 1].ycor()
                self.blocks[block_num].goto(newX, newY)

            self.head.forward(MOVE_DISTANCE)


        def up(self):
            if self.head.heading() !=DOWN:
                self.head.setheading(UP)
        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)