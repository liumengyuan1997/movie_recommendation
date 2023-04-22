"""
A module of tests of the functions in api_response.py

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""
import unittest
import requests
from unittest.mock import patch, MagicMock
from api_response import *


class TestApi(unittest.TestCase):
    @patch('requests.request')
    def test_imdb_success(self, mock_request):
        """
        Test the imdb() function when a successful response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'title': 'The Matrix'}
        mock_request.return_value = mock_response
        result = imdb('The Matrix', 'test_key')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), {'title': 'The Matrix'})

    @patch('requests.request')
    def test_imdb_failure(self, mock_request):
        """
        Test the imdb() function when a failed response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response
        response, status_code = imdb('Non-existing movie', 'test_key')
        self.assertEqual(json.loads(response),
                         {'error': 'Failed to get movies from IMDb'})
        self.assertEqual(status_code, 500)

    @patch('requests.request')
    def test_ott_success(self, mock_request):
        """
        Test the ott() function when a successful response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'tt1234567': 'The Matrix'}
        mock_request.return_value = mock_response
        result = ott("tt1234567", "valid_key")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), {'tt1234567': 'The Matrix'})

    @patch('requests.request')
    def test_ott_failure(self, mock_request):
        """
        Test the ott() function when a failed response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response
        response, status_code = ott('Non-existing movie id', 'test_key')
        self.assertEqual(json.loads(response),
                         {'error':
                          'Failed to get information from OTT'})
        self.assertEqual(status_code, 500)

    @patch('requests.get')
    def test_omdb_success(self, mock_request):
        """
        Test the omdb() function when a successful response is received.

        Args:
        mock_request: A mocked version of the requests.get() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Poster": "http://example.com/poster.jpg"
        }
        mock_request.return_value = mock_response
        result = omdb("tt1234567", "valid_key")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(),
                         {"Poster":
                          "http://example.com/poster.jpg"})

    @patch('requests.get')
    def test_omdb_failure(self, mock_request):
        """
        Test the imdb() function when a failed response is received.

        Args:
        mock_request: A mocked version of the requests.get() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response
        response, status_code = omdb("invalid_id", "invalid_key")
        self.assertEqual(json.loads(response),
                         {'error':
                         "Failed to get posters' url of movies from OMDB"})
        self.assertEqual(status_code, 500)

    @patch('requests.request')
    def test_chatgpt_success(self, mock_request):
        """
        Test the chatgpt() function when a successful response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "text": "tt1234567,tt2345678,tt3456789"
                }
            ]
        }
        mock_request.return_value = mock_response
        result = chatgpt("Inception", "8", "Great movie", "valid_key")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(),
                         {"choices":
                         [{"text": "tt1234567,tt2345678,tt3456789"}]})

    @patch('requests.request')
    def test_chatgpt_failure(self, mock_request):
        """
        Test the chatgpt() function when a failed response is received.

        Args:
        mock_request: A mocked version of the requests.request() method.

        Returns:
        None.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response
        response, status_code = chatgpt("Inception", "8",
                                        "Great movie", "invalid_key")
        self.assertEqual(json.loads(response),
                         {'error':
                         "Failed to get recommendations from ChatGPT"})
        self.assertEqual(status_code, 500)
