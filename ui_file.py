'''
User interface file
'''

import pygame
import time


# displays a horizontally-centred message to the screen
def displayMessage(text, colour, screen, size, screen_size, y_pos, screen_update=None):
	# set the font and size of the message
	# use print(pygame.font.get_fonts()) to see available fonts on system
	displayText = pygame.font.SysFont("ubuntu", size)
	# set the text surface
	textSurface = displayText.render(text, True, colour)
	# get the size of the rectangle surrounding the message
	textRect = textSurface.get_rect()
	# center the container
	textRect.center = ((screen_size[0]/2),y_pos)
	# print it to the screen
	screen.blit(textSurface,textRect)
	# if no secified update screen size
	if screen_update is None:
		screen_update = textRect
	# update the screen with the message
	pygame.display.update(screen_update)
	# print(textRect)
	# return textRect


# displays the user selection of the Main Menu
# bg_colour: background colour, a_colout: active colour, na_colour: inactive colour
def displayMenuSelection(screen, screen_size, choice, bg_colour, a_colour, na_colour):
	screen.fill(bg_colour)
	if choice == 0:
		displayMessage("Maze Runner 8-Bit", na_colour, screen, 50, screen_size, screen_size[1]//5)
		displayMessage("Start Game", a_colour, screen, 30, screen_size, screen_size[1]*2//5)
		displayMessage("Settings", na_colour, screen, 30, screen_size, screen_size[1]*3//5)
		displayMessage("Exit", na_colour, screen, 30, screen_size, screen_size[1]*4//5)
	elif choice == 1:
		displayMessage("Maze Runner 8-Bit", na_colour, screen, 50, screen_size, screen_size[1]//5)
		displayMessage("Start Game", na_colour, screen, 30, screen_size, screen_size[1]*2//5)
		displayMessage("Settings", a_colour, screen, 30, screen_size, screen_size[1]*3//5)
		displayMessage("Exit", na_colour, screen, 30, screen_size, screen_size[1]*4//5)
	elif choice == 2:
		displayMessage("Maze Runner 8-Bit", na_colour, screen, 50, screen_size, screen_size[1]//5)
		displayMessage("Start Game", na_colour, screen, 30, screen_size, screen_size[1]*2//5)
		displayMessage("Settings", na_colour, screen, 30, screen_size, screen_size[1]*3//5)
		displayMessage("Exit", a_colour, screen, 30, screen_size, screen_size[1]*4//5)


# display settings options
# takes in additional grid size and side length parameters
def displaySettingsSelection(screen, screen_size, choice, bg_colour, a_colour, na_colour, grid_size, side_length, bot_speed, bot1_search, bot1_chase, bot2_search, bot2_chase):
	YELLOW = (200, 200, 0)
	PURPLE = (100, 0, 100)
	RED = (183, 0, 0)

	screen.fill(bg_colour)
	grid_text = "Grid size: " + str(grid_size)
	side_text = "Side length: " + str(side_length)
	speed_text = "Bot Speed: " + str(bot_speed)
	search1_text = "Search: " + bot1_search
	chase1_text = "Chase: " + bot1_chase
	search2_text = "Search: " + bot2_search
	chase2_text = "Chase: " + bot2_chase
	speed_text_rect = (145, 235, 210, 34)
	search_text_rect = (145, 300, 210, 34)
	chase_text_rect = (145, 325, 210, 34)
	search2_text_rect = (145, 365, 210, 34)
	chase2_text_rect = (145, 391, 210, 34)
	if choice == 0:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, a_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)
	elif choice == 1:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, a_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)
	elif choice == 2:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, a_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)
	elif choice == 3:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, a_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)
	elif choice == 4:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, a_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)

	elif choice == 5:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, a_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)

	elif choice == 6:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, a_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", na_colour, screen, 30, screen_size, screen_size[1]*29//32)

	elif choice == 7:
		displayMessage("Settings", na_colour, screen, 60, screen_size, screen_size[1]//8)
		displayMessage(grid_text, na_colour, screen, 30, screen_size, screen_size[1]*4//16)
		displayMessage("*bot 2 available if the grid size is at least 30", RED, screen, 12, screen_size, screen_size[1]*19//64)
		displayMessage(side_text, na_colour, screen, 30, screen_size, screen_size[1]*3//8)
		displayMessage(speed_text, na_colour, screen, 30, screen_size, screen_size[1]*4//8, speed_text_rect)
		displayMessage("Bot 1 Mechanism", YELLOW, screen, 20, screen_size, screen_size[1]*10//16)
		displayMessage(search1_text, na_colour, screen, 18, screen_size, screen_size[1]*21//32, search_text_rect)
		displayMessage(chase1_text, na_colour, screen, 18, screen_size, screen_size[1]*22//32, chase_text_rect)
		displayMessage("Bot 2 Mechanism", PURPLE, screen, 20, screen_size, screen_size[1]*12//16)
		displayMessage(search2_text, na_colour, screen, 18, screen_size, screen_size[1]*25//32, search2_text_rect)
		displayMessage(chase2_text, na_colour, screen, 18, screen_size, screen_size[1]*26//32, chase2_text_rect)
		displayMessage("Return", a_colour, screen, 30, screen_size, screen_size[1]*29//32)


# settings function - enables user to choose size of the map
def settingsMenu(screen, screen_size, bg_colour, a_colour, na_colour, cooldown, start_timer, g_size, s_length, b_speed, b1_search, b1_chase, b2_search, b2_chase):
	options = {0:"Grid Size", 1:"Side Length", 2:"Bot Speed", 3:"Bot Search",
			   4:"Bot Chase", 5:"Bot 2 Search", 6:"Bot 2 Chase", 7:"Return"}
	searchs = {0:"A*", 1:"BFS"}
	chases = {0:"Steady", 1:"Stalking"}
	current_selection = options[0]

	grid_size = g_size
	side_length = s_length
	bot_speed = b_speed
	bot_search = b1_search
	bot_chase = b1_chase
	bot2_search = b2_search
	bot2_chase = b2_chase

	pygame.display.set_caption("Settings")

	screen.fill(bg_colour)

	pygame.display.flip()

	displaySettingsSelection(screen, screen_size, 0, bg_colour, a_colour, na_colour,
							 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)

	carryOn = True

	while carryOn:
		# action (close screen)
		for event in pygame.event.get():  # user did something
			if event.type == pygame.QUIT:
				carryOn = False
				Run = False

		# get pressed keys
		keys = pygame.key.get_pressed()

		# if the cooldown timer is reached
		if pygame.time.get_ticks() - start_timer > cooldown:
			if current_selection == options[0]:
				# if user pressed down arrow key
				if keys[pygame.K_DOWN]:
					# display selection
					displaySettingsSelection(screen, screen_size, 1, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[1]
					# restart cooldown timer
					start_timer = pygame.time.get_ticks()
				# decrease the grid size by 1
				if keys[pygame.K_LEFT]:
					grid_size -= 1
					if grid_size < 10:
						grid_size = 10
					displaySettingsSelection(screen, screen_size, 0, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# increase the grid size by 1
				if keys[pygame.K_RIGHT]:
					grid_size += 1
					if grid_size > 35:
						grid_size = 35
					displaySettingsSelection(screen, screen_size, 0, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[1]:
				# if user pressed down arrow key
				if keys[pygame.K_DOWN]:
					# display selection
					displaySettingsSelection(screen, screen_size, 2, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[2]
					# restart cooldown timer
					start_timer = pygame.time.get_ticks()
				# if user pressed up arrow key
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 0, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[0]
					start_timer = pygame.time.get_ticks()
				# decrease the grid size by 1
				if keys[pygame.K_LEFT]:
					side_length -= 1
					if side_length < 10:
						side_length = 10
					displaySettingsSelection(screen, screen_size, 1, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# increase the grid size by 1
				if keys[pygame.K_RIGHT]:
					side_length += 1
					if side_length > 15:
						side_length = 15
					displaySettingsSelection(screen, screen_size, 1, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[2]:
				if keys[pygame.K_DOWN]:
					displaySettingsSelection(screen, screen_size, 3, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[3]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 1, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[1]
					start_timer = pygame.time.get_ticks()
				# decrease the bot speed by 10
				if keys[pygame.K_LEFT]:
					bot_speed -= 10
					if bot_speed < 50:
						bot_speed = 50
					displaySettingsSelection(screen, screen_size, 2, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# increase the bot speed by 10
				if keys[pygame.K_RIGHT]:
					bot_speed += 10
					if bot_speed > 190:
						bot_speed = 190
					displaySettingsSelection(screen, screen_size, 2, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[3]:
				if keys[pygame.K_DOWN]:
					displaySettingsSelection(screen, screen_size, 4, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[4]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 2, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[2]
					start_timer = pygame.time.get_ticks()
				# change bot 1 search algorithm to A*
				if keys[pygame.K_LEFT]:
					bot_search = searchs[0]
					displaySettingsSelection(screen, screen_size, 3, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# change bot 1 search algorithm to BFS
				if keys[pygame.K_RIGHT]:
					bot_search = searchs[1]
					displaySettingsSelection(screen, screen_size, 3, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[4]:
				if keys[pygame.K_DOWN]:
					displaySettingsSelection(screen, screen_size, 5, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[5]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 3, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[3]
					start_timer = pygame.time.get_ticks()
				# change bot 1 chase mechanism to Steady
				if keys[pygame.K_LEFT]:
					bot_chase = chases[0]
					displaySettingsSelection(screen, screen_size, 4, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# change bot 1 chase mechanism to Stalking
				if keys[pygame.K_RIGHT]:
					bot_chase = chases[1]
					displaySettingsSelection(screen, screen_size, 4, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[5]:
				if keys[pygame.K_DOWN]:
					displaySettingsSelection(screen, screen_size, 6, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[6]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 4, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[4]
					start_timer = pygame.time.get_ticks()
				# change bot 2 search algorithm to A*
				if keys[pygame.K_LEFT]:
					bot2_search = searchs[0]
					displaySettingsSelection(screen, screen_size, 5, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# change bot 2 search algorithm to BFS
				if keys[pygame.K_RIGHT]:
					bot2_search = searchs[1]
					displaySettingsSelection(screen, screen_size, 5, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[6]:
				if keys[pygame.K_DOWN]:
					displaySettingsSelection(screen, screen_size, 7, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[7]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_UP]:
					displaySettingsSelection(screen, screen_size, 5, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[5]
					start_timer = pygame.time.get_ticks()
				# change bot 2 chase mechanism to Steady
				if keys[pygame.K_LEFT]:
					bot2_chase = chases[0]
					displaySettingsSelection(screen, screen_size, 6, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
				# change bot 2 chase mechanism to Stalking
				if keys[pygame.K_RIGHT]:
					bot2_chase = chases[1]
					displaySettingsSelection(screen, screen_size, 6, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					start_timer = pygame.time.get_ticks()
			elif current_selection == options[7]:
				# if user pressed up arrow key
				if keys[pygame.K_UP]:
					# display selection 1
					displaySettingsSelection(screen, screen_size, 6, bg_colour, a_colour, na_colour,
											 grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase)
					current_selection = options[6]
					start_timer = pygame.time.get_ticks()
				# press enter key to select this option
				if keys[pygame.K_RETURN]:
					carryOn = False

	# reset the caption
	pygame.display.set_caption("Main Menu")

	# return selected grid size and side length
	return grid_size, side_length, bot_speed, bot_search, bot_chase, bot2_search, bot2_chase


# start screen function
def startScreen(grid_size, side_length, bot_speed, bot1_search, bot1_chase, bot2_search, bot2_chase):
	pygame.init()

	# Define colours
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	GOLD = (249,166,2)

	screen_size = (500,500)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Main Menu")
	screen.fill(WHITE)

	pygame.display.flip()

	displayMenuSelection(screen, screen_size, 0, WHITE, GOLD, BLACK)

	options = {0:"Start Game", 1:"Settings", 2:"Exit"}
	current_selection = options[0]

	clock = pygame.time.Clock()

	Run = True

	carryOn = True
	Settings = False

	# set cooldown for key clicks
	cooldown = 150
	# initialize cooldown timer for key clicks
	start_timer = pygame.time.get_ticks()

	while carryOn:
		# action (close screen)
		for event in pygame.event.get():  # user did something
			if event.type == pygame.QUIT:
				carryOn = False
				Run = False

		# get pressed keys
		keys = pygame.key.get_pressed()

		# if the cooldown timer is reached
		if pygame.time.get_ticks() - start_timer > cooldown:
			if current_selection == options[0]:
				# if user pressed down arrow key
				if keys[pygame.K_DOWN]:
					# display selection 1
					displayMenuSelection(screen, screen_size, 1, WHITE, GOLD, BLACK)
					current_selection = options[1]
					# restart cooldown timer
					start_timer = pygame.time.get_ticks()
				# if user selected this option, break out of loop
				if keys[pygame.K_RETURN]:
					carryOn = False
			elif current_selection == options[1]:
				# if user pressed up arrow key
				if keys[pygame.K_UP]:
					# display selection 0
					displayMenuSelection(screen, screen_size, 0, WHITE, GOLD, BLACK)
					current_selection = options[0]
					start_timer = pygame.time.get_ticks()
				# if user pressed down arrow key
				if keys[pygame.K_DOWN]:
					# display selection 2
					displayMenuSelection(screen, screen_size, 2, WHITE, GOLD, BLACK)
					current_selection = options[2]
					start_timer = pygame.time.get_ticks()
				if keys[pygame.K_RETURN]:
					Settings = True
			elif current_selection == options[2]:
				# if user pressed up arrow key
				if keys[pygame.K_UP]:
					# display selection 1
					displayMenuSelection(screen, screen_size, 1, WHITE, GOLD, BLACK)
					current_selection = options[1]
					start_timer = pygame.time.get_ticks()
				# enter key to select this option
				if keys[pygame.K_RETURN]:
					carryOn = False
					Run = False

		# if the settings option was selected
		if Settings:
			grid_size, side_length, bot_speed, bot1_search, bot1_chase, bot2_search, bot2_chase = settingsMenu(screen, screen_size, WHITE, GOLD, BLACK, cooldown,
																								start_timer, grid_size, side_length, bot_speed, bot1_search, bot1_chase, bot2_search, bot2_chase)
			current_selection = options[0]
			displayMenuSelection(screen, screen_size, 0, WHITE, GOLD, BLACK)
			# refresh the screen
			pygame.display.flip()
			# wait quarter of a second
			time.sleep(0.25)
			start_timer = pygame.time.get_ticks()
			Settings = False

		clock.tick(60)

	pygame.quit()

	return Run, grid_size, side_length, bot_speed, bot1_search, bot1_chase, bot2_search, bot2_chase

# end game screen
def endGame(value):
	pygame.init()

	# Define colours
	BLACK = (0,0,0)
	GRAY = (100,100,100)
	WHITE = (255,255,255)
	GOLD = (249,166,2)

	screen_size = (500,500)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Game Over")
	screen.fill(WHITE)

	pygame.display.flip()
	displayMessage("Game Over", BLACK, screen, 50, screen_size, screen_size[1]//4)
	if value == 1:
		text = "You escaped!"
		displayMessage(text, GOLD, screen, 30, screen_size, screen_size[1]*2//4)
	else:
		text = "You were caught!"
		displayMessage(text, GRAY, screen, 30, screen_size, screen_size[1]*2//4)
	displayMessage("Press enter to exit to menu.", BLACK, screen, 20, screen_size,screen_size[1]*3//4)


	carryOn = True

	clock = pygame.time.Clock()

	while carryOn:

		# action (close screen)
		for event in pygame.event.get():# user did something
			if event.type == pygame.QUIT:
				carryOn = False

		# get keys pressed
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN]:
			carryOn = False

		clock.tick(60)

	pygame.quit()
