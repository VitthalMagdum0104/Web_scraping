import requests
from bs4 import BeautifulSoup
import pandas as pd

# url for Top indian movies
url = "https://www.imdb.com/india/top-rated-indian-movies/"

res = requests.get(url=url)

soup = BeautifulSoup(res.text, features="html.parser")

all_tr = soup.findChildren("tr")

title = []
year = []
rating = []

movie_data = {}

for movie in all_tr:
    try:
        title.append(movie.find(
            "td", {"class": "titleColumn"}).find("a").contents[0])
        year.append(movie.find("td", {"class": "titleColumn"}).find(
            "span", {"class": "secondaryInfo"}).contents[0])
        rating.append(movie.find(
            "td", {"class": "ratingColumn imdbRating"}).find("strong", {}).contents[0])
    except:
        continue

movie_data["Title"] = title
movie_data["Year"] = year
movie_data["Rating"] = rating

movies = pd.DataFrame(movie_data)

movies.to_csv("top_bollywood_movies.csv")
movies.to_excel("top_bollywood_movies.xlsx")
