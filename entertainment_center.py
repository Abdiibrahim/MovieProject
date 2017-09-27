import media  # imports media.py
import fresh_tomatoes  # imports fresh_tomatoes.py

# !/usr/bin/env python
__author__ = "Abdi Ibrahim"
__version__ = "1.0"


"""Initialize objects for each movie."""
the_prestige = media.Movie(
    "The Prestige",
    "Two magicians engage in competitive one-upmanship to create the ultimate "
    "stage illusion.",
    "http://www.impawards.com/2006/posters/prestige_xlg.jpg",
    "https://www.youtube.com/watch?v=DHoXum3M9eE")

fight_club = media.Movie(
    "Fight Club",
    "An office worker crosses paths with a soap maker, forming a fight club.",
    "https://s-media-cache-ak0.pinimg.com/originals/06/27/ed/"
    "0627edaeb7eda6d1659c43256f87821d.jpg",
    "https://www.youtube.com/watch?v=BdJKm16Co6M")

john_wick_2 = media.Movie(
    "John Wick: Chapter 2",
    "Legendary hit man is forced out of retirement again",
    "http://cdn3-www.comingsoon.net/assets/uploads/gallery/john-wick-2/"
    "johnwicksmall.jpg",
    "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

your_name = media.Movie(
    "Your Name.",
    "Two strangers find themselves linked in a bizarre way.",
    "https://i.imgur.com/Uqw37Sk.jpg",
    "https://www.youtube.com/watch?v=o4-URMnBOPU")

get_out = media.Movie(
    "Get Out",
    "It's time for a young African American to meet with his white "
    "girlfriend's parents.",
    "https://cdn.traileraddict.com/content/universal-pictures/"
    "get-out-2017-4.jpg",
    "https://www.youtube.com/watch?v=DzfpyUB60YY")

lion_king = media.Movie(
    "The Lion King",
    "Lion cub and future king Simba searches for his identity.",
    "http://www.impawards.com/1994/posters/lion_king_ver4_xlg.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

movies = [the_prestige, fight_club, john_wick_2, your_name, get_out, lion_king]
# creates an array movies which contains the movie instances.
fresh_tomatoes.open_movies_page(movies)
# calls open_movies_page() method from fresh_tomatoes.py
