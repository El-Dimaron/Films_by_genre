import os
import json
import csv
from database import *

# Step 1

ganres_dict = json.loads(ganres)

# Step 2

os.mkdir("Film Genres")
os.chdir("Film Genres")
print(os.getcwd())

for genre in ganres_dict["results"]:
	os.mkdir(genre["genre"])

# Step 3/4


def stop_symbol(symbol, location, result_symbol="O"):		# used as an intermediate check for prohibited symbol; decided to use a function instead of another 'if' statement for better code comprehension
	if symbol in location:
		location = location.replace(symbol, result_symbol)
	return location

for film in films_data:		# iteration through each film
	for genre in film["gen"]:		# iteration through each genre
		genre_list = [x["genre"] for x in film["gen"]]		# create list of genres
		genre_str = ";".join(genre_list)					# transform list into string
		film_genre = genre["genre"]		# intermediate var for better code readability
		csv_file_path = f"{film_genre}/{film_genre}.csv"
		film["title"] = stop_symbol("Ô", film["title"])
		csv_elements_list = [film["title"], film["year"], film["rating"], film["type"], genre_str]	 # readability and easier file editing
		if not os.path.isfile(csv_file_path):		# create file if it does not exist, else - open it
			film_genre_obj = open(csv_file_path, "w")
			csv.writer(film_genre_obj).writerows([["title", "year", "rating", "type", "ganres"], csv_elements_list])
		else:
			film_genre_obj = open(csv_file_path, "a")
			csv.writer(film_genre_obj).writerow(csv_elements_list)

os.chdir("Film Genres")

for directory in os.listdir():
	if not os.listdir(directory):
		os.mkdir(f"{directory}/.gitkeep")
