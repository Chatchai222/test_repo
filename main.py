import math
import turtle as tur

"""
This is a program/project for drawing stuff using turtle
but more importantly for learning git and github...
"""

def square(t, length):
    # t stands for turtle
    for _ in range(4):
        t.forward(length)
        t.right(90)

def triangle(t, length):
    # t stands for turtle
    # This func is another dev say "CoolDev69"
    for _ in range(3):
        t.forward(length)
        t.right(120)
   
def polygon(t, length, sides):
    internal_angle = ((sides-2) * 180) / sides
    external_angle = 180 - internal_angle
    for _ in range(sides):
        t.forward(length)
        t.right(external_angle)
    