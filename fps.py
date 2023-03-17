import pygame

class FPSCounter():
	def __init__(self, canvas, clock, settings) -> None:
		self.canvas = canvas
		self.clock = clock
		self.settings = settings

		self.font = pygame.font.Font(*self.settings['Font'])

		return

	def draw(self) -> None:
		label = self.font.render(self.__getText(), False, self.settings['TextColor'])

		labelRect = label.get_rect()
		labelRect.topright = (pygame.display.get_window_size()[0], 0)

		self.canvas.blit(label, labelRect)

		return

	def __getText(self) -> str:
		return str(int(self.clock.get_fps())) + ' fps'