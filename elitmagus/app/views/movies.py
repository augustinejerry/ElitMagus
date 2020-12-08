import pandas as pd
from django.shortcuts import render
from .utilities import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator


#to load login page
def movies():
    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        movies = ""

    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 
        
        # Collection Name 
        coll = db["poster"] 

        #fetch user details
        result = coll.find({},{ "_id": 0, "id": 1, "poster_path": 1, "title": 1, "tagline": 1})
        movies = pd.DataFrame(list(result))
        movies = movies.to_dict('records')
    
    return movies

#funtion to store movieId in session variable
def movieSession(request):
    movieId = request.POST.get('movieId', None)
    title = request.POST.get('title', None)
    request.session['movieid'] = movieId
    request.session['title'] = title
    valid = 1
    message = "success"
    data = {    
        'valid': valid,
        'message': message
    }
    return JsonResponse(data)

#funtion to get description of a particular movie
def movieDesc(request):
    movieId = request.session.get('movieid')
    title = request.session.get('title')
    movie = int(movieId)

    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        moviedetails = ""

    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 
        
        # Collection Name 
        coll = db["poster"] 

        #fetch user details
        result = coll.find({"id":movie},{ "_id": 0, "id": 1, "poster_path": 1, "title": 1, "tagline": 1, "genres":1, "overview":1})
        moviedetails = pd.DataFrame(list(result))
        moviedetails = moviedetails.to_dict('records')

    data = {    
        'valid': valid,
        'message': message,
        'moviedetails': moviedetails
    }
    
    return render(request, 'moviedesc.html', {'sessionvar' : data})

def movieList(request):
    movieList = movies()
    # Show 24 mvoies per page.
    paginator = Paginator(movieList, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if isinstance(page_number, str):
        page_number = int(page_number)
    else:
        page_number = 1
    i = page_number + 1
    k = 1
    pages = []
    while i<=paginator.num_pages and k<5:
        pages.append(i)
        i = i + 1
        k = k + 1
    return render(request, 'homepage.html', {'page_obj': page_obj, 'pages':pages})
