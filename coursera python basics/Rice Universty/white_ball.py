# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle((200, 200), ball_radius, 1, "White", "White")

# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius = ball_radius + RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius = ball_radius - RADIUS_INCREMENT
    else:
        print "It's the most little ball now!"
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()
