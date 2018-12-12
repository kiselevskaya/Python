

from main import *
import time
# import math
# import random


start = False
game_over = False
start_time = time.time()

width = 600
height = 600
img_size = 50
center = [width/2 - img_size/2, height/2 - img_size/2]
muppets = ['elmo.png', 'big-bird.png', 'oscar.png', 'abby.png', 'count-von-count.png', 'bert.png', 'kermit.png', 'grover.png', 'ernie.png', 'cookie.png']
end_images = ['won.png', 'game_over.png']
muppet = Muppet(center, muppets[-1], 2)

speed = 10
score = [0, 0]
multiple = 1
logs = []
level = 1
constant = 1


def new_game():
    global start
    if not start:
        reset()
    return start


def reset():
    global start, game_over, start_time, muppet, speed, score, multiple, logs, level, t
    start = True
    game_over = False
    speed = 10
    score = [0, 0]
    multiple = 1
    logs = []
    level = 1
    muppet.image = muppets[-1]
    muppet.pos[0] = center[0]
    muppet.pos[1] = center[1]
    start_time = time.time()
    t = 0


def modify_score(event):
    global multiple, score, speed, start, game_over, level, logs, start_time
    if not game_over and start:
        if event:
            score[0] += 1
            if score[0] == constant*multiple and multiple < len(muppets):
                multiple += 1
                level += 1
                speed += 10
                try:
                    muppet.image = muppets[1+muppets.index(muppet.image)]
                except IndexError:
                    muppet.image = muppets[0]
            else:
                # muppet image changes to won image
                # muppet.image = end_images[0]
                start = False
                game_over = True
        else:
            score[1] += 1
            logs.append('{} time you miss on: {} sec.'.format(score[1], int(round((time.time()-start_time)))))
            if score[1] == len(muppets):
                # muppet image changes to lost image
                # muppet.image = end_images[1]
                start = False
                game_over = True
    return score


def simulation():
    global t
    print(start, game_over)
    if start and not game_over:
        muppet.animate()
        t += 1


def return_logs():
    global logs
    return logs


def return_level():
    global level
    return level
