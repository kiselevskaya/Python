# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global num, exposed, state, counter
    state = 0
    counter = 0
    numbers = range(8)
    numbers.extend(numbers)
    num = list(numbers)
    random.shuffle(num)
    exposed = []
    for n in num:
        exposed.append(False)
    #print exposed
    #print num

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first, second, counter
    if state == 0:
        first = pos[0] // 50
        if exposed[first] is False:
            exposed[first] = True
            state = 1
            counter += 1
            label.set_text("Turns = " + str(counter))
    elif state == 1:
        second = pos[0] // 50
        if exposed[second] is False:
            exposed[second] = True
            state = 2
    elif num[first] == num[second]:
        state = 0
        first = pos[0] // 50
        if exposed[first] is False:
            exposed[first] = True
            state = 1
            counter += 1
            label.set_text("Turns = " + str(counter))
    elif num[first] != num[second]:
        exposed[first] = False
        exposed[second] = False
        state = 0
        first = pos[0] // 50
        if exposed[first] is False:
            exposed[first] = True
            state = 1
            counter += 1
            label.set_text("Turns = " + str(counter))

# cards are logically 50x100 pixels in size
def draw(canvas):
    global num, exposed
    card_pos = 25
    for num_index in range(len(num)):
        num_pos = (50 * num_index) + 10
        canvas.draw_text(str(num[num_index]), [num_pos, 70], 60, "White")

    for el in exposed:
        if el is False:
            canvas.draw_line([card_pos, 10], [card_pos, 90], 45, "Green")
            card_pos += 50
        else:
            card_pos += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
