from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class LoadView(TemplateView):
    template_name = "saveload.html"

    def post(self, request):
        return HttpResponseRedirect(request.path_info)

class SaveView(TemplateView):
    template_name = "saveload.html"

    def post(self, request):
        return HttpResponseRedirect(request.path_info)