"""
A module of tests of the functions in response_handle.py

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""
import unittest
from unittest.mock import patch, MagicMock
import json
import re
from api_response import *
from response_handle import *


class TestApiHandle(unittest.TestCase):

    def test_select_movie_success(self):
        """
        Test the select_movie function when successfully getting response.
        """
        with patch('api_response.imdb') as mock_imdb:
            mock_response = MagicMock()
            mock_response.text = json.dumps({
                "d": [{
                    "id": "tt0111161",
                    "l": "The Shawshank Redemption",
                    "y": "1994",
                    "i": {
                        "imageUrl": "https://SR.jpg"
                    }
                }]
            })
            mock_imdb.return_value = mock_response
            expected_output = {
                  0: ['The Shawshank Redemption',
                      'https://SR.jpg', '1994', 'tt0111161']}
            output = select_movie('The Shawshank Redemption', imdb=mock_imdb)
            self.assertEqual(expected_output, output)

    @patch('api_response.imdb')
    def test_select_movie_fail(self, mock_imdb):
        """
        Test the select_movie function when failing to get a response.
        """
        mock_imdb.return_value = ('', 'Failed to connect to the IMDB API.')

        result = select_movie('fast and furious', mock_imdb)

        expected_result = 'Failed to connect to the IMDB API.'
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_result)

    def test_get_movie_details_success(self):
        """
        Test the get_movie_details function when successfully getting response.
        """
        fake_synopsis = '''Two imprisoned men bond over a
                           number of years, finding solace and eventual
                           redemption through acts of common decency.'''
        with patch('api_response.ott') as mock_ott:
            mock_response = MagicMock()
            mock_response.text = json.dumps(
                        {
                            "title": "The Shawshank Redemption",
                            "imdbid": "tt0111161",
                            "genre": "Drama",
                            "runtime": "2h 22min",
                            "imdbrating": "9.3",
                            "synopsis": fake_synopsis,
                            "language": "English",
                            "streamingAvailability":
                            {"country": {"US": "Netflix"}}}
                        )
            mock_ott.return_value = mock_response
            expected_output = ['Drama', '2h 22min', '9.3',
                               fake_synopsis, 'English', 'Netflix',
                               'tt0111161', 'The Shawshank Redemption']
            output = get_movie_details('tt0111161', ott=mock_ott)
            self.assertEqual(expected_output, output)

    @patch('api_response.ott')
    def test_get_movie_details_fail(self, mock_ott):
        """
        Test the get_movie_details function when cannot get the response.
        """
        mock_ott.return_value = ('Connection failed', 500)

        result = get_movie_details('tt0133093', mock_ott)
        expected_result = "Failed to get movies information from OTT"

        self.assertEqual(result, expected_result)

    def test_get_omdb_url(self):
        """
        Test the get_omdb_url function when successfully getting response.
        """
        with patch('api_response.omdb') as mock_omdb:
            mock_response = MagicMock()
            mock_response.json.return_value = {
                'Title': 'The Shawshank Redemption',
                'Poster': 'https://SR.jpg'}
            mock_omdb.return_value = mock_response
            expected_output = ('The Shawshank Redemption',
                               'https://SR.jpg')
            output = get_omdb_url('tt0111161', omdb=mock_omdb)
            self.assertEqual(expected_output, output)

    @patch('api_response.omdb')
    def test_get_omdb_url_fail(self, mock_omdb):
        """
        Test the get_omdb_url function when cannot get the response.
        """
        mock_omdb.return_value = ("Failed to connect to OMDB API.", 500)
        result = get_omdb_url("tt1234567", mock_omdb)
        self.assertEqual(result,
                         "Failed to get posters' url of movies from OMDB")

    def test_chatgpt_recommendation_success(self):
        """
        Test the chatgpt_recommendation function when successfully
        getting response.
        """
        with patch('api_response.chatgpt') as mock_chatgpt, \
             patch('response_handle.get_omdb_url') as mock_get_omdb_url:

            mock_chat_response = MagicMock()
            mock_chat_response.text = json.dumps({
                "choices": [
                    {
                        "message": {
                            "content": "I recommend tt1234567."
                        }
                    }
                ]
            })
            mock_chatgpt.return_value = mock_chat_response
            mock_get_omdb_url.return_value = ("Movie 1", "http://poster1.jpg")
            expected_output = {
                "tt1234567": ["Movie 1", "http://poster1.jpg"]
            }
            output = chatgpt_recommendation(
                         "The Dark Knight", 8,
                         "Great movie!", chatgpt=mock_chatgpt)
            self.assertEqual(expected_output, output)

    @patch('api_response.chatgpt')
    def test_chatgpt_recommendation_fail(self, mock_chatgpt):
        """
        Test the chatgpt_recommendation function when cannot get the response.
        """
        mock_chatgpt.return_value = ("Failed to connect to ChatGPT API.", 500)
        result = chatgpt_recommendation("one day", "9.0", "nice", mock_chatgpt)
        self.assertEqual(result,
                         "Failed to get recommendations from ChatGPT")
