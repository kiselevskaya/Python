# template for "Stopwatch: The Game"
import simplegui
# define global variables

counter = 0
x = 0
y = 0
work = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tick):
    global A, B, C, D
    if counter <= 5999:
        A = (counter // 10) // 60
        B = ((counter // 10) - (A * 60)) // 10 # ((counter // 10) % 60) // 10
        C = ((counter // 10) - (A * 60)) % 10  # ((counter // 10) % 60) % 10
        D = counter % 10
    else:
        reset
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global work
    timer.start()
    work = True

def stop():
    global x, y, D, work
    timer.stop()
    if work and D == 0 and counter != 0:
        y += 1
        x += 1
    elif work and D != 0 and counter != 0:
        y += 1
    work = False

def reset():
    global counter
    timer.stop()
    counter = 0

def hit_score():
    global x, y
    score = str(x) + "/" + str(y)
    return score

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    return counter

# define draw handler
def draw(canvas):
    global text, hit
    text = format(tick)
    hit = hit_score()
    canvas.draw_text(text, [55, 170], 80, "White")
    canvas.draw_text(hit, [245, 35], 40, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
