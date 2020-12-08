from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('login',views.login, name = 'loginlogout'),
    path('validatelogin',views.validateLogin, name = 'validatelogin'),
    path('homepage',views.movieList, name = 'homepage'),
    path('registerload',views.registerLoad, name = 'registerload'),
    path('register',views.createUser, name = 'createUser'),
    path('setmoviedesc',views.movieSession, name = 'movieSession'),
    path('moviedesc',views.movieDesc, name = 'movieDesc'),
    path('simpleRecommender',views.simpleRecommender, name = 'simpleRecommender'),
    path('overviewRecommender',views.get_recommendations_overview, name = 'overviewRecommender'),
    path('castRecommender',views.get_recommendations_cast, name = 'castRecommender'),
    path('userRecommender',views.get_recommendations_user, name = 'userRecommender'),
    path('test',views.homepage, name = 'test'),
]