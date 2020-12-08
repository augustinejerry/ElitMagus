# Import Pandas
import pandas as pd
from .utilities import *
from django.http import JsonResponse
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
# Import Numpy
import numpy as np
# Parse the stringified features into their corresponding python objects
from ast import literal_eval
# Import CountVectorizer and create the count matrix
from sklearn.feature_extraction.text import CountVectorizer
# Compute the Cosine Similarity matrix based on the count_matrix
from sklearn.metrics.pairwise import cosine_similarity



def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 3:
            names = names[:3]
        return names

    #Return empty list in case of missing/malformed data
    return []

# Function to convert all strings to lower case and strip names of spaces
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])

# Function that computes the weighted rating of each movie
def weighted_rating(x, m, C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

#function to suggest top 10 movies
def simpleRecommender(request):
    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        movie_json = ""

    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 
        
        # Collection Name 
        coll = db["poster"] 

        #fetch user details
        result = coll.find({})
        
        #create dataframe from result set
        metadata =  pd.DataFrame(list(result))

        #changing the datatype
        metadata['vote_average'] = metadata['vote_average'].astype(float)
        metadata['vote_count'] = metadata['vote_count'].astype(float)

        # Calculate mean of vote average column
        C = metadata['vote_average'].mean()

        # Calculate the minimum number of votes required to be in the chart, m
        m = metadata['vote_count'].quantile(0.90)

        # Filter out all qualified movies into a new DataFrame
        q_movies = metadata.copy().loc[metadata['vote_count'] >= m]

        # Define a new feature 'score' and calculate its value with `weighted_rating()`
        q_movies['score'] = q_movies.apply(lambda x : weighted_rating(x,m=m,C=C), axis=1)

        #Sort movies based on score calculated above
        q_movies = q_movies.sort_values('score', ascending=False)

        #Print the top 15 movies
        movies = q_movies[['id', 'title', 'tagline', 'poster_path']].head(10) 
        movies = movies.to_json(orient = 'records')

    
    data = {    
        'valid': 1,
        'message': message,
        'movies': movies
    }
    
    return JsonResponse(data)

#function to calculate cosine similarity of movie overview
def cosine_sim_overview(request):
    #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    metadata['overview'] = metadata['overview'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(metadata['overview'])

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations_overview(request):
    title = request.POST.get('title', None)
    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        movie_json = ""
    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 
        
        # Collection Name 
        coll = db["poster"] 

        #fetch user details
        result = coll.find({})
        
        #create dataframe from result set
        metadata =  pd.DataFrame(list(result))

        #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')

        #Replace NaN with an empty string
        metadata['overview'] = metadata['overview'].fillna('')

        #Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(metadata['overview'])

        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        #Construct a reverse map of indices and movie titles
        indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

        # Get the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        movies = metadata[['id', 'title', 'tagline', 'poster_path']].iloc[movie_indices]
        movies = movies.to_json(orient = 'records')

    data = {    
        'valid': valid,
        'message': message,
        'movies': movies
    }
    
    return JsonResponse(data)

def get_recommendations_cast(request):
    title = request.POST.get('title', None)
    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        movie_json = ""
    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 
        
        # Collection Name 
        coll = db["poster"] 
        #fetch user details
        result = coll.find({})        
        #create dataframe from result set
        metadata =  pd.DataFrame(list(result))

        # Collection Name 
        coll = db["credits"] 
        #fetch user details
        result = coll.find({})        
        #create dataframe from result set
        credits =  pd.DataFrame(list(result))

        # Collection Name 
        coll = db["keywords"] 
        #fetch user details
        result = coll.find({})        
        #create dataframe from result set
        keywords =  pd.DataFrame(list(result))

        # Remove rows with bad IDs.
        metadata = metadata.drop(metadata[~metadata['id'].apply(lambda x: str(x).isnumeric())].index)

        # Convert IDs to int. Required for merging
        keywords['id'] = keywords['id'].astype('int')
        credits['id'] = credits['id'].astype('int')
        metadata['id'] = metadata['id'].astype('int')

        # Merge keywords and credits into your main metadata dataframe
        metadata = metadata.merge(credits, on='id')
        metadata = metadata.merge(keywords, on='id')

        features = ['cast', 'crew', 'keywords', 'genres']
        for feature in features:
            metadata[feature] = metadata[feature].apply(literal_eval)

        # Define new director, cast, genres and keywords features that are in a suitable form.
        metadata['director'] = metadata['crew'].apply(get_director)

        features = ['cast', 'keywords', 'genres']
        for feature in features:
            metadata[feature] = metadata[feature].apply(get_list)

        # Apply clean_data function to your features.
        features = ['cast', 'keywords', 'director', 'genres']

        for feature in features:
            metadata[feature] = metadata[feature].apply(clean_data)

        # Create a new soup feature
        metadata['soup'] = metadata.apply(create_soup, axis=1)

        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(metadata['soup'])

        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        # Reset index of your main DataFrame and construct reverse mapping as before
        metadata = metadata.reset_index()
        indices = pd.Series(metadata.index, index=metadata['title'])
        #Construct a reverse map of indices and movie titles
        indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

        # Get the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        movies = metadata[['id', 'title', 'tagline', 'poster_path']].iloc[movie_indices]
        movies = movies.to_json(orient = 'records')

    data = {    
        'valid': valid,
        'message': message,
        'movies': movies
    }
    
    return JsonResponse(data)

#function to find user based suggestion
def get_recommendations_user(request):
    userId = request.session['userid']
    print(userId)
    connection = connectMongo()

    if connection == -1:
        valid = -1
        message = "Error in establishing connection with the database"
        movie_json = ""
    else:
        valid = 1
        message = "success"

        # Database Name 
        db = connection["elitmagus"] 

        # Collection Name 
        coll = db["poster"] 
        #fetch user details
        result = coll.find({})
        #create dataframe from result set
        metadata =  pd.DataFrame(list(result))
        
        # Collection Name 
        coll = db["ratings_small"] 
        #fetch user details
        result = coll.find({})        
        #create dataframe from result set
        ratings =  pd.DataFrame(list(result))

        #change the datatype of movieId
        ratings['movieId'] = ratings['movieId'].astype('string')

        #group the result by userId to get the list of movies watched by each user
        watchedList = ratings.groupby('userId')['movieId'].apply(lambda x: ' '.join(x)).reset_index()

        ind = pd.Series(watchedList.index, index=watchedList['userId'])
        #Construct a reverse map of indices and movie titles
        ind = pd.Series(watchedList.index, index=watchedList['userId']).drop_duplicates()

        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(watchedList['movieId'])

        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        idx = ind[userId]
        
        # Get the pairwsie similarity scores of all users with that user
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the users based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar users
        sim_scores = sim_scores[1:11]

        # Get the user indices
        user_indices = [i[0] for i in sim_scores]

        currentUser = userId

        #watched list of the similar users
        probableMovies = watchedList.iloc[user_indices]

        idx = ind[currentUser]
        #watched list of current user
        userWatchedlist = watchedList['movieId'].iloc[idx]

        #convert string to array
        probableMovies['movieId'] = probableMovies['movieId'].apply(lambda x: np.fromstring(x, dtype=int, sep=' '))

        #find the union of similar user's movies
        unionList = np.empty([1, 1], dtype=int)
        for index, row in probableMovies.iterrows():
            unionList = np.union1d(unionList, row['movieId'])

        #make the array from string
        userWatchedlist = np.fromstring(userWatchedlist, dtype=int, sep=' ')

        #finding the movies which are not seen by the user from the list
        suggestions = np.setdiff1d(unionList, userWatchedlist)

        suggestedMovies = np.apply_along_axis(lambda y: [str(i) for i in y], 0, suggestions[0:10]).tolist()

        movies = metadata[['id', 'title', 'tagline', 'poster_path']].loc[metadata.id.isin(suggestedMovies)]
        movies = movies.to_json(orient = 'records')

    data = {    
        'valid': valid,
        'message': message,
        'movies': movies
    }
    
    return JsonResponse(data)