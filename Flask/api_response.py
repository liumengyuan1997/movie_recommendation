from flask import request, jsonify
import requests


def imdb(title: str, key: str):
    """
    Retrieves movie information from IMDb using the RapidAPI auto-complete
    endpoint.

    Parameters:
    title (str): The title of the movie to search for.
    key (str): The RapidAPI key for accessing the IMDb API.

    Returns:
    A response object containing information about the movie from IMDb.
    If the request fails, returns a JSON object with an error message and HTTP
    status code 500.
    """
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q": title}
    headers = {
        	"X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response
    else:
        return jsonify({'error': 'Failed to get movies from IMDb'}), 500


def ott(movie_id: str, key: str):
    """
    Retrieves information about a movie from OTT using the RapidAPI
    gettitleDetails endpoint.

    Parameters:
    movie_id (str): The IMDb ID of the movie to search for.
    key (str): The RapidAPI key for accessing the OTT API.

    Returns:
    A response object containing information about the movie from OTT.
    If the request fails, returns a JSON object with an error message and HTTP
    status code 500.
    """
    url = "https://ott-details.p.rapidapi.com/gettitleDetails"
    querystring = {"imdbid": movie_id}
    headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": "ott-details.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response
    else:
        return jsonify({'error': 'Failed to get information from OTT'}), 500


def omdb(movie_id, key):
    """
    Retrieves the posters' url of a movie from OMDB using the OMDB API.

    Parameters:
    movie_id (str): The IMDb ID of the movie to search for.
    key (str): The OMDB API key for accessing the OMDB API.

    Returns:
    A response object containing the posters' url of the movie from OMDB.
    If the request fails, returns a JSON object with an error message and HTTP
    status code 500.
    """
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        return jsonify({'error': "Failed to get posters' url of movies\
        from OMDB"}), 500


def chatgpt(title: str, rating: str, comment: str, key: str):
    """
    Requests movie recommendations from ChatGPT using the RapidAPI completions
    endpoint.

    Parameters:
    title (str): The title of the movie to use in the request.
    rating (str): The user's rating to the movie to use in the request.
    comment (str): The user's comment to the movie to use in the request.
    key (str): The RapidAPI key for accessing the ChatGPT API.

    Returns:
    A response object containing movie recommendations from ChatGPT.
    If the request fails, returns a JSON object with an error message and HTTP
    status code 500.
    """
    url = "https://openai80.p.rapidapi.com/chat/completions"
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
    {
    "role": "user",
    "content": f"I watched a movie named '{title}'. And my rating for this\
    movie is {rating} out of 10. And my reviews for the movie is: {comment}.\
    Can you recommend some movies based on my rating and review? Only give me\
    the imdb id of those movies in the format of a list. NO OTHER THINGS!\
    ONLY A LIST OF ID! And use ',' to seperate ids."
    }
    ]
    }
    headers = {
    "content-type": "application/json",
    'X-RapidAPI-Key': key,
    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return jsonify({'error': "Failed to get recommendations from\
        ChatGPT"}), 500
