from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import View, TemplateView
from Moviemon.GameManager import GameManager
from Moviemon.mixins import GamedataContextMixin

game_manager: GameManager = GameManager()
# Create your views here.
class MoviedexView(GamedataContextMixin, View):

    def get(self, request):
        context = self.get_context_data()
        game_data = game_manager.game_data

        # TODO it's for testing, don't forget delete string below!!!
        # game_data.captured_moviemon_ids = [
        #     movie_id for movie_id in game_data.movie_info
        # ]
        catched_movies_ids = game_data.captured_moviemon_ids
        moviemons = [game_data.movie_info[movie_id] for movie_id in catched_movies_ids]

        display_movies = [None, None, None]
        mov_pos = game_data.moviedex_position
        no_catched = True
        for i in range(3):
            movie = None
            if mov_pos + i - 1 >= 0 and i < len(moviemons):
                movie = moviemons[mov_pos - 1 + i]
                no_catched = False
            display_movies[i] = {
                'movie': movie,
                'i': i
                }
        context['display_movies'] = display_movies
        context['no_catched'] = no_catched
        return render(request, "moviedex/index.html", context)

    def post(self, request):

        key = request.POST.get('KEY')
        print(key)
        if key == 'SELECT':
            return redirect('worldmap')
        elif key == 'A':
            if not game_manager.game_data.captured_moviemon_ids:
                return HttpResponseRedirect(request.path_info)
            movie_id = game_manager.game_data.captured_moviemon_ids[
                game_manager.game_data.moviedex_position
            ]
            return HttpResponseRedirect(f'/moviedex/{movie_id}')
        elif key == 'UP':
            game_manager.change_moviedex_position(-1)
        elif key == 'DOWN':
            game_manager.change_moviedex_position(1)
        return HttpResponseRedirect(request.path_info)


class MoviedexDetailView(GamedataContextMixin, View):
    def get(self, request, movie_id):
        context = self.get_context_data()
        game_data = game_manager.game_data
        if movie_id not in game_data.captured_moviemon_ids:
            return HttpResponseNotFound('Movie not found')
        context['movie'] = game_data.movie_info[movie_id]
        return render(request, 'moviedex/detail.html', context)

    def post(self, request, movie_id):
        key = request.POST.get('KEY')
        if key == 'B':
            return redirect('moviedex:index')
        else:
            return HttpResponseRedirect(request.path_info)




