import webbrowser  # imports webbrowser and its methods

# !/usr/bin/env python
__author__ = "Abdi Ibrahim"
__version__ = "1.0"


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This method stores variables for movie_title, movie_storyline,
        poster_image, trailer_youtube"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method opens the default web browser and plays the movie's
        youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)
