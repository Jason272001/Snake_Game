from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,350 )
        self.write( f"Your Score: {self.score} ",align="center", font=("Arial",25,"normal"))
        self.hideturtle()
        self.update()


    def update(self):
        self.write( f"Your Score: {self.score} ",align="center", font=("Arial",25,"normal"))



    def increase(self):

        self.score+=1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over ", align="center", font=("Arial", 25, "normal"))
