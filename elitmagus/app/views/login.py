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

    #deleting the session variable 
    try:
        del request.session['userid']
    except KeyError:
        pass
    try:
        del request.session['regError']
    except KeyError:
        pass
    try:
        del request.session['title']
    except KeyError:
        pass
    try:
        del request.session['movieid']
    except KeyError:
        pass

    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"

    else:
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
            if r["password"] == passwordTyped:
                valid = 1
                userId = r["user_id"]
        
        print("rescnt")
        print(resCnt)
        
        if valid == 1 and resCnt == 1:
            request.session['userid'] = userId
            message = "Success"
        elif valid == 0 and resCnt == 1:
            message = "Wrong password"
        elif valid == 1 and resCnt > 1:
            valid = 0
            message = "Multiple users"
        else:
            message = "Invalid username"
        print(valid)
        print(message)
    data = {    
        'valid': valid,
        'message': message,
    }
    
    return JsonResponse(data)