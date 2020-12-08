function validate() {
	var email = document.forms["registerform"]["email"];
	var password = document.forms["registerform"]["password"];
	var fname = document.forms["registerform"]["fname"];
	var lname = document.forms["registerform"]["lname"];
	var dob = document.forms["registerform"]["dob"];
	var contact = document.forms["registerform"]["phone"];
	var add1 = document.forms["registerform"]["add1"];
	var add2 = document.forms["registerform"]["add2"];
	var city = document.forms["registerform"]["city"];
	var province = document.forms["registerform"]["province"];
    var zip = document.forms["registerform"]["zip"];
	if (ValidateEmail(email)) {
		if (password_validation(password)) {
			if (firstname_validation(fname)) {
				if (lastname_validation(lname)) {
					if (Validate_dob(dob)) {
						if (Validate_phone(contact)) {
							if (add1_validation(add1)) {
								alert("dsfds");
								/*
if(alphanumeric(add2))
{ 
if(allnumeric(uzip))
{
}
} 
}
} 
}
*/
							}
						}
					}
				}
			}
		}
	}
	return true;

	function Validate_dob(dob) {
		var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
		// Match the date format through regular expression
		if (dob.value == "") {
			alert("Date of birth cannot be empty")
		} else if (dob.value.match(dateformat)) {
			dob.focus();
			//Test which seperator is used '/' or '-'
			var opera1 = dob.value.split('/');
			var opera2 = dob.value.split('-');
			lopera1 = opera1.length;
			lopera2 = opera2.length;
			// Extract the string into month, date and year
			if (lopera1 > 1) {
				var pdate = dob.value.split('/');
			} else if (lopera2 > 1) {
				var pdate = dob.value.split('-');
			}
			var dd = parseInt(pdate[0]);
			var mm = parseInt(pdate[1]);
			var yy = parseInt(pdate[2]);
			// Create list of days of a month [assume there is no leap year by default]
			var ListofDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
			if (mm == 1 || mm > 2) {
				if (dd > ListofDays[mm - 1]) {
					alert('Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY');
					return false;
				}
			}
			if (mm == 2) {
				var lyear = false;
				if ((!(yy % 4) && yy % 100) || !(yy % 400)) {
					lyear = true;
				}
				if ((lyear == false) && (dd >= 29)) {
					alert('Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY');
					return false;
				}
				if ((lyear == true) && (dd > 29)) {
					alert('Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY');
					return false;
				}
            }
            return true;
		} else {
			alert("Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY");
			dob.focus();
			return false;
		}
	}

	function ValidateEmail(email) {
		var mailformat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		if (email.value == "") {
			alert("Email cannot be empty")
		} else if (email.value.match(mailformat)) {
			return true;
		} else {
			alert("You have entered an invalid email address!");
			email.focus();
			return false;
		}
	}

	function password_validation(password) {
		var str = password.value;
		if (password.value == "") {
			alert("Password cannot be empty")
		} else if (str.match(/[a-z]/g) && str.match(
				/[A-Z]/g) && str.match(
				/[0-9]/g) && str.match(
				/[^a-zA-Z\d]/g) && str.length >= 8) {
			return true;
		} else {
			alert("Password must have at least 1 uppercase character,1 lowercase character, 1 digit, 1 special character.and minimum 8 characters.")
			return false;
		}
	}


	function firstname_validation(fname) {
		var letters = /^[A-Za-z]+$/;
		if (fname.value == "") {
			alert("First name cannot be empty")
			fname.focus();
		} else if (fname.value.match(letters)) {
			return true;
		} else {
			alert("Firstname must have alphabet characters only")
			fname.focus();
			return false;
		}
	}

	function lastname_validation(lname) {
		var letters = /^[A-Za-z]+$/;
		if (lname.value == "") {
			alert("Last name cannot be empty")
			lname.focus();
		} else if (lname.value.match(letters)) {
			return true;
		} else {
			alert("Lastname must have alphabet characters only")
			lname.focus();
			return false;
		}
	}

	function Validate_phone(contact) {
        var phoneno = /^\d{10}$/;
		if (contact.value == "") {
			alert("Phone number cannot be empty")
			contact.focus();
		} else if (contact.value.match(phoneno)) {
			return true;
		} else {
			alert("Please enter a valid phone number")
			contact.focus();
			return false;
		}

	}


	function add1_validation(add1) {
		var address1 = /^[0-9a-zA-Z]+$/;
		if (add1.value == "") {
			alert("Address cannot be empty")
			add1.focus();
		} else if (add1.value.match(address1)) {
			alert("aa");
			return true;
		} else {
			alert("User address must have alphanumeric characters only")
			add1.focus();
			return false;
		}
	}

	/*
	function countryselect(ucountry)
	{
	if(ucountry.value == "Default")
	{
	alert('Select your country from the list');
	ucountry.focus();
	return false;
	}
	else
	{
	return true;
	}
	}
	function allnumeric(uzip)
	{ 
	var numbers = /^[0-9]+$/;
	if(uzip.value.match(numbers))
	{
	return true;
	}
	else
	{
	alert('ZIP code must have numeric characters only');
	uzip.focus();
	return false;
	}
	}
	function ValidateEmail(uemail)
	{
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(uemail.value.match(mailformat))
	{
	return true;
	}
	else
	{
	alert("You have entered an invalid email address!");
	uemail.focus();
	return false;
	}
	} function validsex(umsex,ufsex)
	{
	x=0;

	if(umsex.checked) 
	{
	x++;
	} if(ufsex.checked)
	{
	x++; 
	}
	if(x==0)
	{
	alert('Select Male/Female');
	umsex.focus();
	return false;
	}

	else

	{
	alert('Form Succesfully Submitted');
	window.location.reload()
	return true;
	}
	}
	*/
}