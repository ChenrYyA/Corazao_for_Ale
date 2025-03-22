import turtle
import random

pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("corazao")
pantalla.setup(width=800, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def dibujar_corazon_grande():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

    for _ in range(10):
        t.penup()
        angle = random.randint(0, 360)
        dist = random.randint(140, 170)
        t.goto(0, -50)
        t.setheading(angle)
        t.forward(dist)
        t.pendown()
        t.color("pink")
        t.dot(random.randint(5, 10))

def dibujar_corazon_pequeño(x, y, tamaño):
    mini = turtle.Turtle()
    mini.hideturtle()
    mini.penup()
    mini.goto(x, y)
    mini.pendown()
    mini.color("hot pink")
    mini.begin_fill()
    mini.left(50)
    mini.forward(tamaño)
    mini.circle(tamaño / 2, 200)
    mini.right(140)
    mini.circle(tamaño / 2, 200)
    mini.forward(tamaño)
    mini.end_fill()

def corazones_esquinas():
    for _ in range(30):
        x = random.choice([random.randint(-380, -250), random.randint(250, 380)])
        y = random.choice([random.randint(-280, -150), random.randint(150, 280)])
        tamaño = random.randint(10, 20)
        dibujar_corazon_pequeño(x, y, tamaño)

def mensaje():
    t.penup()
    t.goto(0, 250)
    t.color("white")
    t.write("i love you my guuuurlll", align="center", font=("Courier", 16, "bold"))

corazones_esquinas()
dibujar_corazon_grande()
mensaje()

pantalla.mainloop()
