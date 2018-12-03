

from main import *
import time
# import math
# import random
mouse_pos = None


started = False
start_time = time.time()

width = 600
height = 600
img_size = 50
center = [width/2 - img_size/2, height/2 - img_size/2]
muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"]
muppet = Muppet(center, muppets[-1], 2)


def reset():
    global started, started_time, t, muppet
    started = True
    muppet.image = muppets[-1]
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


speed = 10
score = [0, 0]
multiple = 1
logs = []
level = [1]


def modify_score(event):
    global multiple, score, speed
    if event:
        score[0] += 1
        if score[0] == 3*multiple:
            multiple += 1
            level.pop()
            level.append(multiple)
            speed += 10
            try:
                muppet.image = muppets[1+muppets.index(muppet.image)]
            except IndexError:
                muppet.image = muppets[0]
    else:
        score[1] += 1
        logs.append('{} time you miss on: {} sec.'.format(score[1], int(round((time.time()-start_time)))))
    return multiple
