from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class BattleView(TemplateView):
    template_name = "battle.html"

    def post(self, request):
        return HttpResponseRedirect(request.path_info)