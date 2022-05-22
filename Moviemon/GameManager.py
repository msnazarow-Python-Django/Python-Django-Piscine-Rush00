from dataclasses import dataclass


@dataclass
class GameData:
	player_position: (int, int)
	player_movieballs: int
	player_strenght: int
	captured_moviemon_ids: [int]
	all_moviemon_ids: [int]
	map_size: (int, int)

class GameManager:

	def __init__(self):
		self.game_data = GameData()

	def load(self, game_data: GameData):
		data = pickle.loads(self.loaded_data)
		self.player_position = data[0]
		self.player_movieballs = data[1]
		self.player_strength = data[2]
		self.captured_moviemons = data[3]
		self.film_ids = data[4]
		self.grid_size = data[5]
		self.moviemons_info = data[6]
		self.bushes = data[7]
	def dump(self):
		return game_data