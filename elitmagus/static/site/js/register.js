function validate()                                    
{ 
    var email = document.forms["registerform"]["email"];               
    var password = document.forms["registerform"]["password"];    
    var fname = document.forms["registerform"]["fname"];  
    var lname =  document.forms["registerform"]["lname"];  
    var dob = document.forms["registerform"]["dob"];  
    var phone = document.forms["registerform"]["phone"];  
    var add1 = document.forms["registerform"]["add1"];  
    var add2 = document.forms["registerform"]["add2"];  
    var city = document.forms["registerform"]["city"];  
    var province = document.forms["registerform"]["province"];  
    var zip = document.forms["registerform"]["zip"];  
    
    if (email.value == "")                                   
    { 
    	document.getElementById("msg").innerHTML = "your message";
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
    if (password.value == "0")                                   
    { 
        window.alert("Please enter a valid password."); 
        password.focus(); 
        return false; 
    } 
    if (fname.value == "")                                  
    { 
        window.alert("Please enter your first name."); 
        fname.focus(); 
        return false; 
    } 
   
    if (lname.value == "")                               
    { 
        window.alert("Please enter your last name."); 
        lname.focus(); 
        return false; 
    } 
       
    if (dob.value == "")                           
    { 
        window.alert("Please enter your Date of Birth."); 
        dob.focus(); 
        return false; 
    } 
   
    if (phone.value == "")                           
    { 
        window.alert("Please enter your telephone number."); 
        phone.focus(); 
        return false; 
    } 
   
    if (add1.value == "")                           
    { 
        window.alert("Please enter your address."); 
        add1.focus(); 
        return false; 
    } 
   
    if (city.value == "")                           
    { 
        window.alert("Please enter your city."); 
        city.focus(); 
        return false; 
    }
    if (province.value == "")                           
    { 
        window.alert("Please enter your province."); 
        province.focus(); 
        return false; 
    }
    if (zip.value == "")                           
    { 
        window.alert("Please enter your zip."); 
        zip.focus(); 
        return false; 
    } 
   
    return true; 
}