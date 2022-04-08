from turtle import *


def half_circle(step):
    for _ in range(180):
        fd(step)
        rt(1)


def square(a):
    for _ in range(4):
        fd(a)
        rt(90)
