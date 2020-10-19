$(document).ready(function() {                        
                $('#login').click(function(event) {  
                    var username=$('#username').val();
					var password=$('#password').val();
                    $.ajax( 
                        { 
                            type:"POST", 
                            url: "validatelogin", 
                            data:{username:username, password:password}, 
                            dataType: "text",
                            success: function(data) { 
                                var obj = JSON.parse(data);
                                alert("Hello! I am an alert box!!"+ obj.valid);
                                // alert("Hello! I am an alert box!!" + obj.count);
                                if (obj.valid == 1){   
                                    window.location.replace('homepage');
                                }
                                else{   
                                    $('#error').text(data);
                                }                          
				            },
                            error: function(data) {
                                alert("error"+data);
                            }
                        });
                });
            });