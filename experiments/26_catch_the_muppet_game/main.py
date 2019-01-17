# -*- coding: utf-8 -*-
# main.py


import math


# t = 0
# scale = (2 / (3 - math.cos(60*t)))*9
# lemniscate = [scale * math.cos(t/30)*30, scale * math.sin(2*t/30)*30 / 2]

step = 60
increment = 2*math.pi/step
theta = increment
decrease = False

width = 600
height = 600
img_size = 50
center = [width/2 - img_size/2, height/2 - img_size/2]

spiral = [[theta * math.cos(theta)], [theta * math.sin(theta)]]
muppets = ['cookie.png', 'elmo.png', 'big-bird.png', 'oscar.png', 'abby.png', 'count-von-count.png', 'bert.png', 'kermit.png', 'grover.png', 'ernie.png']


class Muppet(object):
    global theta, center, decrease, muppets

    def __init__(self, pos, image):
        self.pos = [pos[0], pos[1]]
        self.image = image

    def __str__(self):
        return '{}, {}, {}'.format(self.pos[0], self.pos[1], self.image)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def animate(self):
        xy = graph_direction(self.pos[0], self.pos[1], theta * math.cos(theta), theta * math.sin(theta))
        # vel = 5*(muppets.index(self.image)+1)
        vel = 30
        self.pos[0] = center[0] + xy[0]*vel
        self.pos[1] = center[1] + xy[1]*vel
        return self


def graph_direction(x, y, func_x, func_y):
    global theta, decrease, center, width, height

    half_img = 25

    if (x > center[0] + width/2 - half_img or y > center[1] + height/2 - half_img or
            x < center[0] - width/2 + half_img or y < center[1] - height/2 + half_img and not decrease):
        decrease = True
    elif x == center[0] and y == center[1]:
        decrease = False

    if decrease:
        theta -= increment
    else:
        theta += increment

    new_x = func_x
    new_y = func_y
    return [new_x, new_y]

