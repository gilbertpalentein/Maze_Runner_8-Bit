import logic
import random
import pygame
from collections import deque
from graph import Graph
from character import Character


# creates a grid of size (size)*(size)
def create_grid (size):
    # create a graph for the grid
    grid = Graph()

    # add the vertices of the grid
    for i in range(size):
        for j in range(size):
            grid.add_vertex((i, j))

    # return the constructed grid
    return grid


# creates a maze when a grid ad its vertices are passed in
def create_maze (grid, vertex, completed=None, vertices=None):
    if vertices is None:
        vertices = grid.get_vertices()
    if completed is None:
        completed = [vertex]

    # select a random direction
    paths = list(int(i) for i in range(4))
    random.shuffle(paths)

    # vertices in the direction from current vertex
    up = (vertex[0], vertex[1] - 1)
    down = (vertex[0], vertex[1] + 1)
    left = (vertex[0] - 1, vertex[1])
    right = (vertex[0] + 1, vertex[1])

    for direction in paths:
        if direction == 0:
            if up in vertices and up not in completed:
                # add the edges
                grid.add_edge((vertex, up))
                grid.add_edge((up, vertex))
                completed.append(up)
                create_maze(grid, up, completed, vertices)
        elif direction == 1:
            if down in vertices and down not in completed:
                grid.add_edge((vertex, down))
                grid.add_edge((down, vertex))
                completed.append(down)
                create_maze(grid, down, completed, vertices)
        elif direction == 2:
            if left in vertices and left not in completed:
                grid.add_edge((vertex, left))
                grid.add_edge((left, vertex))
                completed.append(left)
                create_maze(grid, left, completed, vertices)
        elif direction == 3:
            if right in vertices and right not in completed:
                grid.add_edge((vertex, right))
                grid.add_edge((right, vertex))
                completed.append(right)
                create_maze(grid, right, completed, vertices)

    return grid


# draw maze function
# takes in a (size)x(size) maze and prints a "colour" path
# side_length is the length of the grid unit and border_width is its border thickness
def draw_maze (screen, maze, size, colour, side_length, border_width):
    # for every vertex in the maze:
    for i in range(size):
        for j in range(size):
            # if the vertex is not at the left-most side of the map
            if i != 0:
                # check if the grid unit to the current unit's left is connected by an edge
                if maze.is_edge(((i, j), (i - 1, j))):
                    # if connected, draw the grid unit without the left wall
                    pygame.draw.rect(screen, colour,
                                     [(side_length + border_width) * i, border_width + (side_length + border_width) * j, \
                                      side_length + border_width, side_length])
            # if the vertex is not at the right-most side of the map
            if i != size - 1:
                if maze.is_edge(((i, j), (i + 1, j))):
                    # draw the grid unit without the right wall (extend by border_width)
                    pygame.draw.rect(screen, colour, [border_width + (side_length + border_width) * i, \
                                                      border_width + (side_length + border_width) * j,
                                                      side_length + border_width, side_length])
            # if the vertex is not at the top-most side of the map
            if j != 0:
                if maze.is_edge(((i, j), (i, j - 1))):
                    pygame.draw.rect(screen, colour, [border_width + (side_length + border_width) * i, \
                                                      (side_length + border_width) * j, side_length,
                                                      side_length + border_width])
            # if the vertex is not at the bottom-most side of the map
            if j != size - 1:
                if maze.is_edge(((i, j), (i, j + 1))):
                    pygame.draw.rect(screen, colour, [border_width + (side_length + border_width) * i, \
                                                      border_width + (side_length + border_width) * j, side_length,
                                                      side_length + border_width])


# draw position of grid unit
def draw_position (screen, side_length, border_width, current_point, colour):
    pygame.draw.rect(screen, colour, [border_width + (side_length + border_width) * current_point[0], \
                                      border_width + (side_length + border_width) * current_point[1], side_length,
                                      side_length])


# takes in a player2 character, maze, vertices, cooldown, and timer
def playerTwo (player2, maze, vertices, cooldown, timer):
    # get the pressed keys
    keys = pygame.key.get_pressed()

    if (pygame.time.get_ticks() - timer > cooldown):
        current_point = player2.get_current_position()
        # move character right
        if keys[pygame.K_d]:
            # check if the next point is in the maze
            if (current_point[0] + 1, current_point[1]) in vertices:
                next_point = (current_point[0] + 1, current_point[1])
                # check if the next point is connected by an edge
                if (maze.is_edge((current_point, next_point))):
                    player2.move_character_smooth(next_point, 5)
            # restart cooldown timer
            timer = pygame.time.get_ticks()
        # move character left
        if keys[pygame.K_a]:
            if (current_point[0] - 1, current_point[1]) in vertices:
                next_point = (current_point[0] - 1, current_point[1])
                if (maze.is_edge((current_point, next_point))):
                    player2.move_character_smooth(next_point, 5)
            # restart cooldown timer
            timer = pygame.time.get_ticks()
        # move character up
        if keys[pygame.K_w]:
            if (current_point[0], current_point[1] - 1) in vertices:
                next_point = (current_point[0], current_point[1] - 1)
                if (maze.is_edge((current_point, next_point))):
                    player2.move_character_smooth(next_point, 5)
            # restart cooldown timer
            timer = pygame.time.get_ticks()
        # move character down
        if keys[pygame.K_s]:
            if (current_point[0], current_point[1] + 1) in vertices:
                next_point = (current_point[0], current_point[1] + 1)
                if (maze.is_edge((current_point, next_point))):
                    player2.move_character_smooth(next_point, 5)
            # restart cooldown timer
            timer = pygame.time.get_ticks()

    return timer


# update console function
def update_console (screen, screen_size, side_length, text_size, a_colour, na_colour, keys_left, wallBreaks):
    if keys_left == 0:
        text = "Escape! " + " WB: " + str(wallBreaks)
    else:
        text = "K: " + str(keys_left) + " WB: " + str(wallBreaks)
    # console rect
    console_rect = (0, screen_size[1] - side_length * 3, screen_size[0], side_length * 3)
    # clear console
    pygame.draw.rect(screen, na_colour, console_rect)
    # display the text
    displayText = pygame.font.SysFont("ubuntu", text_size)
    textSurface = displayText.render(text, True, a_colour)
    textRect = textSurface.get_rect()
    # center text
    textRect.center = (screen_size[0] / 2, screen_size[1] - text_size * 2)
    # display text on screen ("blit")
    screen.blit(textSurface, textRect)
    # update the screen
    pygame.display.update(console_rect)


# run the maze game
# takes in grid size and side length for the maze
def runGame (grid_size, side_length):
    # initialize the game engine
    pygame.init()

    # Defining colours (RGB) ...
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    DARKGRAY = (50, 50, 50)
    WHITE = (255, 255, 255)
    GOLD = (249, 166, 2)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # set the grid size and side length of each grid
    # grid_size = 20 # this is the maximum size before reaching recursion limit on maze buidling function
    # side_length = 10

    # scale the border width with respect to the given side length
    border_width = side_length // 5

    # initialize the grid for the maze
    grid = create_grid(grid_size)
    # create the maze using the grid
    maze = create_maze(grid, (grid_size // 2, grid_size // 2))  # use the starting vertex to be middle of the map

    # Opening a window ...
    # set the screen size to match the grid
    size = (grid_size * (side_length + border_width) + border_width, \
            grid_size * (side_length + border_width) + border_width + side_length * 3)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("\"Esc\" to exit")

    # set the continue flag
    carryOn = True

    # set the clock (how fast the screen updates)
    clock = pygame.time.Clock()

    # have a black background
    screen.fill(BLACK)

    # get all of the vertices in the maze
    vertices = maze.get_vertices()

    # draw the maze
    draw_maze(screen, maze, grid_size, WHITE, side_length, border_width)

    # initialize starting point of character and potential character 2
    start_point = (0, 0)

    # set end-point for the maze
    end_point = (grid_size - 1, grid_size - 1)

    # randomize a start and end point
    choice = random.randrange(4)

    if choice == 0:
        start_point = (grid_size - 1, grid_size - 1)
        end_point = (0, 0)
    elif choice == 1:
        start_point = (0, grid_size - 1)
        end_point = (grid_size - 1, 0)
    elif choice == 2:
        start_point = (grid_size - 1, 0)
        end_point = (0, grid_size - 1)

    # initialize winner variable
    winner = 0

    # set random key points (from 1 to grid_size-2)
    # 8 keys in total
    n_keys = 8 + int(grid_size/10 - 1)
    x_coords = random.sample(range(1, grid_size - 1), n_keys)
    y_coords = random.sample(range(1, grid_size - 1), n_keys)
    # initialize empty key list
    unlock_keys = []
    # append coordinates to the key list
    for i in range(n_keys):
        unlock_keys.append((x_coords[i], y_coords[i]))
    # if grid_size is 30 or more, add another computer
    is2Computer = False
    if grid_size >= 30:
        is2Computer = True
    # re-initialize character
    player1 = Character(screen, side_length, border_width, vertices, start_point, \
                        end_point, start_point, GREEN, WHITE, True, unlock_keys, GOLD)
    # initialize computer character
    computer_character = Character(screen, side_length, border_width, vertices, \
                                   start_point, end_point, start_point, GRAY, WHITE)
    # initialize computer2 character
    if is2Computer:
        computer2_character = Character(screen, side_length, border_width, vertices, \
                                       start_point, end_point, start_point, DARKGRAY, WHITE)
    # create a deque for the paths to the player
    dq = deque()
    # put start_point for the deque
    dq.append(start_point)
    # set the cooldown for how fast the computer moves
    computer_cooldown = grid_size * 100
    # set the maximum cooldown for the computer
    if computer_cooldown > 3000:
        computer_cooldown = 3000
    # set the initial wait time for the computer
    initial_wait = 3000
    if is2Computer:
        dq2 = deque()
        dq2.append(start_point)
        computer2_cooldown = computer_cooldown
        isCom2Far = False
    # initialize timers
    computer_timer = pygame.time.get_ticks()
    initial_wait_timer = pygame.time.get_ticks()
    # for computer2
    if is2Computer:
        computer2_timer = pygame.time.get_ticks()
        initial_wait_timer2 = pygame.time.get_ticks()

    # draw the end-point
    draw_position(screen, side_length, border_width, end_point, RED)
    # draw keys
    player1.draw_keys()
    # update console
    update_console(screen, size, side_length, size[0] // grid_size, WHITE, BLACK, player1.get_keys_left(),
                   player1.get_wallBreaks())

    # update the screen
    pygame.display.flip()

    # set cooldown for key presses
    cooldown = 100

    # initialize the cooldown timer
    start_timer = pygame.time.get_ticks()

    # main loop
    while carryOn:
        # action (close screen)
        for event in pygame.event.get():  # user did something
            if event.type == pygame.QUIT:
                carryOn = False
                winner = -1
            elif event.type == pygame.KEYDOWN:
                # Pressing the Esc Key will quit the game
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
                    winner = -1

        # get the pressed keys
        keys = pygame.key.get_pressed()

        if (pygame.time.get_ticks() - start_timer > cooldown):
            # get the current point of character
            current_point = player1.get_current_position()
            # move character right
            if keys[pygame.K_RIGHT]:
                # check if the next point is in the maze
                if (current_point[0] + 1, current_point[1]) in vertices:
                    next_point = (current_point[0] + 1, current_point[1])
                    # check if the next point is connected by an edge
                    if (maze.is_edge((current_point, next_point))):
                        player1.move_character_smooth(next_point, 5)
                        # update the shortest path for the computer to use
                        dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                        if is2Computer:
                            dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                    else:
                        # if the player pressed the space key, break the wall in the direction they are moving in
                        if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
                            maze = logic.break_wall(maze, current_point, next_point)
                            # move the player to that point
                            player1.move_character_smooth(next_point, 5)
                            # decrement the player's number of wallBreaks
                            player1.use_wallBreak()
                            # update the shortest path for the computer to use
                            dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                            if is2Computer:
                                dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                # restart cooldown timer
                start_timer = pygame.time.get_ticks()
            # move character left
            elif keys[pygame.K_LEFT]:
                if (current_point[0] - 1, current_point[1]) in vertices:
                    next_point = (current_point[0] - 1, current_point[1])
                    if (maze.is_edge((current_point, next_point))):
                        player1.move_character_smooth(next_point, 5)
                        # update the shortest path for the computer to use
                        dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                        if is2Computer:
                            dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                    else:
                        # if the player pressed the space key, break the wall in the direction they are moving in
                        if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
                            maze = logic.break_wall(maze, current_point, next_point)
                            # move the player to that point
                            player1.move_character_smooth(next_point, 5)
                            # decrement the player's number of wallBreaks
                            player1.use_wallBreak()
                            # update the shortest path for the computer to use
                            dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                            if is2Computer:
                                dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                # restart cooldown timer
                start_timer = pygame.time.get_ticks()
            # move character up
            elif keys[pygame.K_UP]:
                if (current_point[0], current_point[1] - 1) in vertices:
                    next_point = (current_point[0], current_point[1] - 1)
                    if (maze.is_edge((current_point, next_point))):
                        player1.move_character_smooth(next_point, 5)
                        # update the shortest path for the computer to use
                        dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                        if is2Computer:
                            dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                    else:
                        # if the player pressed the space key, break the wall in the direction they are moving in
                        if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
                            maze = logic.break_wall(maze, current_point, next_point)
                            # move the player to that point
                            player1.move_character_smooth(next_point, 5)
                            # decrement the player's number of wallBreaks
                            player1.use_wallBreak()
                            # update the shortest path for the computer to use
                            dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                            if is2Computer:
                                dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                # restart cooldown timer
                start_timer = pygame.time.get_ticks()
            # move character down
            elif keys[pygame.K_DOWN]:
                if (current_point[0], current_point[1] + 1) in vertices:
                    next_point = (current_point[0], current_point[1] + 1)
                    if (maze.is_edge((current_point, next_point))):
                        player1.move_character_smooth(next_point, 5)
                        # update the shortest path for the computer to use
                        dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                        if is2Computer:
                            dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                    else:
                        if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
                            maze = logic.break_wall(maze, current_point, next_point)
                            # move the player to that point
                            player1.move_character_smooth(next_point, 5)
                            # decrement the player's number of wallBreaks
                            player1.use_wallBreak()
                            # update the shortest path for the computer to use
                            dq = logic.update_path_a(computer_character.get_current_position(), next_point, maze, dq)
                            if is2Computer:
                                dq2 = logic.update_path_bfs(computer2_character.get_current_position(), next_point, maze, dq2)
                # restart cooldown timer
                start_timer = pygame.time.get_ticks()

        # redraw the keys
        player1.draw_keys()
        # check if all keys are collected
        if player1.collected_all():
            draw_position(screen, side_length, border_width, end_point, GREEN)
        else:
            draw_position(screen, side_length, border_width, end_point, RED)
        # increase the computer speed if got another 2 keys
        if player1.increase_computer_speed():
            computer_cooldown = computer_cooldown / 2
        # computer2 movement increase
        if is2Computer:
            if len(dq2) > 8 and not isCom2Far:
                computer2_cooldown = computer2_cooldown/10
                isCom2Far = True
            elif isCom2Far:
                computer2_cooldown = computer2_cooldown*10
                isCom2Far = False
            if player1.increase_computer_speed():
                computer2_cooldown = computer2_cooldown*0.8
        # update console
        update_console(screen, size, side_length, size[0] // grid_size, WHITE, BLACK, player1.get_keys_left(),
                       player1.get_wallBreaks())

        # update the wait condition
        waitCondition = pygame.time.get_ticks() - initial_wait_timer > initial_wait
        if is2Computer:
            waitCondition2 = pygame.time.get_ticks() - initial_wait_timer2 > initial_wait
        # check if the wait condition is met
        if (waitCondition):
            if (pygame.time.get_ticks() - computer_timer > computer_cooldown):
                # make sure that the deque is not empty
                if dq:
                    computer_character.move_character_smooth(dq.popleft(), 5)
                # reset the cooldown timer for computer
                computer_timer = pygame.time.get_ticks()
        # for computer2
        if is2Computer:
            if (waitCondition2):
                if (pygame.time.get_ticks() - computer2_timer > computer2_cooldown):
                    # make sure that the deque is not empty
                    if dq2:
                        computer2_character.move_character_smooth(dq2.popleft(), 10)
                    # reset the cooldown timer for computer
                    computer2_timer = pygame.time.get_ticks()

        # redraw the characters
        computer_character.draw_position()
        if is2Computer:
            computer2_character.draw_position()
        player1.draw_position()
        # update screen
        pygame.display.update()

        # win conditions
        if player1.escaped():
            winner = 1
            carryOn = False
        elif computer_character.get_current_position() == player1.get_current_position() and waitCondition \
                or is2Computer and computer2_character.get_current_position() == player1.get_current_position() and waitCondition2:
            winner = 2
            carryOn = False

        # limit to 60 frames per second (fps)
        clock.tick(60)

    # stop the game engine once exited the game
    pygame.quit()

    return winner

