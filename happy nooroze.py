import turtle

def draw_rectangle(turtle, color, width, height, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

def draw_horizontal_ribbon(turtle, color, width, height, x, y):
    draw_rectangle(turtle, color, width, height, x - (width / 2), y)
    draw_rectangle(turtle, color, 20, 10, x - 10, y)

def write_nowruz_greeting(turtle, text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color('black')
    turtle.write(text, align="center", font=("B Nazanin", 24, "bold"))

wn = turtle.Screen()
wn.bgcolor("white")

gift = turtle.Turtle()
gift.speed('fastest')

draw_rectangle(gift, "saddle brown", 240, 20, -120, -20)

for i, color in enumerate(["forest green", "lime green", "dark green"]):
    draw_rectangle(gift, color, 80, 160, -120 + (i * 80), 0)

ribbon_height = 20
ribbon_width = 240 
draw_horizontal_ribbon(gift, "red", ribbon_width, ribbon_height, 0, 40)
write_nowruz_greeting(gift, "happy Norooz", 0, -100)

gift.hideturtle()

wn.mainloop()