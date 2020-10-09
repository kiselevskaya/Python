# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # Angle update
        self.angle += self.angle_vel
        # Possition update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        # Acceleration in direction of forward vector
        # forward = angle_to_vector(math.radians(self.angle))
        forward = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += forward[0] * .1
            self.vel[1] += forward[1] * .1
        # Friction update
        self.vel[0] *= .99
        self.vel[1] *= .99

    def angle_vel_increase(self):
        self.angle_vel += 0.05

    def angle_vel_decrease(self):
        self.angle_vel -= 0.05

    def set_acceleration(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()

    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0], self.pos[1]]
        missile_pos[0] += self.radius * forward[0]
        missile_pos[1] += self.radius * forward[1]
        missile_vel = [self.vel[0] + 6* forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # Angle update
        self.angle += self.angle_vel
        # Possition update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age >= self.lifespan:
            return True
        return False

    def collide(self, other_object):
        return dist(self.pos, other_object.pos) <= self.radius + other_object.radius


def group_collide(group, other_object):
    num_collision = 0
    for element in set(group):
        if element.collide(other_object):
            group.remove(element)
            num_collision += 1
            return True
    return num_collision
    return False

def group_group_collide(group_first, group_second):
    number_of_collisions = 0
    for item in set(group_first):
        if group_collide(group_second, item):
            group_first.discard(item)
            number_of_collisions += 1
            #return True
    return number_of_collisions
    #return False


def keydown(key):
    if simplegui.KEY_MAP['right'] == key:
        my_ship.angle_vel_increase()
    elif simplegui.KEY_MAP['left'] == key:
        my_ship.angle_vel_decrease()
    elif simplegui.KEY_MAP['up'] == key and started:
        my_ship.set_acceleration(True)
    elif simplegui.KEY_MAP['space'] == key and started:
        my_ship.shoot()

def keyup(key):
    if simplegui.KEY_MAP['right'] == key:
        my_ship.angle_vel_decrease()
    elif simplegui.KEY_MAP['left'] == key:
        my_ship.angle_vel_increase()
    elif simplegui.KEY_MAP['up'] == key and started:
        my_ship.set_acceleration(False)


# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, soundtrack
    lives = 3
    score = 0
    soundtrack.rewind()
    soundtrack.play()
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True


def process_sprite_group(group, canvas):
    for sprite in set(group):
        if not sprite.update():
            sprite.draw(canvas)
        else:
            group.remove(sprite)

def draw(canvas):
    global time, started, lives, score, soundtrack
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    canvas.draw_text('Lives ' + str(lives), [70, 60], 35, 'Maroon')
    canvas.draw_text('Score ' + str(score), [620, 60], 35, 'Maroon')

    # draw and update ship and sprites

    my_ship.draw(canvas)
    my_ship.update()

    if group_collide(rock_group, my_ship):
        lives -= 1
    if lives == 0:
        started = False

    if group_group_collide(missile_group, rock_group):
        score += 1

    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)

# draw splash screen if not started
    if not started:
        soundtrack.pause()
        my_ship.pos = [WIDTH / 2, HEIGHT / 2]
        my_ship.vel = [0, 0]
        my_ship.angle = 0
        rock_group.difference_update(set(rock_group))
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())

# timer handler that spawns a rock
def rock_spawner():
    global started
    rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    rock_vel = [random.random() * random.choice([-1, 1]), random.random() * random.choice([-1, 1])]
    rock_angvel = random.random() * random.choice([-1, 1]) / 20
    #    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    #    rock_avel = random.random() * .2 - .1
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_angvel, asteroid_image, asteroid_info)
    if started:
        if dist(a_rock.pos, my_ship.pos) > (a_rock.radius + my_ship.radius) * 1.1:
            if len(rock_group) < 12:
                rock_group.add(a_rock)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [0.3, 0.4], 0, 0.03, asteroid_image, asteroid_info)
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
