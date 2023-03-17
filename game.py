import pygame

from fps import FPSCounter
from snake import Snake

class Game:
	def __init__(self, settings):
		self.settings = settings

		pygame.init()
		self.clock = pygame.time.Clock()
		self.canvas = pygame.display.set_mode(self.settings['Env']['Resolution'])

		self.frameCounter = FPSCounter(self.canvas, self.clock, self.settings['Obj']['FPS'])
		self.player = Snake(self.canvas, self.settings)

		pygame.display.set_caption(self.settings['Env']['Name'])

		self.player.move(food = True)
		self.player.move(food = True)
		self.player.move(food = True)
		self.player.move(food = True)
		self.player.move(food = True)
		self.player.move(food = True)

		return

	def blit(self):
		self.clock.tick(self.settings['Env']['FPS'])
		self.canvas.fill(self.settings['Env']['BackgroundColor'])

		self.frameCounter.draw()
		self.player.draw()

		pygame.display.update()

	def input(self, key): return self.player.input(key)

	def move(self): return self.player.move()