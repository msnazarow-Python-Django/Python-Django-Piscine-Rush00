from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class WorldmapView(TemplateView):
    template_name = "worldmap.html"