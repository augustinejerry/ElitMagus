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
	var message = "";
	if (ValidateEmail(email)) {
		if (password_validation(password)) {
			if (firstname_validation(fname)) {
				if (lastname_validation(lname)) {
					if (Validate_dob(dob)) {
						if (Validate_phone(contact)) {
							if (add1_validation(add1)) {
								if (add2_validation(add2)) {
									if (city_validation(city)) {
										if (province_validation(province)) {
											if(zip_validation(zip)) {
												return true;
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	if(message!==""){
		var innerhtml = "<div class=\"alert alert-danger\" role=\"alert\">" + message + "</div>";
		$("#alertbox").html(innerhtml);
	}
	return false;
	function Validate_dob(dob) {
		var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
		// Match the date format through regular expression
		if (dob.value == "") {
			message = "Date of birth cannot be empty";
			return false;
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
					message = "Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY";
					return false;
				}
			}
			if (mm == 2) {
				var lyear = false;
				if ((!(yy % 4) && yy % 100) || !(yy % 400)) {
					lyear = true;
				}
				if ((lyear == false) && (dd >= 29)) {
					message = "Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY";
					return false;
				}
				if ((lyear == true) && (dd > 29)) {
					message = "Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY";
					return false;
				}
            }
            return true;
		} else {
			message = "Invalid date format! Please try DD/MM/YYYY or DD-MM-YYYY";
			dob.focus();
			return false;
		}
	}

	function ValidateEmail(email) {
		var mailformat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		if (email.value == "") {
			message = "Email cannot be empty";
			email.focus();
			return false;
		} else if (email.value.match(mailformat)) {
			return true;
		} else {
			message = "You have entered an invalid email address!";
			email.focus();
			return false;
		}
	}

	function password_validation(password) {
		var str = password.value;
		if (password.value == "") {
			message = "Password cannot be empty";
			password.focus();
			return false;
		} else if (str.match(/[a-z]/g) && str.match(
				/[A-Z]/g) && str.match(
				/[0-9]/g) && str.match(
				/[^a-zA-Z\d]/g) && str.length >= 8) {
			return true;
		} else {
			message = "Password must have at least 1 uppercase character,1 lowercase character, 1 digit, 1 special character.and minimum 8 characters.";
			password.focus();
			return false;
		}
	}


	function firstname_validation(fname) {
		var letters = /^[A-Za-z]+$/;
		if (fname.value == "") {
			message = "First name cannot be empty";
			fname.focus();
			return false;
		} else if (fname.value.match(letters)) {
			return true;
		} else {
			message = "Firstname must have alphabet characters only";
			fname.focus();
			return false;
		}
	}

	function lastname_validation(lname) {
		var letters = /^[A-Za-z]+$/;
		if (lname.value == "") {
			message = "Last name cannot be empty";
			lname.focus();
			return false;
		} else if (lname.value.match(letters)) {
			return true;
		} else {
			message = "Lastname must have alphabet characters only";
			lname.focus();
			return false;
		}
	}

	function Validate_phone(contact) {
        var phoneno = /^\d{10}$/;
		if (contact.value == "") {
			message = "Phone number cannot be empty";
			contact.focus();
		} else if (contact.value.match(phoneno)) {
			return true;
		} else {
			message = "Please enter a valid phone number";
			contact.focus();
			return false;
		}

	}


	function add1_validation(add1) {
		var address1 = /^[0-9a-zA-Z_]+$/;
		if (add1.value == "") {
			message = "Address cannot be empty";
			add1.focus();
			return false;
		} else if (add1.value.match(address1)) {
			return true;
		} else {
			message = "User address must have alphanumeric characters only";
			add1.focus();
			return false;
		}
	}

	function add2_validation(add2) {
		var address2 = /^[a-zA-Z_]+$/;
		if (add2.value == "") {
			return true;
		} else if (add2.value.match(address2)) {
			return true;
		} else {
			message = "User address must have alphabets only";
			add2.focus();
			return false;
		}
	}
	function city_validation(city) {
		var city_format = /^[a-zA-Z_]+$/;
		if (city.value == "") {
			message = "City cannot be empty";
			city.focus();
			return false;
		} else if (city.value.match(city_format)) {
			return true;
		} else {
			message = "City must have alphabets only";
			city.focus();
			return false;
		}
	}
	function province_validation(province) {
		var province_format = /^[a-zA-Z_]+$/;
		if (province.value == "") {
			message = "Province cannot be empty";
			province.focus();
			return false;
		} else if (province.value.match(province_format)) {
			return true;
		} else {
			message = "Province must have alphabets only";
			province.focus();
			return false;
		}
	}
	function zip_validation(zip) {
		var zip_format = /^[a-zA-Z0-9]{6}$/;
		if (zip.value == "") {
			message = "Zip cannot be empty";
			zip.focus();
			return false;
		} else if (zip.value.match(zip_format)) {
			return true;
		} else {
			message = "Zip must be an alphanumeric of size 6";
			zip.focus();
			return false;
		}
	}
}