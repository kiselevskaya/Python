

import math


muppets = ['cookie.png', 'elmo.png', 'big-bird.png', 'oscar.png', 'abby.png', 'count-von-count.png', 'bert.png', 'kermit.png', 'grover.png', 'ernie.png']


def next_x(theta):
    return theta * math.cos(theta)


def next_y(theta):
    return theta * math.sin(theta)


class Muppet:
    def __init__(self, image, image_size=50, width=600, height=600, step=60):
        self.image = image
        self.image_size = image_size
        self.width = width
        self.height = height
        self.center = [self.width/2 - self.image_size/2, self.height/2 - self.image_size/2]
        self.pos = [self.center[0], self.center[1]]
        self.step = step
        self.increment = 2*math.pi/self.step
        self.theta = self.increment
        self.decrease = False
        self.vel = 10
        self.next_step = [next_x, next_y]

    def __str__(self):
        return '{}, {}, {}'.format(self.pos[0], self.pos[1], self.image)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def animate(self):
        xy = self.process_direction()
        # vel = 5*(muppets.index(self.image)+1)
        self.pos[0] = xy[0]
        self.pos[1] = xy[1]
        return self

    def process_direction(self):
        old_x = self.pos[0]
        old_y = self.pos[1]
        half_img = self.image_size/2

        move_x = self.next_step[0](self.theta)
        move_y = self.next_step[1](self.theta)

        move_x = self.center[0] + move_x*self.vel
        move_y = self.center[1] + move_y*self.vel

        if (not self.decrease and
            (move_x > self.width - half_img or
             move_y > self.height - half_img or
             move_x < half_img or
             move_y < half_img)):
            self.decrease = True
        elif (math.fabs(old_x - self.center[0]) < 0.01) and (math.fabs(old_y - self.center[1]) < 0.01):
            self.decrease = False

        if self.decrease:
            self.theta -= self.increment
        else:
            self.theta += self.increment

        move_x = self.next_step[0](self.theta)
        move_y = self.next_step[1](self.theta)

        move_x = self.center[0] + move_x*self.vel
        move_y = self.center[1] + move_y*self.vel
        return [move_x, move_y]

    def check_shoot(self, coordinates):
        xc = coordinates[0]
        yc = coordinates[1]
        half_img = self.image_size/2

        selfx = self.pos[0] + half_img
        selfy = self.pos[1] + half_img

        if math.pow(selfx - xc, 2) + math.pow(selfy - yc, 2) < math.pow(half_img, 2):
            return True
        return False
