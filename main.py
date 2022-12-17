import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Turtle,Screen

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()

        scoreboard.gameover()
        game_is_on=False

    for i in snake.segments:
        if i == snake.head:
            pass
        elif snake.head.distance(i)<5:
            game_is_on=False
            scoreboard.gameover()



screen.exitonclick()











