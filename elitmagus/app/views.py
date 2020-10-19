from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pyodbc
import pymongo
from django.http import HttpResponseRedirect
from .forms import registerForm 

#to load login page
def login(request):
    return render(request, 'login.html')

#to load register page
def registerload(request):
    return render(request, 'register.html')

#to authenticate the login
def validatelogin(request):
    data = {
        'valid': 1,
        'message': 'Success',
    }
    request.session['userid'] = 234        #store userid in session variable
    return JsonResponse(data)

#to insert the new user details to the db
def createUser(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = registerForm(request.POST)
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
            print("hello inside is valid")
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']               
            password = form.cleaned_data['password']    
            fname = form.cleaned_data['fname']  
            lname =  form.cleaned_data['lname']  
            dob = form.cleaned_data['dob']  
            phone = form.cleaned_data['phone']  
            add1 = form.cleaned_data['add1']  
            add2 = form.cleaned_data['add2']  
            city = form.cleaned_data['city']  
            province = form.cleaned_data['province']  
            zip = form.cleaned_data['zip']
            print(fname)
            # redirect to a new URL:
            return render(request, 'homepage.html', {'sessionvar' : fname})

    # if a GET (or any other method) we'll create a blank form
    else:
        print("hello inside else")
        form = registerForm()
    print("hello")
    return render(request, 'register.html', {'form': form})

#to load homepage
def homepage(request):
    return render(request, 'homepage.html', {'sessionvar' : request.session['userid']})