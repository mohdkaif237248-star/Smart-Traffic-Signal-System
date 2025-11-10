"""
signal_simulation.py
Simple 2-road traffic-light simulation using turtle.
Run: python3 signal_simulation.py
It will ask for vehicle counts for Road A and Road B, then show a simple traffic light animation.
"""
import turtle
import time

def draw_signal(x, y):
    body = turtle.Turtle()
    body.hideturtle()
    body.penup()
    body.goto(x-30, y+80)
    body.pendown()
    body.color("white")
    body.begin_fill()
    for _ in range(2):
        body.forward(60)
        body.right(90)
        body.forward(160)
        body.right(90)
    body.end_fill()
    return

def make_light(x, y):
    t = turtle.Turtle()
    t.shape("circle")
    t.shapesize(2.5)
    t.penup()
    t.goto(x, y)
    t.color("black")
    return t

def show_sequence(light, color, secs):
    # turn off all lights first
    for L in lights:
        L.color("black")
    light.color(color)
    time.sleep(secs)

# Setup screen
wn = turtle.Screen()
wn.title("Smart Traffic Signal - 2 Road Simulation")
wn.bgcolor("grey20")

draw_signal(-150, 0)  # left signal
draw_signal(150, 0)   # right signal

# lights for Road A (left) and Road B (right)
redA = make_light(-150, 60)
yellowA = make_light(-150, 0)
greenA = make_light(-150, -60)

redB = make_light(150, 60)
yellowB = make_light(150, 0)
greenB = make_light(150, -60)

lights = [redA, yellowA, greenA, redB, yellowB, greenB]

# take input
try:
    roadA = int(wn.numinput("Input", "Vehicles on Road A (0-100):", minval=0, maxval=999))
    roadB = int(wn.numinput("Input", "Vehicles on Road B (0-100):", minval=0, maxval=999))
except:
    roadA = 5
    roadB = 5

# Decide which road gets green
if roadA > roadB:
    green_time = max(5, roadA)  # minimum 5 seconds
    sequence = [("A", green_time)]
elif roadB > roadA:
    green_time = max(5, roadB)
    sequence = [("B", green_time)]
else:
    sequence = [("A", 10), ("B", 10)]

# run sequence once
for who, secs in sequence:
    if who == "A":
        # A green, B red
        show_sequence(greenA, "green", min(6, secs))   # show green (short for demo)
        show_sequence(yellowA, "yellow", 2)
        show_sequence(redA, "red", 0.5)
    else:
        show_sequence(redB, "red", 0.5)
        show_sequence(greenB, "green", min(6, secs))
        show_sequence(yellowB, "yellow", 2)

wn.bye()