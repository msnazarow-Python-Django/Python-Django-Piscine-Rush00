import pickle
import random
from dataclasses import dataclass
from enum import Enum

from django.conf import settings
from moviedex.service import Moviemon


class GameState(Enum):
    start_screen = 0
    worldmap = 1
    ready_to_battle = 2
    in_battle = 3
    moviedex = 4
    moviedex_detail = 5
    saving = 6
    loading = 7
    options = 8


def singleton(class_) -> 'GameManager()':
    instanses = {}

    def getinstansce(*args, **kwargs):
        if class_ not in instanses:
            instanses[class_] = class_(*args, **kwargs)
        return instanses[class_]

    return getinstansce


@dataclass
class GameData:
    player_strength: int
    player_position: (int, int)
    player_movieballs: int
    captured_moviemon_ids: {str}
    movie_info: {str: Moviemon}
    moviedex_position: int
    state: GameState


@singleton
class GameManager:

    def __init__(self):
        self.game_data = GameData(settings.DEFAULT_PLAYER_STRENGTH,
                                  settings.DEFAULT_PLAYER_POSITION,
                                  0,
                                  {},
                                  Moviemon.get_movies(),
                                  0,
                                  GameState.start_screen)

    def load(self, game_data: GameData):
        self.game_data = game_data
        return self

    def dump(self) -> GameData:
        return self.game_data

    def get_random_movie(self) -> Moviemon:
        return random.choice(settings.MOVIE_IDS - self.game_data.captured_moviemon_ids)

    def get_strength(self) -> int:
        return self.game_data.player_strength

    def load_default_settings(self) -> 'GameManager':
        self.game_data = GameData(settings.DEFAULT_PLAYER_STRENGTH,
                                  settings.DEFAULT_PLAYER_POSITION,
                                  0,
                                  {},
                                  Moviemon.get_movies(),
                                  0,
                                  GameState.start_screen)
        return self

    def get_movie(self, id: int):
        return self.game_data.movie_info[id]

    def save(self, slot_name):
        with open(f"slot{slot_name}_{len(self.game_data.captured_moviemon_ids)}_{len(settings.MOVIE_IDS)}.mmg",
                  "wb") as save_file:
            pickle.dump(self.dump(), save_file)

    def quick_save(self):
        with open("current_game.mmg", "wb") as current_game:
            pickle.dump(self.dump(), current_game)

    def load_file(self, save_file):
        with open(save_file, "rb") as save_file:
            self.load(pickle.load(save_file))

