from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()

screen.setup(width=800, height=800)

screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
score=Score()
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

x = snake.head.xcor()
y = snake.head.ycor()

game_is_on=True

while game_is_on:
        screen.update()
        time.sleep(0.16)
        snake.move()

        if snake.head.distance(food)<15:
                food.refresh()
                score.increase()
                snake.extend()

        if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
                game_is_on = False
                score.gameover()
        for block in snake.blocks:
                if block==snake.head:
                        pass
                elif snake.head.distance(block)<8:
                        game_is_on=False
                        score.gameover()

screen.exitonclick()