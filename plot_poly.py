from turtle import *

mode("logo")
speed(0)


def eval_poly(x_0, coefs):
    x = 1
    res = 0
    for c in coefs:
        res += c * x
        x *= x_0
    return res


def draw_axis(scale):
    vw = 500
    vh = 400

    pensize(1)

    # X axis
    up()
    goto(-vw, 0)
    down()
    goto(vw, 0)

    # Y axis
    up()
    goto(0, -vh)
    down()
    goto(0, vh)

    up()
    goto(0, 0)
    down()

    if scale:
        scale_lines_height = 4
        for x in range(-vw, vw, scale):
            up()
            goto(x, -scale_lines_height)
            down()
            goto(x, scale_lines_height)
        for y in range(-vh, vh, scale):
            up()
            goto(-scale_lines_height, y)
            down()
            goto(scale_lines_height, y)


# coefs[i] is coef of x^i
def plot(a, b, poly_coefs, step, scale, axis, col):
    color(col)
    if axis:
        draw_axis(scale)
    pensize(2)
    x = a
    value = eval_poly(x, poly_coefs)
    up()
    goto(x * scale, value * scale)
    down()
    while x <= b:
        value = eval_poly(x, poly_coefs)
        goto(x * scale, value * scale)
        x += step
    pensize(1)
    color("black")


plot(-3., 3., [0, 0, 1], 0.1, 20, True, "black")
plot(-2.3, 9., [-4.4, 3.7, 2.4, -1.14, 0.1], 0.05, 20, False, "red")

done()
