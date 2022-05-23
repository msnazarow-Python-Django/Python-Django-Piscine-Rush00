from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Moviemon.mixins import GamedataContextMixin
from Moviemon.GameManager import GameManager, GameState

game_manager: GameManager = GameManager()


class BattleView(GamedataContextMixin, TemplateView):
    template_name = "battle.html"

    def get(self, request, *args, **kwargs):
        if game_manager.game_data.current_page != f'/battle/{kwargs["moviemon_id"]}':
            return redirect(game_manager.game_data.current_page)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        key = request.POST.get('KEY')
        if key == "B":
            game_manager.game_data.current_page = "/worldmap"
            return redirect('/worldmap')
        elif key == "A" and False:
            pass  # do logic

        game_manager.game_data.state == GameState.worldmap
        return HttpResponseRedirect(request.path_info)
