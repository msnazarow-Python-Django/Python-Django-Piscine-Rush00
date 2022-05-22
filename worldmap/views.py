from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class WorldmapView(TemplateView):
    template_name = "worldmap.html"

    def post(self, request):
        if request.POST.get('START'):
            return redirect('options')
        elif request.POST.get('SELECT'):
            return redirect('moviedex')
        elif request.POST.get('A') and False:
            return redirect('battle')
        elif request.POST.get('UP'):
            pass #logic
        elif request.POST.get('DOWN'):
            pass #logic
        elif request.POST.get('RIGHT'):
            pass #logic
        elif request.POST.get('LEFT'):
            pass #logic
        else:
            return HttpResponseRedirect(request.path_info)