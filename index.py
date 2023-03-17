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

if __name__ == '__main__':
	main()