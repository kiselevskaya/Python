

# from game_logic import *
import math


t = 0
scale = (2 / (3 - math.cos(60*t)))*9
step = 60
increment = 2*math.pi/step
theta = increment
decrease = False

width = 600
height = 600
img_size = 50
center = [width/2 - img_size/2, height/2 - img_size/2]


lemniscate = [scale * math.cos(t/30)*30, scale * math.sin(2*t/30)*30 / 2]
spiral = [theta * math.cos(theta), theta * math.sin(theta)]


class Muppet(object):
    global theta, center, decrease

    def __init__(self, pos, image, vel, graph):
        self.pos = [pos[0], pos[1]]
        self.image = image
        self.vel = vel
        self.graph = graph

    def __str__(self):
        return '{}, {}, {}'.format(self.pos[0], self.pos[1], self.image)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def animate(self):
        xy = graph_direction(self.pos[0], self.pos[1], theta * math.cos(theta), theta * math.sin(theta))
        self.pos[0] += xy[0]
        self.pos[1] += xy[1]
        return self


def graph_direction(x, y, func_x, func_y):
    global theta, decrease, center, width, height

    if x > center[0] + width/2 - 100:
        decrease = True
        print('right side, decrease = {}'.format(decrease))
    elif y > center[1] + width/2 - 100:
        decrease = True
        print('bottom, decrease = {}'.format(decrease))
    elif x < center[0] - height/2 + 100:
        decrease = True
        print('left side, decrease = {}'.format(decrease))
    elif y < center[1] - height/2 + 100:
        decrease = True
        print('top, decrease = {}'.format(decrease))
    elif x == center[0] and y == center[1]:
        decrease = False
        print('decrease = {}'.format(decrease))

    if not decrease:
        theta += increment
    else:
        theta -= increment

    new_x = func_x
    new_y = func_y
    return [new_x, new_y]
