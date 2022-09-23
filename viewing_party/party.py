# ------------- WAVE 1 --------------------

from enum import unique
from turtle import title
from tests.test_constants import clean_wave_2_data


def create_movie(title, genre, rating):
    movie_info = {}
    keys = ["title", "genre", "rating"]
    values = [title, genre, rating]
    for i in range(len(keys)):
        if values[i] == None:
            return None
        movie_info[keys[i]]=values[i]     
    return movie_info

def add_to_watched(user_data, movie):
    for key in user_data: 
        user_data[key]=[movie]
    return user_data

def add_to_watchlist(user_data, movie):
    for key in user_data: 
        user_data[key]=[movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    ratings_sum = 0

    if watched_list == []:
            return 0.0

    for movie in watched_list:
        ratings_sum += movie["rating"]
        average = ratings_sum / len(watched_list)
    return average

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    genre_list = []

    if watched_list == []:
        return None
    
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    top_genre = max(set(genre_list), key=genre_list.count)
    return top_genre

        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friend_movies_list = []

    #creating a dictionary of friend's watched movies and putting into a list
    for watchlist in user_data["friends"]:
        for watched in watchlist.values():
            for movies_dict in watched:
                friend_movies_list.append(movies_dict)
    
    #comparing user list and friends list for unique titles
    for movies in user_data["watched"]:
        if movies not in friend_movies_list:
            unique_movies.append(movies)
    
    return unique_movies


def get_friends_unique_watched(user_data):
    unique_movies = []
    user_movies_list = []
    return_list = []
    
    #creating a dictionary of user's watched and putting into a list
    for movies in user_data["watched"]:
        user_movies_list.append(movies)

    #comparing friends list and user list for unique titles
    for watchlist in user_data["friends"]:
        for watched in watchlist.values():
            for movies_dict in watched:
                if movies_dict not in user_movies_list:
                    unique_movies.append(movies_dict)
    
    #checking unique list for any duplicates 
    for movie in unique_movies:
        if movie not in return_list:
            return_list.append(movie)
    
    print(return_list)
    
    return return_list         
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

