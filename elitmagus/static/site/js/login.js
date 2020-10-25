$(document).ready(function() {                        
                $('#login').click(function(event) {  
                    var username=$('#username').val();
                    var password=$('#password').val();
                    var csrfToken=$('#token').val();
                    $.ajax( 
                        { 
                            type:"POST", 
                            url: "validatelogin", 
                            headers: {'X-CSRFToken': csrfToken},
                            data: {username:username, password:password},
                            dataType: "text",
                            success: function(data) { 
                                var obj = JSON.parse(data);
                                if (obj.valid == 1){   
                                    window.location.replace('homepage');
                                }
                                else{   
                                    $('#error').text(obj.message);
                                }                          
				            },
                            error: function(data) {
                                alert("error"+data);
                            }
                        });
                });
            });