from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import registerForm 
from .utilities import *

#to load register page
def registerLoad(request):
    try:
        del request.session['regError']
    except KeyError:
        pass
    return render(request, 'register.html')

#to insert the new user details to the db
def createUser(request):
    if request.method == 'POST':
        valid = 0
        errorMessage = ''
        userExists = 0
        # create a form instance and populate it with data from the request:
        form = registerForm(request.POST)
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
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
            
            if connection == -1:
                valid = -1
                message = "Error in establishing connection with the database"

            else:
                inserted = 0

                # Database Name 
                db = connection["elitmagus"] 
                
                # Collection Name 
                coll = db["users"] 

                #checking the email is already registered or not
                result = coll.find({"email":email},{ "_id": 0, "user_id": 1, "password": 1 })
                for r in result:
                    userExists = 1
                
                if userExists == 1:
                    form = registerForm()
                    request.session['regError'] = 'email already exists'
                    return render(request, 'register.html', {'form': form})

                #fetch the maximum user id
                result = coll.aggregate([{"$group":
                            {
                              "_id" : "null",
                              "maxId" : {"$max" : "$user_id"}
                            }
                        }])
                print(result)

                for r in result:
                    userId = r["maxId"] + 1
                    print(r["maxId"])
                    valid = 1

                if valid == 1 :
                    #create the document to be inserted
                    document = {"user_id" : userId, 
                                "email" : email, 
                                "password" : password,
                                "fname" : fname,
                                "lname" : lname,
                                "dob" : dob,
                                "phone" : phone,
                                "address" : {"address_line_1" : add1,
                                            "address_line_2" : add2,
                                            "city" : city,
                                            "province" : province,
                                            "zip" : zip}
                            }
                    try:
                        #insert it
                        coll = coll.insert_one(document)
                        request.session['userid'] = userId
                        inserted = 1
                    except Exception as e:
                        print("An exception occurred ::", e)
                        valid = -1
                        errorMessage = e
        if valid == 1:
            #deleting the session variable 
            try:
                del request.session['regError']
            except KeyError:
                pass
            return redirect('homepage')
        else:
            form = registerForm()
            request.session['regError'] = errorMessage
            return render(request, 'register.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = registerForm()
        errorMessage = "POST is not used"
        request.session['regError'] = errorMessage
        return render(request, 'register.html', {'form': form})