import turtle

def draw_regular_polygon(num_sides, side_length):

    t = turtle.turtle()
    size = 100
    angle = 360/side_length
    t.pencolor('blue')
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()

    for i in range(num_sides+1):
        t.forward(size)
        t.right(angle)

    t.end_fill()