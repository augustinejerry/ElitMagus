from django import forms

class registerForm(forms.Form):
    email = forms.CharField(label = 'email', max_length = 100)               
    password = forms.CharField(label = 'password', max_length = 100)    
    fname = forms.CharField(label = 'fname', max_length = 100)  
    lname =  forms.CharField(label = 'lname', max_length = 100)  
    dob = forms.CharField(label = 'dob', max_length = 100)  
    phone = forms.CharField(label = 'phone', max_length = 100)  
    add1 = forms.CharField(label = 'add1', max_length = 100)  
    add2 = forms.CharField(label = 'add2', max_length = 100)  
    city = forms.CharField(label = 'city', max_length = 100)  
    province = forms.CharField(label = 'province', max_length = 100)  
    zip = forms.CharField(label = 'zip', max_length = 100)  
