"""
A Flask application for a movie search, rating, and recommendation system

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import urllib.parse
import json
from response_handle import *
from api_response import *
from utils import *

app = Flask(__name__)

with open('/Users/liumengyuan/CS_5001/final_project/Flask/keys.json', 'r') as\
          file:
    keys = json.load(file)

app.secret_key = keys["app_secret_key"]


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Renders the main.html template if a GET request is received, or redirects
    to the '/get_movies' route if a POST request is received.

    Parameters:
    None

    Returns:
    If a GET request is received:
        Returns the rendered 'main.html' template.

    If a POST request is received:
        Redirects the user to the 'get_movies' route with the 'title' parameter
        specified in the request form.
    """
    if request.method == "POST":
        title = str(request.form.get('title'))
        if isinstance(imdb(title, keys['imdb_key']), tuple):
            flash('Invalid movie name! Please try again.')
            return render_template("main.html")
        return redirect(url_for("get_movies", title=title))
    else:
        return render_template("main.html")


@app.route('/<title>', methods=['POST', 'GET'])
def get_movies(title):
    """
    Renders the select_movie.html template, displaying a list of movies with
    images and titles, based on the user's search query specified in the
    'title' parameter. If a POST request is received, the user can select
    a movie to get more details or to receive recommendations based on their
    further input.

    Parameters:
    title (str): The movie title to be searched for.

    Returns:
    If a GET request is received:
        Renders the 'select_movie.html' template with the 'info_dic' and
        'image_ls' variables.

    If a POST request is received:
        Based on the user's input, redirects to the 'get_rating' or
        'get_recommendation' route with the appropriate parameters.
    """
    info_dic = select_movie(title, imdb)
    if request.method == "POST":
        title = str(request.form.get('title'))
        year = str(request.form.get('year'))
        choice = request.form['choice']
        for key, value in info_dic.items():
            if title == value[0] and year == value[2]:
                movie_url = value[1]
                movie_id = value[3]
                if choice == 'option1':
                    return redirect(url_for("get_rating", movie_id=movie_id,
                                    movie_url=movie_url))
                elif choice == 'option2':
                    return redirect(url_for("get_recommendation",
                                    title=title))
    else:
        image_ls = []
        for key, value in info_dic.items():
            image_ls.append(value[1])

        return render_template("select_movie.html", info_dic=info_dic,
                               image_ls=image_ls)


@app.route('/id/<movie_id>', methods=['POST', 'GET'])
def get_rating(movie_id):
    """
    Renders the movie_rating.html template, displaying movie details such as
    title, image, release year, genre, synopsis, and ratings, based on the
    'movie_id' parameter passed to the URL.

    Parameters:
    movie_id (str): The movie ID of the movie to display details for.

    Returns:
    Returns the rendered 'movie_rating.html' template with the 'movie_url'
    and 'info_ls' variables.
    """
    movie_url = request.args.get('movie_url')
    info_ls = get_movie_details(movie_id, ott)
    return render_template("movie_rating.html", movie_url=movie_url,
                           info_ls=info_ls)


@app.route('/movie_title/movie_recommendation', methods=['POST', 'GET'])
def get_recommendation():
    """
    Renders the recommendation.html template, allowing the user to rate a
    movie and write a review to receive recommendations for similar movies.

    Parameters:
    None

    Returns:
    If a GET request is received:
        Renders the 'get_review.html' template with the 'title' variable.
    If a POST request is received:
        Returns the rendered 'recommendation.html' template with the
        'distinct_dic' variable containing a dictionary of movie
        recommendations.
    """
    title = request.args.get('title')
    if request.method == "POST":
        rating = str(request.form.get('rating'))
        if not check_number(rating):
            flash('Invalid movie rating! Please enter a number between 0-10.')
            return render_template("get_review.html", title=title)
        valid_rating = convert_rating(rating, 0, 10)
        comment = str(request.form.get('movie_review'))
        url_dic = chatgpt_recommendation(title, valid_rating, comment, chatgpt)
        distinct_dic = {}
        for key, value in url_dic.items():
            if value[0] != title:
                distinct_dic[key] = value
        return render_template("recommendation.html",
                               distinct_dic=distinct_dic)
    else:
        return render_template("get_review.html", title=title)


@app.route('/movie_title/movie_recommendation/detail', methods=['POST', 'GET'])
def movie_detail():
    """
    Renders the movie_rating.html template, displaying detailed movie
    information based on the 'movie_id' and 'image_url' parameters
    passed in the URL.

    Parameters:
    None

    Returns:
    Returns the rendered 'movie_rating.html' template with the
    'movie_url' and 'info_ls' variables.
    """
    movie_id = request.args.get('movie_id')
    movie_url = request.args.get('image_url')
    info_ls = get_movie_details(movie_id, ott)
    return render_template("movie_rating.html", movie_url=movie_url,
                           info_ls=info_ls)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
