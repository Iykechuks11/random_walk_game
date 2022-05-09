import turtle as t
import random

move = t.Turtle()
color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
         "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
move.width(5)
move.speed("fast")

# Solution one
# start_moves = 0
# end_moves = 100

# while start_moves < end_moves:
#     move.width(5)
#     move.color(random.choice(color))
#     move.forward(30)
#     move.seth(random.choice(directions))
#     start_moves += 1
#     if start_moves == end_moves:
#         break


# Solution two
for _ in range(200):
    move.color(random.choice(color))
    move.forward(30)
    move.setheading(random.choice(directions))






screen = t.Screen()
screen.exitonclick()
