from turtle import *


def draw_branch(branch_length, angle):
    if branch_length > 5:
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle)
        left(2 * angle)
        draw_branch(branch_length - 15, angle)
        right(angle)
        pensize(2)
        backward(branch_length)




#
# draw_branch(100, 20)

def draw_tree(trunk_length, angle):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle)
    done()


draw_tree(100, 20)
