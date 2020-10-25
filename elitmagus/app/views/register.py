from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import registerForm 
from .utilities import *

#to load register page
def registerLoad(request):
    return render(request, 'register.html')

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

            connection = connectMongo()
            resCnt = 0
            valid = 0

            # Database Name 
            db = connection["elitmagus"] 
            
            # Collection Name 
            coll = db["users"] 

            # document = {"user_id" : 1, 
            #             "email" : "sample@gmail.com", 
            #             "password" : "123",
            #             "fname" : "sample",
            #             "lname" : "1",
            #             "dob" : new Date("1994-12-11"),
            #             "phone" : 5454545214,
            #             "address" : {"address_line_1" : "25 Celeste Drive",
            #                         "address_line_2" : "Scarborough",
            #                         "city" : "Toronto",
            #                         "province" : "Ontario",
            #                         "zip" : "M1E2V6"}
            #            }
            
            # redirect to a new URL:
            return render(request, 'homepage.html', {'sessionvar' : fname})

    # if a GET (or any other method) we'll create a blank form
    else:
        print("hello inside else")
        form = registerForm()
    print("hello")
    return render(request, 'register.html', {'form': form})