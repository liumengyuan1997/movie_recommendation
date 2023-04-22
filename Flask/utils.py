"""
Utility functions that help with run.py

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""


def check_number(user_input: str) -> bool:
    """Check whether the input is a valid number.

    Args:
        user_input (str): the string of user input

    Returns:
        bool: whether the input value is valid
    """
    try:
        float_val = float(user_input)
    except ValueError:
        return False
    return True


def convert_rating(rating: str, min_score: int, max_score: int) -> str:
    """Converts rating to a resonable one. Will convert any value under
    min_score to be min_score and anything over max_score to be max_score.

    Args:
        rating (str): the input rating string
        min_score (int): the minimum rating score.
        max_score (int): the minimum rating score.

    Returns:
        str: scores between min_score and max_score
    """
    rating = float(rating)
    if rating < min_score:
        rating = min_score
    if rating > max_score:
        rating = max_score
    return str(rating)
