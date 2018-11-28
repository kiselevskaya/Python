

import math
import time
# import random

start_time = time.time()
t = 0
scale = (2 / (3 - math.cos(60*t)))*9
step = 4
increment = 2*math.pi/step
theta = increment

started = False


def reset():
    global started, started_time, t
    started = True
    muppet.pos[0] = center[0]
    muppet.pos[1] = center[1]
    started_time = time.time()
    t = 0


def start():
    global started
    if not started:
        reset()
    if started:
        timeout()


def timeout():
    global t
    while started:
        muppet.animate()
        t += 1
        print(muppet)
        return muppet


class Graphics:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


lemniscate = Graphics(scale * math.cos(t/30)*30, scale * math.sin(2*t/30)*30 / 2)
spiral = Graphics(theta * math.cos(theta), theta * math.sin(theta))


width = 600
height = 600
img_size = 50
center = [width/2 - img_size/2, height/2 - img_size/2]


class Muppet(object):
    def __init__(self, pos, image, t, graph=spiral):
        self.pos = [pos[0], pos[1]]
        self.image = image
        self.t = t
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
        self.t += 1
        return self.pos


muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"];
muppet = Muppet(center, muppets[-1], t)
# muppet = Muppet(center, random.choice(muppets))


# def main():
#     start()
#
#
# if __name__ == '__main__':
#     main()
