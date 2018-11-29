

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
muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"];
muppet = Muppet(center, muppets[-1], 2)


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


speed = 10
score = [0, 0]
multiple = 1
level = multiple
new_level = 3 * multiple
logs = ["Zero missed yet"]


def modify_score():
    global multiple, new_level, score, speed
    if muppet.pos[0] <= mouse_pos[0] <= muppet.pos[0]+50:
        if muppet.pos[1] <= mouse_pos[1] <= muppet.pos[1]+50:
            score[0] += 1
            if score[0] == new_level:
                multiple += 1
                speed += 10
                try:
                    muppet.image = muppets[muppets.index(muppet.image)+1]
                except IndexError:
                    muppet.image = muppets[0]
    else:
        score[1] += 1
        logs.append('{} time you miss on: {} sec.'.format(score[1], (time.time()-start_time)/1000))
