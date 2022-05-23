import pickle
import random
from dataclasses import dataclass
from enum import Enum
from math import floor, ceil

from singleton_decorator import singleton
from django.conf import settings
from moviedex.service import Moviemon
import numpy as np


class GameState(Enum):
    start_screen = 0
    worldmap = 1
    movieball_found = 9
    ready_to_battle = 2
    in_battle = 3
    moviedex = 4
    moviedex_detail = 5
    saving = 6
    loading = 7
    options = 8


@dataclass
class GameData:
    player_strength: int
    player_position: [int]
    player_movieballs: int
    captured_moviemon_ids: [str]
    non_captured_moviemon_ids: {str}
    movie_info: {str: Moviemon}
    moviedex_position: int
    state: GameState
    map: [[int]]


@singleton
class GameManager:

    def __init__(self):
        self.game_data: GameData
        self.load_default_settings()

    def load(self, game_data: GameData):
        self.game_data = game_data
        return self

    def dump(self) -> GameData:
        return self.game_data

    def get_random_movie(self) -> Moviemon:
        return random.choice(settings.MOVIE_IDS - set(self.game_data.captured_moviemon_ids))

    def get_strength(self) -> int:
        return self.game_data.player_strength

    def load_default_settings(self) -> 'GameManager':
        self.game_data = GameData(player_strength=settings.DEFAULT_PLAYER_STRENGTH,
                                  player_position=list(settings.DEFAULT_PLAYER_POSITION),
                                  player_movieballs=settings.DEFAULT_PLAYER_MOVIEBALLS,
                                  captured_moviemon_ids=[],
                                  non_captured_moviemon_ids=settings.MOVIE_IDS,
                                  movie_info=Moviemon.get_movies(),
                                  moviedex_position=0,
                                  state=GameState.start_screen,
                                  map=np.zeros((settings.MAP_SIZE[0], settings.MAP_SIZE[1])))

        for i in range(min(len(settings.MOVIE_IDS), max(settings.FRAME_SIZE))):
            self.game_data.map[random.randint(0, settings.MAP_SIZE[0] - 1)][random.randint(0, settings.MAP_SIZE[0] - 1)] = 2
            self.game_data.map[random.randint(0, settings.MAP_SIZE[0] - 1)][random.randint(0, settings.MAP_SIZE[0] - 1)] = 1

        self.game_data.map[self.game_data.player_position[1], self.game_data.player_position[0]] = -1

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

    def frame(self):
        leftX = 0
        rightX = settings.FRAME_SIZE[0]
        topY = 0
        bottomY = settings.FRAME_SIZE[1]
        left_padding = floor(settings.FRAME_SIZE[0] / 2)
        right_padding = ceil(settings.FRAME_SIZE[0] / 2)
        top_padding = floor(settings.FRAME_SIZE[0] / 2)
        bottom_padding = ceil(settings.FRAME_SIZE[0] / 2)
        half_height = settings.FRAME_SIZE[1] // 2
        leftX = min(settings.MAP_SIZE[0] - settings.FRAME_SIZE[0], max(self.game_data.player_position[0] - left_padding, 0))
        rightX = min(settings.MAP_SIZE[0], max(self.game_data.player_position[0] + right_padding, settings.FRAME_SIZE[0]))
        topY = min(settings.MAP_SIZE[1] - settings.FRAME_SIZE[1], max(self.game_data.player_position[1] - top_padding, 0))
        bottomY = min(settings.MAP_SIZE[1], max(self.game_data.player_position[1] + bottom_padding, settings.FRAME_SIZE[1]))

        return self.game_data.map[topY: bottomY, leftX: rightX]

    def move(self, direction):
        self.game_data.map[self.game_data.player_position[1]][self.game_data.player_position[0]] = 0
        if direction == "LEFT":
            self.game_data.player_position[0] = max(self.game_data.player_position[0] - 1, 0)
        elif direction == "RIGHT":
            self.game_data.player_position[0] = min(self.game_data.player_position[0] + 1, settings.MAP_SIZE[0] - 1)
        elif direction == "UP":
            self.game_data.player_position[1] = max(self.game_data.player_position[1] - 1, 0)
        elif direction == "DOWN":
            self.game_data.player_position[1] = min(self.game_data.player_position[1] + 1, settings.MAP_SIZE[1] - 1)

        if self.game_data.map[self.game_data.player_position[1]][self.game_data.player_position[0]] == 1:
            self.game_data.state = GameState.movieball_found
        elif self.game_data.map[self.game_data.player_position[1]][self.game_data.player_position[0]] == 2:
            self.game_data.state = GameState.ready_to_battle

        self.game_data.map[self.game_data.player_position[1], self.game_data.player_position[0]] = -1

    def change_moviedex_position(self, value):
        new_position = self.game_data.moviedex_position + value
        if 0 < new_position < len(self.game_data.captured_moviemon_ids):
            self.game_data.moviedex_position = new_position