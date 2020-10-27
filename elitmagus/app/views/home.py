from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

#to load homepage
def homepage(request):
    return render(request, 'homepage.html', {'sessionvar' : request.session['userid']})