from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class WorldmapView(TemplateView):
    template_name = "worldmap.html"

    def post(self, request):
        return HttpResponseRedirect(request.path_info)