import pickle
import random
from dataclasses import dataclass
from settings import DEFAULT_PLAYER_POSITION, MAP_SIZE, MOVIE_IDS, DEFAULT_PLAYER_STRENGTH
from moviedex.service import Moviemon


@dataclass
class GameData:
    player_strength: int
    player_position: (int, int)
    player_movieballs: int
    captured_moviemon_ids: {str}
    movie_info: {str: Moviemon}


class GameManager:

    def __init__(self):
        self._game_data = GameData(DEFAULT_PLAYER_STRENGTH, DEFAULT_PLAYER_POSITION, 0, {}, Moviemon.get_movies())

    def load(self, game_data: GameData):
        self._game_data = game_data
        return self

    def dump(self) -> GameData:
        return self._game_data

    def get_random_movie(self) -> Moviemon:
        return random.choice(MOVIE_IDS - self._game_data.captured_moviemon_ids)

    def get_strength(self) -> int:
        return self._game_data.player_strength

    def load_default_settings(self) -> 'GameManager':
        self._game_data = GameData(DEFAULT_PLAYER_STRENGTH, DEFAULT_PLAYER_POSITION, 0, {}, Moviemon.get_movies())
        return self

    def get_movie(self, id: int):
        return self._game_data.movie_info[id]

    def save(self, slot_name):
        with open(f"slot{slot_name}_{len(self._game_data.captured_moviemon_ids)}_{len(MOVIE_IDS)}.mmg",
                  "wb") as save_file:
            pickle.dump(self.dump(), save_file)

    def quick_save(self):
        with open("current_game.mmg", "wb") as current_game:
            pickle.dump(self.dump(), current_game)

    def load_file(self, save_file):
        with open(save_file, "rb") as save_file:
            self.load(pickle.load(save_file))



if __name__ == '__main__':
    game_manager = GameManager()
