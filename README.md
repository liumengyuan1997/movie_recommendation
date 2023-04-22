## Flask Application for a Movie Search, Rating, and Recommendation System
This Flask application is designed to provide a movie search, rating, and recommendation system for users. The application allows users to search for movies based on title, view movie details, and receive recommendations based on movie ratings and reviews. The application uses the following libraries: Flask, os, urllib, and json.

### How to Use the Application 
1. Clone the repository to your local machine.  
2. Install the required libraries using pip: Flask, os, urllib, and json.  
3. Add keys.json file into the Flask package. This file should contain your keys of your Flask app and APIs and formatted like the following (remember to replace the "key" with your actual keys).  

  {
  <br>   "app_secret_key" = "key",
  <br>   "imdb_key": "key",
  <br>   "ott_key": "key",
  <br>   "omdb_key": "key",
  <br>   "chatgpt_key": "key"
  }

4. Run the Flask application in your terminal using the command: python3 run.py.Open your browser and navigate to http://localhost:5000/ to access the main page.  
5. Enter a movie title in the search bar and click the 'Search' button.  
6. The application will display a list of movies based on the user's search query. Select a movie to view more details or receive recommendations.  
7. To view more details about a movie, click the 'View Details' button.  
8. To receive recommendations, rate the movie and write a review, then click the 'Get Recommendations' button.  
9. The application will display a list of recommended movies based on the user's ratings and reviews.  

### Functionality The application is built using Flask and consists of several routes:

/: This route renders the main.html template. If a POST request is received, it redirects the user to the get_movies route with the title parameter specified in the request form.

/<title>: This route renders the select_movie.html template, displaying a list of movies with images and titles, based on the user's search query specified in the title parameter. If a POST request is received, the user can select a movie to get more details or to receive recommendations based on their further input.

/id/<movie_id>: This route renders the movie_rating.html template, displaying movie details such as title, image, release year, genre, synopsis, and ratings, based on the movie_id parameter passed to the URL.

/movie_title/movie_recommendation: This route renders the get_review.html template, allowing the user to rate a movie and write a review to receive recommendations for similar movies.

/movie_title/movie_recommendation/detail: This route renders the movie_rating.html template, displaying detailed movie information based on the movie_id and image_url parameters passed in the URL.

### Contact 
For any questions or issues, please contact liumengyuan23@gmail.com.
