from django.shortcuts import render, redirect
from django.views import generic

from Moviemon.GameManager import GameManager, GameState
from Moviemon.mixins import GamedataContextMixin

game_manager: GameManager = GameManager()
class IndexView(GamedataContextMixin, generic.TemplateView):
    template_name = 'mainpage/index.html'

    def post(self, request):
        key = request.POST.get("KEY")
        if key == "A":
            game_manager.game_data.state = GameState.worldmap
            return redirect('worldmap')
        elif key == "B":
            game_manager.game_data.state = GameState.loading
            return redirect('load_game')
