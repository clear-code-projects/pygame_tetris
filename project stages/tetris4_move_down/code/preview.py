from settings import * 

class Preview:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
		self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING,PADDING))

	def run(self):
		self.display_surface.blit(self.surface, self.rect)