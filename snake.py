import pygame
from collections import deque
from functools import reduce
from operator import sub

class Snake:
	def __init__(self, canvas, settings):
		self.settings = settings['Obj']['Player']
		self.scale = settings['Env']['Scale']

		self.canvas = canvas
		self.dir = (0, -1)
		self.loc = deque([self.settings['StartPos']])
		
		self.refresh = pygame.USEREVENT
		pygame.time.set_timer(self.refresh, self.settings['RefreshRate'])

		return

	def __len__(self): return len(self.loc)

	def __getNeighborDirs(self, pos = 0):
		out = []

		if not pos == 0:
			out.append(tuple(a - b for a, b in zip(self.loc[pos - 1], self.loc[pos])))
		if pos < len(self) - 1:
			out.append(tuple(a - b for a, b in zip(self.loc[pos + 1], self.loc[pos])))

		return [pos] + out

	def getPos(self): return list(self.loc)

	def move(self, food = False):
		if not food: print('Sneaky snake on the move!')
		else: print("Sneaky snake loves apples!")

		newLoc = [a + b for a, b in zip(self.dir, self.loc[0])]
		self.loc.appendleft(newLoc)
		if not food: self.loc.pop()

		return True

	def draw(self):
		for x, y in self.loc:
			pygame.draw.rect(
				self.canvas,
				(120, 120, 120),
				pygame.Rect(*(a * b for a, b in zip([x, y], self.scale)), self.scale[0], self.scale[1])
			)
			pygame.draw.rect(
				self.canvas,
				self.settings['BodyColor'],
				pygame.Rect(x * self.scale[0] + 5, y * self.scale[1] + 5, self.scale[0] - 10, self.scale[1] - 10)
			)
		return

	def input(self, key):
		if self.settings['Keys'][key] not in self.__getNeighborDirs():
			self.dir = self.settings['Keys'][key]