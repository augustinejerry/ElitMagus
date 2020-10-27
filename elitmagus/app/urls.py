from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('validatelogin',views.validateLogin, name = 'validatelogin'),
    path('homepage',views.homepage, name = 'homepage'),
    path('registerload',views.registerLoad, name = 'registerload'),
    path('register',views.createUser, name = 'createUser')
]