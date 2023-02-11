from turtle import Turtle, Screen, speed
import random


colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4", "blue4"]
rotation = [0, 90, 180, 270, 360]
speed = 10
tommy = Turtle()
tommy.shape("turtle")

for number in range(200):
    tommy.forward(30)
    tommy.right(random.choice(rotation))

    color = random.choice(colors)
    tommy.pencolor(color)

    if number <= 10:
        tommy.pensize(number)

    tommy.speed(speed)
    speed += 1




window = Screen()
window.exitonclick()