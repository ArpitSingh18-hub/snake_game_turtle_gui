from turtle import Screen,Turtle
import time
from scoreboard import Scorecard
from snake import Snake
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE XNEZIA")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor( ) > 290 or snake.head.xcor( ) <-290 or snake.head.ycor( ) >290 or snake.head.ycor( ) < -290 :
       scoreboard.reset()
       snake.reset()

    #Detect collision with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()