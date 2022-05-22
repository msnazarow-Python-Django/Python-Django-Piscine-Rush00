from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Moviemon.mixins import GamedataContextMixin
from Moviemon.GameManager import GameManager, GameState

game_manager = GameManager()


class BattleView(GamedataContextMixin, TemplateView):
    template_name = "battle.html"

    def post(self, request):
        key = request.POST.get('KEY')
        if key == "B":
            return redirect('worldmap')
        elif key == "A" and False:
            pass  # do logic
        else:
            return HttpResponseRedirect(request.path_info)
