from turtle import *
from shapes import *


def flower(n, size):
    for i in range(n):
        rt(360 / n)
        square(size)


def flower2(n, size):
    delta = size / n
    for i in range(n):
        rt(360 / n)
        square(size)
        size = size - delta


def dot_line(dot_size, n):
    for i in range(n):
        dot(dot_size, "purple")
        up()
        fd(dot_size)
        down()
    up()
    bk(dot_size * n)
    down()


def dot_square(dot_size, n):
    for i in range(n):
        dot_line(dot_size, n)
        up()
        rt(90)
        fd(dot_size)
        lt(90)
        down()
    up()
    lt(90)
    fd(n * dot_size)
    rt(90)
    down()


def golden_spiral(squares_cnt):
    a = 1
    b = 0
    for _ in range(squares_cnt):
        step = a / 10
        for _ in range(90):
            fd(step)
            lt(1)
        c = b
        b = a
        a += c
