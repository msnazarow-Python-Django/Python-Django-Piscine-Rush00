from django.shortcuts import render, redirect
from django.views import generic
from Moviemon.mixins import GamedataContextMixin


class IndexView(GamedataContextMixin, generic.TemplateView):
    template_name = 'mainpage/index.html'

    def post(self, request):
        key = request.POST.get("KEY")
        if key == "A":
            return redirect('worldmap')
        elif key == "B":
            return redirect('load_game')
