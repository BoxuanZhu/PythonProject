class GameStats():
	
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.ships_left = 0
		self.game_active = False
		self.score = 0
		self.reset_stats()

	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
