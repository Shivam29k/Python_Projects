# import colorgram

# colors = colorgram.extract('hirst.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

rgb_colors = [(241, 228, 89), (24, 24, 61), (183, 73, 38), (144, 17, 31), (39, 29, 21), (214, 145, 85), (124, 159, 216), (204, 73, 115), (68, 26, 35), (55, 92, 138), (37, 45, 126), (23, 33, 23), (161, 21, 14), (142, 57, 80), (71, 78, 32), (67, 113, 74), (100, 98, 192), (141, 178, 161), (207, 77, 62), (144, 213, 191), (98, 168, 76), (192, 141, 156), (49, 85, 26), (156, 210, 221), (225, 172, 184), (175, 185, 221), (231, 174, 164), (163, 162, 78), (89, 143, 152), (30, 71, 96)]
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.setheading(220)
tim.penup()
tim.forward(350)
tim.setheading(0)
for __ in range(10):

    for _ in range(12):
        tim.pendown()
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        if _ != 11:
            tim.forward(50)
    if __ % 2 == 0 or __ == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)

        
    

screen = turtle_module.Screen()
screen.exitonclick()