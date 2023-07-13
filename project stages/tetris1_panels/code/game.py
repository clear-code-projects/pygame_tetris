from settings import *

class Game:
	def __init__(self):

		# general 
		self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
		self.display_surface = pygame.display.get_surface()

	def run(self):
		self.display_surface.blit(self.surface, (PADDING,PADDING))