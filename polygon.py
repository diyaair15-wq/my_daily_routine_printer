import turtle  
turtle.Screen().bgcolor("red")
turtle.Screen().screensize(300,400)
polygon = turtle.Turtle()

num_sides = 11
side_length = 22
angle = 360 / num_sides

for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
