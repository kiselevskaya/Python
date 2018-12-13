

# from game_logic import *
import math


t = 0
scale = (2 / (3 - math.cos(60*t)))*9
step = 20
increment = 2*math.pi/step
theta = increment
decrease = False


class Graphics:
    global t, scale, theta, step

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


lemniscate = Graphics(scale * math.cos(t/30)*30, scale * math.sin(2*t/30)*30 / 2)
spiral = Graphics(theta * math.cos(theta), theta * math.sin(theta))


class Muppet(object):
    def __init__(self, pos, image, vel, graph=spiral):
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
        self.pos[0] += self.graph.x
        self.pos[1] += self.graph.y
        return self
