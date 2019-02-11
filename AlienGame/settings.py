class Settings():
	
	def __init__(self):

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,200,180)
		self.ship_speed_factor = 3
		self.ship_limit = 3
		self.alien_speed_factor = 1	
		self.alien_points = 100
		self.bullet_speed_factor = 30
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (69,69,69)
		self.bullets_allowed = 5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 # -1 for left, 1 for right
