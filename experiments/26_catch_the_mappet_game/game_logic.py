

import math
import time
# import random
# from collections import OrderedDict

start_time = time.time()
scale = (2 / (3 - math.cos(60*start_time)))*9
step = 20
increment = 2*math.pi/step
theta = increment


class Graphics:
    def __init__(self, x, y):
        self.time = time
        self.scale = scale
        self.theta = theta
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


lemniscate = Graphics(scale * math.cos(time.time()/30)*30, scale * math.sin(2*time.time()/30)*30 / 2)
spiral = Graphics(theta * math.cos(theta), theta * math.sin(theta))


width = 600
height = 600
center = [width/2, height/2]
img_size = 70


class Muppet(object):
    def __init__(self, pos, image, vel=0.9, graph=spiral):
        self.pos = [pos[0], pos[1]]
        self.vel = vel
        self.image = image
        self.graph = graph

    def __str__(self):
        return '{}, {}, {}'.format(self.pos[0], self.pos[1], self.image)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def animate(self):
        self.pos[0] += self.vel*self.graph.x
        self.pos[1] += self.vel*self.graph.y
        return self.pos


muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"];
muppet = Muppet(center, muppets[-1])
# muppet = Muppet(center, random.choice(muppets))
