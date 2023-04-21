from flask import request, jsonify
from api_response import *
import requests, json, re


with open('/Users/liumengyuan/CS_5001/final_project/Flask/keys.json', 'r') as\
file:
    keys = json.load(file)


def select_movie(title):
    """
    Retrieves multiple possible titles about movies matching a given input
    vague title from IMDB.

    Args:
        title (str): The vague title of the movie to search for.

    Returns:
        dict: A dictionary containing information about the movies matching
        the given title. Each key in the dictionary represents a different
        movie and the value is a list of strings containing the title,
        image URL, release year, and IMDB ID of the movie.

        str: If a connection cannot be established with the IMDB API, returns
        a string indicating that the connection failed.
    """
    key = keys['imdb_key']
    response = imdb(title, key)
    if response != '':
        results = json.loads(response.text)
        formated = json.dumps(results, indent=4)
        movies_dic = json.loads(formated)
        raw_data = movies_dic["d"]
        info_dic = {}
        for index in range(len(raw_data)):
            try:
                movie_id = str(raw_data[index]["id"])
                title = str(raw_data[index]["l"])
                image_url = str(raw_data[index]["i"]["imageUrl"])
                release_year = str(raw_data[index]["y"])
                dic_index = len(info_dic)
                info_dic[dic_index] = [title, image_url, release_year,  movie_id]
            except:
                pass
        return info_dic
    else:
        return "Failed to connect to the IMDB API."


def get_movie_details(movie_id):
    """
    Retrieves detailed information about a movie from the OTT database.

    Args:
        movie_id (str): The IMDB ID of the movie to search for.

    Returns:
        list: A list containing detailed information about the movie, including
        genre, runtime, IMDB rating, synopsis, language, and availability on
        streaming services.

        str: If a connection cannot be established with the OTT database,
        returns a string indicating that the connection failed.
    """
    key = keys['ott_key']
    response = ott(movie_id, key)
    if response != '':
        results = json.loads(response.text)
        formated = json.dumps(results, indent=4)
        movies_dic = json.loads(formated)
        info_ls = []
        title = movies_dic['title']
        movie_id = movies_dic['imdbid']
        genre = movies_dic['genre']
        run_time = movies_dic['runtime']
        rating = movies_dic['imdbrating']
        synopsis = movies_dic['synopsis']
        language = movies_dic['language']
        availability = movies_dic['streamingAvailability']['country']['US']
        info_ls.extend([genre, run_time, rating, synopsis,
                        language, availability, movie_id, title])
        return info_ls
    else:
        return "Failed to get movies information from OTT"


def get_omdb_url(movie_id):
    """
    Retrieves the poster URL of a movie from the OMDB API.

    Args:
        movie_id (str): The IMDB ID of the movie to search for.

    Returns:
        tuple: A tuple containing the title and poster URL of the movie.

        str: If a connection cannot be established with the OMDB API, returns a
        string indicating that the connection failed.
    """
    key = keys['omdb_key']
    response = omdb(movie_id, key)
    if response != '':
        response = response.json()
        movie_title = response['Title']
        poster_url = response['Poster']
        if movie_title != None and poster_url != None:
            return movie_title, poster_url
    else:
        return "Failed to get posters' url of movies from OMDB"


def chatgpt_recommendation(title, rating, comment):
    """
    Retrieves movie recommendations based on user input from the ChatGPT API.

    Args:
        title (str): The title of the movie for which to receive
        recommendations.
        rating (int): The rating (out of 10) the user gives to the current
        movie.
        comment (str): The user's comment about the movie.

    Returns:
        dict: A dictionary containing information about the recommended movies.
        Each key in the dictionary represents a different movie and the value
        is a list of strings containing the title and poster URL of the movie.

        str: If a connection cannot be established with the ChatGPT API,
        returns a string indicating that the connection failed.
    """
    key = keys['chatgpt_key']
    response = chatgpt(title, rating, comment, key)
    if response != '':
        url_dic = {}
        results = json.loads(response.text)
        formated = json.dumps(results, indent=4)
        response_info = json.loads(formated)
        raw_response = response_info["choices"][0]["message"]["content"]
        pattern = r"tt\d+"
        id_ls = re.findall(pattern, raw_response)
        for element in id_ls:
            element = element.strip()
            title, poster = get_omdb_url(element)
            try:
                url_dic[element] = [title, poster]
            except:
                pass
        return url_dic
    else:
        return "Failed to get recommendations from ChatGPT"
