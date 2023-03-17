import pygame

from settings import settings

from game import Game

def main():
	game = Game(settings)

	state = 1
	while state > 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: state = 0
			if event.type == pygame.KEYDOWN:
				if event.key in settings['Obj']['Player']['Keys']:
					game.input(event.key)
				if event.key == pygame.K_ESCAPE: state = 0
			if event.type == pygame.USEREVENT:
				game.move()

		game.blit()

	return

def main2():
	# Load settings
	# if not os.path.exists(os.path.join(os.getcwd(), SETTINGSFILENAME)):
	# 	print('Unable to find settings file .\\\'' + SETTINGSFILENAME + '\'')
	# 	return -1
	# with open(SETTINGSFILENAME, 'r') as file:
	# 	settings = json.load(file)


	# Initialize pygame
	pygame.init()
	clock = pygame.time.Clock()
	canvas = pygame.display.set_mode(settings['Env']['Resolution'])
	pygame.display.set_caption(settings['Env']['Name'])

	# frameCounter = FPSCounter(canvas, clock, settings['Obj']['FPS'])
	player = Snake(canvas, settings)

	player.move(food = True)
	player.move(food = True)
	player.move(food = True)
	player.move(food = True)
	player.move(food = True)
	player.move(food = True)

	state = 1
	while state > 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				state = 0
			if event.type == pygame.KEYDOWN:
				if event.key in settings['Obj']['Player']['Keys']:
					player.input(event.key)
				if event.key == pygame.K_ESCAPE: state = 0
			if event.type == player.refresh:
				player.move()


		clock.tick(settings['Env']['FPS'])
		canvas.fill(settings['Env']['BackgroundColor'])

		player.draw()
		# frameCounter.draw()

		pygame.display.update()

	return

if __name__ == '__main__':
	main()