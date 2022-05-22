from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from Moviemon.GameManager import GameManager
from Moviemon.mixins import GamedataContextMixin


# Create your views here.
class MoviedexView(GamedataContextMixin, View):
    template_name = "moviedex/index.html"
    context = {}

    def get(self, request):
        context = self.get_context_data()
        game_data = GameManager().game_data
        catched_movies_id = game_data.captured_moviemon_ids
        # moviemons = [game_data.movie_info[movie_id] for movie_id in catched_movies_id]
        # TODO uncomment  string above and delete string below. It's for testing
        moviemons = [movie for movie in game_data.movie_info.values()]
        display_movies = [None, None, None]
        mov_pos = game_data.moviedex_position

        for i in range(3):
            if mov_pos + i - 1 >= 0 and i < len(moviemons):
                display_movies[i] = {
                    'movie': moviemons[mov_pos - 1 + i],
                    'i': i
                }
        context['display_movies'] = display_movies
        return render(request, "moviedex/index.html", context)

    def post(self):
        context = self.get_context_data()

class MoviedexDetailView(GamedataContextMixin, TemplateView):
    template_name = "moviedex/detail.html"
    context = {}
