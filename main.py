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
   
