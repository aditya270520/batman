import turtle
import math

kalam = turtle.Turtle()
kalam.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
kalam.color("yellow")

aditya = 20

kalam.left(90)
kalam.penup()
kalam.goto(-7 * aditya, 0)
kalam.pendown()

for a in range(-7 * aditya, -3 * aditya, 1):
    x = a / aditya
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * aditya)

for a in range(-3 * aditya, -1 * aditya - 1, 1):
    x = a / aditya
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * aditya)

kalam.goto(-1 * aditya, 3 * aditya)
kalam.goto(int(-0.5 * aditya), int(2.2 * aditya))
kalam.goto(int(0.5 * aditya), int(2.2 * aditya))
kalam.goto(1 * aditya, 3 * aditya)
print("Batman Logo with Python Turtle")
for a in range(1 * aditya + 1, 3 * aditya + 1, 1):
    x = a / aditya
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * aditya)

for a in range(3 * aditya + 1, 7 * aditya + 1, 1):
    x = a / aditya
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * aditya)

for a in range(7 * aditya, 4 * aditya, -1):
    x = a / aditya
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * aditya)

for a in range(4 * aditya, -4 * aditya, -1):
    x = a / aditya
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    kalam.goto(a, y * aditya)

for a in range(-4 * aditya - 1, -7 * aditya - 1, -1):
    x = a / aditya
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * aditya)

kalam.penup()
kalam.goto(300, 300)
turtle.done()