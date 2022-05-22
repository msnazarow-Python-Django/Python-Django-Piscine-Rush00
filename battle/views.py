from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class BattleView(TemplateView):
    template_name = "battle.html"

    def post(self, request):
        if request.POST.get('B'):
            return redirect('worldmap')
        elif request.POST.get('A') and False:
            pass # do logic
        else:
            return HttpResponseRedirect(request.path_info)