## Flask Application for a Movie Search, Rating, and Recommendation System
This Flask application is designed to provide a movie search, rating, and recommendation system for users. The application allows users to search for movies based on title, view movie details, and receive recommendations based on movie ratings and reviews. The application uses the following libraries: Flask, os, urllib, json, requests, and re.

### How to Use the Application 
1. Clone the repository to your local machine.  
2. Install the required libraries using  
```
pip install Flask urllib requests
```
3. Add keys.json file into the Flask package. This file should contain your keys of your Flask app and APIs and formatted like the following (remember to replace the "key" with your actual keys).  
```json
  {
    "app_secret_key": "key",
    "imdb_key": "key",
    "ott_key": "key",
    "omdb_key": "key",
    "chatgpt_key": "key"
   }
```
4. Run the Flask application in your terminal using the command: python3 run.py. Open your browser and navigate to http://127.0.0.1:5000 to access the main page.  
5. Enter a movie title in the search bar and click the 'Search' button.  
6. The application will display a list of movies based on the user's search query. Select a movie to view more details or receive recommendations.  
7. To view more details about a movie, click the 'Want to watch' button.  
8. To rate the movie, write a review, and receive recommendations, then click the 'Already watched' button.  
9. The application will display a list of recommended movies based on the user's ratings and reviews.  

### Functionality The application is built using Flask and consists of several routes:

/: This route renders the main.html template. If a POST request is received, it redirects the user to the get_movies route with the title parameter specified in the request form.

/<title>: This route renders the select_movie.html template, displaying a list of movies with images and titles, based on the user's search query specified in the title parameter. If a POST request is received, the user can select a movie to get more details or to receive recommendations based on their further input.

/id/<movie_id>: This route renders the movie_rating.html template, displaying movie details such as title, image, release year, genre, synopsis, and ratings, based on the movie_id parameter passed to the URL.

/movie_title/movie_recommendation: This route renders the get_review.html template, allowing the user to rate a movie and write a review to receive recommendations for similar movies. If a POST request is received, the user will receive movie recommendations based on their previous rating and reviews.

/movie_title/movie_recommendation/detail: This route renders the movie_rating.html template, displaying detailed movie information based on the movie_id and image_url parameters passed in the URL.

### Contact 
For any questions or issues, please contact liumengyuan23@gmail.com.

### Project Reflection
There are lots of learning points for this project. What I can think of includes building a Flask application for a movie search, rating, and recommendation system, using APIs to retrieve data, implementing a chatbot using OpenAI's GPT-3 to provide movie recommendations based on user reviews and ratings, developing a user interface with HTML, CSS, and JS, using templates and forms to handle user input and display data.

I like the process of getting a project done. It gives me a sense of achievement. And I also learned a lot during the process. Not only did I become more proficient in using the concept I learned in the course CS5001, but also I learned some new knowledge, such as building a simple web using the Flask framework, and using HTML, CSS, and JS to create beautiful user interfaces. Also, I use lots of APIs in my project. This is the first time I know how powerful the API is. But, since there is a lot of new knowledge for me to learn, I definitely encounter lots of difficulties during the process. For example, at first, I was not familiar with the APIs usage, so I spent lots of time making those APIs work in my expected way. And also, there was one time, my API usage reached the limits, but I don’t know about that and I think there might be an unexpected bug in my code, which consumes me lots of time to figure it out. At last, I figured out that it is because of the API usage limitation. Also, designing and implementing the front end of the application is also challenging, since I’m not experienced with HTML, CSS, and JavaScript. Those three tools are new concepts to me. Even though there are plenty of learning sources on the web, I still need to learn the basic language semantics and see whether the online recourses can fit my project. And last, handling errors and debugging the application is also difficult, since I have multiple routes, functions, and templates. So when bugs come out, I usually go around all my files, to check the possible positions that bug comes from. 


There are several imperfect places in my project, and that’s where I can work on later. First, since I use APIs, my runtime is somewhat longer than thought. And since I use several APIs, the things that usually happen are the movie exists in one API does not exist in another one. So sometimes, I get internal errors due to information inconsistency. So, I plan to create my own database to replace the use of APIs in the future, which will significantly reduce runtime, and reduce the possibility of information inconsistency. Secondly, my recommendation system is built on chatGPT-3, which is for fun at the beginning. Therefore, I aim to store users' comments and perform sentiment analysis on them to provide more personalized, serious, and accurate recommendations. Thirdly, in order to support the sentiment analysis functionality, I also need to develop additional functions such as write-to-file and read-from-file to manage user comments effectively. 

Since I want to be a software engineer in the future, the process of developing a Flask application equipped me with some essential skills that software engineers need to have, even though, what I’ve learned is really superficial. For instance, building a web application requires an understanding of web technologies, such as HTML, CSS, and JavaScript. It also requires proficiency in server-side programming languages like Python and an understanding of web frameworks like Flask. Additionally, developing a web application requires skills in problem-solving, debugging, and testing, which are critical for any software engineering role. Overall, I think developing a web application is a valuable experience for anyone aspiring to become a software engineer. It provides an opportunity to learn and practice essential skills, tools, and technologies that are necessary for a career in software engineering.
