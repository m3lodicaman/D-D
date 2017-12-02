import turtle
turtle.speed("fastest")
turtle.hideturtle()
turtle.screensize(300, 300)
#make main bottom box
turtle.penup()
turtle.goto(300,-300)
turtle.pendown()
turtle.goto(0,-300)
turtle.goto(0,-100)
turtle.goto(300,-100)
turtle.goto(300,-300)
turtle.penup()
turtle.goto(0,-160)
turtle.pendown()
turtle.goto(300,-160)
#making other bottom boxes
for x in range(3):
    y = -100 * x
    turtle.penup()
    turtle.goto(0 + y,-300)
    turtle.pendown()
    turtle.goto(-100 + y,-300)
    turtle.goto(-100 + y,-150)
    turtle.goto(0 + y,-150)
    turtle.goto(0 + y,-300)
#writing in the boxes
turtle.penup()
turtle.goto(90,-140)
turtle.pendown()
name1 = input("Please input the name of the first player: ")
turtle.write(name1, font=("Arial", 20, "normal"),align="center")
