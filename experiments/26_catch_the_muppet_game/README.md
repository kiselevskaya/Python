Simple game to catch the muppet

    There is a game field with a moving muppet on it.
    The idea is to catch (mouse click) muppet while it changes its position.
    After 3 times the muppet was caught level increases alongside with speed also changes muppet.
    The Player won if passes all levels or loses if the number of missed shots equal to the number of levels multiplied by 3.


**game_logic.py**

    The new_game function starts the new game by resetting score, level, position of object, speed, muppet image.
    Counts score and level increase level and speed, and changes the muppet image on every 3 times target have been caught.
    Won if passed all levels, lost if missed 3*(number of levels) times.

**main.py**

    Determines position and image for a muppet.

**muppet_server.py**
    
    Starts server at port 8000.
    Responds to events (button push, missed shot, target catch) by running proper function and send updated information to the web browser.
