from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .utilities import *

#to load login page
def login(request):
    return render(request, 'login.html')

#to authenticate the login
def validateLogin(request):
    usernameTyped = request.POST.get('username', None)
    passwordTyped = request.POST.get('password', None)
    connection = connectMongo()

    resCnt = 0
    valid = 0

    # Database Name 
    db = connection["elitmagus"] 
    
    # Collection Name 
    coll = db["users"] 

    #fetch user details
    result = coll.find({"email":usernameTyped},{ "_id": 0, "user_id": 1, "password": 1 })
    for r in result:
        resCnt += 1
        print(r["password"] + passwordTyped)
        if r["password"] == passwordTyped:
            valid = 1
            userId = r["user_id"]
    
    if valid == 1 and resCnt == 1:
        request.session['userid'] = userId
        message = "Success"
    elif valid == 0 and resCnt == 1:
        message = "Wrong password"
    elif valid == 1 and resCnt > 1:
        message = "Multiple users"
    else:
        message = "Invalid username"
    
    data = {    
        'valid': valid,
        'message': message,
    }
    
    return JsonResponse(data)