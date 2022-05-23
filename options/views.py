from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Moviemon.mixins import GamedataContextMixin


class LoadView(GamedataContextMixin, TemplateView):
    template_name = "saveload.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get('A'):
            pass #logic
        elif request.POST.get('UP'):
            pass  # logic
        elif request.POST.get('DOWN'):
            pass  # logic
        elif request.POST.get('B'):
            return redirect('mainpage')
        else:
            return HttpResponseRedirect(request.path_info)

class SaveView(TemplateView):
    template_name = "saveload.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get('A'):
            pass #logic
        elif request.POST.get('UP'):
            pass  # logic
        elif request.POST.get('DOWN'):
            pass  # logic
        elif request.POST.get('B'):
            return redirect('options')
        else:
            return HttpResponseRedirect(request.path_info)

class OptionsView(TemplateView):
    template_name = "options.html"

    def post(self, request, *args, **kwargs):
        key = request.POST.get('KEY')
        if key == 'A':
            return redirect('save')
        elif key == 'START':
            return redirect('worldmap')
        elif key == 'B':
            return redirect('mainpage')
        else:
            return HttpResponseRedirect(request.path_info)