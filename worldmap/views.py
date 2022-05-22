from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from Moviemon.GameManager import GameState, GameManager
from Moviemon.mixins import GamedataContextMixin


game_manager: GameManager = GameManager()


class WorldmapView(GamedataContextMixin, TemplateView):
    template_name = "worldmap.html"

    def post(self, request):
        key = request.POST.get('KEY')
        if key == 'START':
            return redirect('options')
        elif key == 'SELECT':
            return redirect('moviedex')
        elif key == 'A':
            if game_manager.game_data.state == GameState.ready_to_battle:
                return redirect('battle')
            elif game_manager.game_data.state == GameState.movieball_found:
                return HttpResponseRedirect(request.path_info)
        elif key == "UP" or key == "DOWN" or key == "RIGHT" or key == "LEFT":
            game_manager.move(key)
            return HttpResponseRedirect(request.path_info)
        else:
            return HttpResponseRedirect(request.path_info)
