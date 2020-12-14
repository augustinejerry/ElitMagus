function genres(gen){
    var str = gen.replace(/'/g,'"');
    var arr = JSON.parse(str);
    var disp = "";
    for (var i = 0; i < arr.length; i++){
        var obj = arr[i];
        var disp = disp + "<span class=\"border border-primary\">" + obj['name'] + "</span>";
    }
    console.log(disp);
    console.log(str);
    alert(gen);
    return disp;
    // $("#genres").html(disp);
} 
$(document).ready(function() {  
    var csrfToken=$('#token').val();
    var userId=$('#userId').val();
    var movieId=$('#movieId').val();
    var title=$('#title').val();
    var path=$('#path').val();
    var gen=$('#gen').val();
    
    //displaying genres
    var str = gen.replace(/'/g,'"');
    var arr = JSON.parse(str);
    var disp = "";
    for (var i = 0; i < arr.length; i++){
        var obj = arr[i];
        var disp = disp + "<button id = \"genrebt\" type=\"button\" class=\"genrebtn\" disabled=\"disabled\"><b>" + obj['name'] + "</b></button>";
    }
    $("#genres").html(disp);

    $.ajax( 
        { 
            type:"POST", 
            url: "simpleRecommender", 
            headers: {'X-CSRFToken': csrfToken},
            data: {userId:userId,movieId:movieId,title:title},
            dataType: "text",
            success: function(data) { 
                var obj = JSON.parse(data);
                if (obj.valid == 1){  
                    var movies = JSON.parse(obj.movies); 
                    var row = "<ul class=\"list-group list-group-horizontal-lg\">";
                    for (var i=0; i<movies.length; i++) {
                        // row = row + "<li class=\"list-group-item\">" + movies[i].title + "</li>";
                        row = row + "<div class=\"card\">"
                            + "<div id=\""
                            + movies[i].id +"$" + movies[i].title
                            +"\" class=\"movieTag\">"
                            + "<img class=\"card-img-top\" src=\"http://image.tmdb.org/t/p/w500/" 
                            + movies[i].poster_path 
                            +"\" onerror=this.src=\"/static/site/images/noposter.jpg\">"
                            // + "<div class=\"card-body\">"
                            + "<p class=\"card-text\">"
                            + movies[i].title
                            + "</p>"
                            // + "</div>"
                            + "</div>"
                            + "</div>";
                    }
                    row = row + "</ul>";
                    $("#simple").html(row);
                    $.ajax( 
                        { 
                            type:"POST", 
                            url: "overviewRecommender", 
                            headers: {'X-CSRFToken': csrfToken},
                            data: {userId:userId,movieId:movieId,title:title},
                            dataType: "text",
                            success: function(data) { 
                                var obj = JSON.parse(data);
                                if (obj.valid == 1){  
                                    var movies = JSON.parse(obj.movies); 
                                    var row = "<ul class=\"list-group list-group-horizontal-lg\">"
                                    for (var i=0; i<movies.length; i++) {
                                        // row = row + "<li class=\"list-group-item\">" + movies[i].title + "</li>";
                                        row = row + "<div class=\"card\">"
                                            + "<div id=\""
                                            + movies[i].id+"$" + movies[i].title
                                            +"\" class=\"movieTag\">"
                                            + "<img class=\"card-img-top\" src=\"http://image.tmdb.org/t/p/w500/" 
                                            + movies[i].poster_path 
                                            +"\" onerror=this.src=\"/static/site/images/noposter.jpg\">"
                                            // + "<div class=\"card-body\">"
                                            + "<p class=\"card-text\">"
                                            + movies[i].title
                                            + "</p>"
                                            // + "</div>"
                                            + "</div>"
                                            + "</div>";
                                    }
                                    row = row + "</ul>";
                                    $("#overview").html(row);
                                    $.ajax( 
                                        { 
                                            type:"POST", 
                                            url: "castRecommender", 
                                            headers: {'X-CSRFToken': csrfToken},
                                            data: {userId:userId,movieId:movieId,title:title},
                                            dataType: "text",
                                            success: function(data) { 
                                                var obj = JSON.parse(data);
                                                if (obj.valid == 1){  
                                                    var movies = JSON.parse(obj.movies); 
                                                    var row = "<ul class=\"list-group list-group-horizontal-lg\">"
                                                    for (var i=0; i<movies.length; i++) {
                                                        // row = row + "<li class=\"list-group-item\">" + movies[i].title + "</li>";
                                                        row = row + "<div class=\"card\">"
                                                            + "<div id=\""
                                                            + movies[i].id+"$" + movies[i].title
                                                            +"\" class=\"movieTag\">"
                                                            + "<img class=\"card-img-top\" src=\"http://image.tmdb.org/t/p/w500/" 
                                                            + movies[i].poster_path 
                                                            +"\" onerror=this.src=\"/static/site/images/noposter.jpg\">"
                                                            // + "<div class=\"card-body\">"
                                                            + "<p class=\"card-text\">"
                                                            + movies[i].title
                                                            + "</p>"
                                                            // + "</div>"
                                                            + "</div>"
                                                            + "</div>";
                                                    }
                                                    row = row + "</ul>";
                                                    $("#cast").html(row);
                                                    $.ajax( 
                                                        { 
                                                            type:"POST", 
                                                            url: "userRecommender", 
                                                            headers: {'X-CSRFToken': csrfToken},
                                                            data: {userId:userId,movieId:movieId,title:title},
                                                            dataType: "text",
                                                            success: function(data) { 
                                                                var obj = JSON.parse(data);
                                                                if (obj.valid == 1){  
                                                                    var movies = JSON.parse(obj.movies); 
                                                                    var row = "<ul class=\"list-group list-group-horizontal-lg\">"
                                                                    for (var i=0; i<movies.length; i++) {
                                                                        // row = row + "<li class=\"list-group-item\">" + movies[i].title + "</li>";
                                                                        row = row + "<div class=\"card\">"
                                                                            + "<div id=\""
                                                                            + movies[i].id +"$" + movies[i].title
                                                                            +"\" class=\"movieTag\">"
                                                                            + "<img class=\"card-img-top\" src=\"http://image.tmdb.org/t/p/w500/" 
                                                                            + movies[i].poster_path 
                                                                            +"\" onerror=this.src=\"/static/site/images/noposter.jpg\">"
                                                                            // + "<div class=\"card-body\">"
                                                                            + "<p class=\"card-text\">"
                                                                            + movies[i].title
                                                                            + "</p>"
                                                                            // + "</div>"
                                                                            + "</div>"
                                                                            + "</div>";
                                                                    }
                                                                    row = row + "</ul>";
                                                                    $("#user").html(row);
                                                                    
                                                                }
                                                                else{   
                                                                    $('#error').text(obj.message);
                                                                }                          
                                                            },
                                                            error: function(data) {
                                                                alert("error"+data);
                                                            }
                                                        });
                                                }
                                                else{   
                                                    $('#error').text(obj.message);
                                                }                          
                                            },
                                            error: function(data) {
                                                alert("error"+data);
                                            }
                                        });
                                }
                                else{   
                                    $('#error').text(obj.message);
                                }                          
                            },
                            error: function(data) {
                                alert("error"+data);
                            }
                        });
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
$(document).on("click" , ".movieTag" , function() 
{
        var movie=this.id;
        var arr = movie.split('$');
        var movieId = arr[0];
        var title = arr[1];
        // var userId=request.session.userid;
        var csrfToken=$('#token').val();
        $.ajax( 
            { 
                type:"POST", 
                url: "setmoviedesc", 
                headers: {'X-CSRFToken': csrfToken},
                data: {movieId:movieId, title:title},
                dataType: "text",
                success: function(data){
                    window.location.replace('moviedesc');
                },
                error: function(data) {
                    alert("error"+data);
                }
            });
        
});