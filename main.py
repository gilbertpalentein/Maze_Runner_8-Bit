from game import runGame
import ui_file
import os


# function to set the position of the display window
def set_window_position (x, y):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)


# main function
if __name__ == "__main__":

    # set the window display position
    set_window_position(50, 50)

    # initialize states
    states = {0: "Main Menu", 1: "Gameplay"}
    current_state = states[0]

    # initialize variables with default value
    grid_size = 20
    side_length = 10
    bot_speed = 100
    b1_search, b1_chase = "A*", "Steady"
    b2_search, b2_chase = "BFS", "Stalking"

    # flag for main loop
    Run = True

    while Run:
        if current_state == states[0]:
            Run, grid_size, side_length, bot_speed, b1_search, b1_chase, b2_search, b2_chase = ui_file.startScreen(grid_size, side_length, bot_speed, b1_search, b1_chase, b2_search, b2_chase)
            current_state = states[1]
        elif current_state == states[1]:
            value = runGame(grid_size, side_length, bot_speed, b1_search, b1_chase, b2_search, b2_chase)
            if value != -1:
                ui_file.endGame(value)

            current_state = states[0]

    # just in case lol
    quit()

