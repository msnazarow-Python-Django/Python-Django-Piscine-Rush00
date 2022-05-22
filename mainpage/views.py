from django.shortcuts import render, redirect
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'mainpage/index.html'

    def post(self, request):
        print(request.POST)
        if request.POST.get('A'):
            return redirect('worldmap')
        elif request.POST.get('B'):
            return redirect('load')