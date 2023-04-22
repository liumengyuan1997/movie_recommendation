"""
A module of tests of the functions in run.py

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""
from unittest import TestCase
from unittest.mock import patch, MagicMock
from run import *


class TestRun(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_get(self):
        """test case for the index function with GET method"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        """test case for the index function with POST method"""
        title = 'test-movie-title'
        response = self.app.post('/', data=dict(title='One Day'))
        self.assertEqual(response.status_code, 302)

    def test_get_movies_get(self):
        """test case for the get_movies function with GET method"""
        test_dict = {'key1': 'value1', 'key2': 'value2'}
        test_list = [1, 2, 3, 4, 5]
        response = self.app.get("/One Day")
        self.assertEqual(response.status_code, 200)

    def test_get_movies_post_option1(self):
        """test case for the get_movies function with POST method, option 1"""
        response = self.app.post('/The Lion King', data=dict(
                                 title='The Lion King', year='1994',
                                 choice='option1'))
        self.assertEqual(response.status_code, 302)

    def test_get_movies_post_option2(self):
        """test case for the get_movies function with POST method, option 2"""
        response = self.app.post('/The Lion King', data=dict(
                                 title='The Lion King', year='1994',
                                 choice='option1'))
        self.assertEqual(response.status_code, 302)

    def test_get_rating_get(self):
        """test case for the get_rating function with GET method"""
        mock_get_movie_details = MagicMock(return_value=[
                "The Lion King", "1994", "Animation, Adventure, Drama"])
        response = self.app.get('/id/tt0110357')
        self.assertEqual(response.status_code, 200)

    def test_get_recommendation_get(self):
        """test case for the get_recommendation function with GET method"""
        response = self.app.get('/movie_title/movie_recommendation')
        self.assertEqual(response.status_code, 200)

    def test_get_recommendation_post(self):
        """test case for the get_recommendation function with POST method"""
        mock_chatgpt_recommendation = MagicMock(return_value={
                   "1": "The Lion King", "2": "One Day"})
        response = self.app.post('/movie_title/movie_recommendation',
                                 data=dict(rating='5',
                                           movie_review='Great movie!'))
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_get(self):
        """test case for the movie_detail function with GET method"""
        mock_get_movie_details = MagicMock(return_value=[
                "The Lion King", "1994", "Animation, Adventure, Drama"])
        response = self.app.get('/id/tt0110357')
        self.assertEqual(response.status_code, 200)
