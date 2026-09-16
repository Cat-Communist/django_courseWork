from django.shortcuts import render
from cinema.models import Movie
from django.views.generic import TemplateView
from typing import Any

# Create your views here.
class ShowMoviesView(TemplateView):
    template_name = "movies/show_movies.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()

        return context
        