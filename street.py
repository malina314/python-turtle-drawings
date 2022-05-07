import math
from turtle import *
from random import random


def random_int(a, b):
    x = random()
    d = b - a + 1
    id = 1.0 / d
    res = x / id
    return a + int(res)


def square(a):
    for i in range(4):
        fd(a)
        rt(90)


def squares_in_row(n, a):
    rt(90)
    for i in range(n):
        square(a)
        up()
        fd(2 * a)
        down()
    up()
    bk(2 * n * a)
    lt(90)
    down()


def rect_of_squares(h, w, a):
    color('blue')
    begin_fill()
    for i in range(h):
        squares_in_row(w, a)
        up()
        fd(2 * a)
        down()
    end_fill()
    up()
    bk(2 * h * a)
    down()


def roof(w, h):
    color('red')
    begin_fill()
    rt(45)
    fd(h * 2 ** 0.5)
    rt(45)
    fd(w - 2 * h)
    rt(45)
    fd(h * 2 ** 0.5)
    rt(135)
    fd(w)
    rt(90)
    end_fill()


def building(h, w, a):
    color('green')
    begin_fill()
    for i in range(2):
        fd(2 * h * a + a)
        rt(90)
        fd(2 * w * a + a)
        rt(90)
    end_fill()
    up()
    fd(2 * a)
    rt(90)
    fd(a)
    lt(90)
    down()
    rect_of_squares(h, w, a)
    up()
    bk(2 * a)
    rt(90)
    bk(a)
    lt(90)
    fd(2 * h * a + a)
    down()
    roof(2 * w * a + a, a)
    up()
    bk(2 * h * a + a)
    down()
    color('black')


def street(w, n, step):
    up()
    goto(-w / 2, 0)
    down()
    for i in range(n):
        rt(90)
        fd(step)
        lt(90)
        building(random_int(3, 9), 3, 15)
        up()
        rt(90)
        fd(2 * 3 * 15 + 15)
        down()
        fd(step)
        lt(90)


def main():
    mode('logo')
    speed(0)

    street(window_width(), 5, 30)
    # for i in range(10):
    #     print(random_int(0, 4))


    done()


main()
