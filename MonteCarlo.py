import math
from random import random
from turtle import *
from shapes import *


def monte_carlo(n):
    cnt = 0
    for _ in range(n):
        x = random()
        y = random()
        if x ** 2 + y ** 2 < 1:
            cnt += 1
    return cnt / n * 4


# print(monte_carlo(10000000))

def random_dot_size(minimum):
    x = random()
    size = minimum - 1
    sum = 0
    k = 1
    while sum < x:
        size += 1
        k *= 2
        sum += 1 / k
    if size == minimum + 1 and random() < 0.33:
        size += int(random() * random_dot_size(6))
    return size


def draw_monte_carlo(n):
    scale = 6.6
    a = 115.6 * scale
    cnt = 0
    mode("logo")
    speed(0)
    width = window_width()
    height = window_height()
    up()
    shift_x = -width / 2 + 10
    shift_y = -height / 2 + 15
    goto(shift_x, shift_y)
    down()
    pensize(3)
    square(a)
    up()
    fd(a)
    down()
    rt(90)
    for _ in range(90):
        fd(2 * scale)
        rt(1)
    for _ in range(n):
        x = random()
        y = random()
        if x ** 2 + y ** 2 < 1:
            color("red")
            cnt += 1
        else:
            color("blue")
        up()
        goto(x * a + shift_x, y * a + shift_y)
        down()
        dot(random_dot_size(3))
    print(f"pi approximation is {cnt / n * 4}")
    done()


draw_monte_carlo(50000)





