from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from Moviemon.GameManager import GameManager
from Moviemon.mixins import GamedataContextMixin


# Create your views here.
class MoviedexView(GamedataContextMixin, TemplateView):
    template_name = "moviedex/index.html"
    context = {}

    def post(self):
        pass

class MoviedexDetailView(GamedataContextMixin, TemplateView):
    template_name = "moviedex/detail.html"
    context = {}
