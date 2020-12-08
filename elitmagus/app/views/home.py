from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .recommendation import simpleRecommender
from .recommendation import get_recommendations_overview
from .recommendation import get_recommendations_cast
from .recommendation import get_recommendations_user
from .movies import movies

#to load homepage
def homepage(request):
    print(request.session['userid'])
    result = simpleRecommender(request)
    # result = movies()
    # result = get_recommendations_overview("The Dark Knight Rises")
    # result = get_recommendations_cast("The Dark Knight Rises")
    # result = get_recommendations_user(1)
    return render(request, 'home.html', {'sessionvar' : result})

def clickedMovie(request):
    request.session['movieid'] = request.POST.get('movieId', None)