$(document).ready(function() {                        
                    $('.movieTag').click(function(event) { 
                        var movie=this.id;
                        var arr = movie.split('#');
                        var movieId = arr[0];
                        var title = arr[1];
                        // var userId=request.session.userid;
                        var csrfToken=$('#token').val();
                        $.ajax( 
                            { 
                                type:"POST", 
                                url: "setmoviedesc", 
                                headers: {'X-CSRFToken': csrfToken},
                                data: {movieId:movieId,title:title},
                                dataType: "text",
                                success: function(data){
                                    window.location.replace('moviedesc');
                                },
                                error: function(data) {
                                    alert("error"+data);
                                }
                            });
                        
                    });
                });
