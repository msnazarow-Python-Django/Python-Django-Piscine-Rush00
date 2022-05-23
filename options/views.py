from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from Moviemon.mixins import GamedataContextMixin
from Moviemon.GameManager import GameManager


class LoadView(GamedataContextMixin, View):
    def get(self, request):
        context = self.get_context_data()
        game_data = GameManager().game_data
        context['slots'] = game_data.save_slots
        context['a_button'] = 'Load'
        return render(request, 'saveload.html', context)

    def post(self, request):
        if not GameManager().game_data.loaded:
            key = request.POST.get('KEY')

            if key == 'A':
                GameManager().load_game()
            elif key == 'B':
                GameManager().reset_slot_position()
                return redirect('mainpage')
            elif key == 'UP':
                GameManager().change_slot_position(-1)
            elif key == 'DOWN':
                GameManager().change_slot_position(1)
            return HttpResponseRedirect(request.path_info)
        else:
            GameManager().game_data.loaded = False
            GameManager().reset_slot_position()
            return redirect('worldmap')


class SaveView(GamedataContextMixin, View):
    def get(self, request):
        context = self.get_context_data()
        game_data = GameManager().game_data
        context['slots'] = game_data.save_slots
        context['a_button'] = 'Save'
        return render(request, 'saveload.html', context)

    def post(self, request, *args, **kwargs):
        key = request.POST.get('KEY')
        if key == 'A':
            GameManager().save_game()
            return HttpResponseRedirect(request.path_info)
        elif key == 'B':
            GameManager().reset_slot_position()
            return redirect('options')
        elif key == 'UP':
            GameManager().change_slot_position(-1)
        elif key == 'DOWN':
            GameManager().change_slot_position(1)
        return HttpResponseRedirect(request.path_info)


class OptionsView(TemplateView):
    template_name = "options.html"

    def post(self, request, *args, **kwargs):
        key = request.POST.get('KEY')
        if key == 'A':
            return redirect('save_game')
        elif key == 'START':
            return redirect('worldmap')
        elif key == 'B':
            return redirect('mainpage')
        else:
            return HttpResponseRedirect(request.path_info)
