import turtle

def draw_heart():
    turtle.bgcolor("black")  
    turtle.pensize(3)  
    turtle.speed(3)  
    turtle.color("red")  

    turtle.begin_fill()
    turtle.fillcolor("red")  

    turtle.left(140)
    turtle.forward(180)  

    turtle.circle(-90, 200)  
    turtle.left(120)
    turtle.circle(-90, 200) 

    turtle.forward(180)  

    turtle.end_fill()
    turtle.hideturtle()  

    turtle.penup()
    turtle.goto(-40, -150)  
    turtle.color("white")
    turtle.write("  For  You", font=("Arial", 24, "bold"), align="center")
    turtle.hideturtle()
    turtle.done()

draw_heart()