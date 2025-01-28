from flask import Flask
from flask import render_template, request, redirect, url_for, flash, make_response, Response
import polars as pl
import csv
import os
import time
import random
app = Flask(__name__)

data_path="db_dump/uncompressed/"
test_time_dir="testing/results/"
test_time_log_file="test_time_log_1.csv"

lst = os.listdir(test_time_dir)
if lst:
    lst.sort()
    i=int(lst[-1].split("_")[-1][:-4])+1
    test_time_log_file=test_time_log_file[:-5]+str(i)+".csv"

#DATASET DATA TABLES
title_principals = pl.scan_csv(data_path+"title.principals.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
name_basics = pl.scan_csv(data_path+"name.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_akas = pl.scan_csv(data_path+"title.akas.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_crew = pl.scan_csv(data_path+"title.crew.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_episode = pl.scan_csv(data_path+"title.episode.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_basics = pl.scan_csv(data_path+"title.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_ratings = pl.scan_csv(data_path+"title.ratings.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")

title_principals2 = pl.scan_csv(data_path+"title.principals.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
name_basics2 = pl.scan_csv(data_path+"name.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_akas2 = pl.scan_csv(data_path+"title.akas.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_crew2 = pl.scan_csv(data_path+"title.crew.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_episode2 = pl.scan_csv(data_path+"title.episode.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_basics2 = pl.scan_csv(data_path+"title.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_ratings2 = pl.scan_csv(data_path+"title.ratings.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")

title_principals3 = pl.scan_csv(data_path+"title.principals.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
name_basics3 = pl.scan_csv(data_path+"name.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_akas3 = pl.scan_csv(data_path+"title.akas.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_crew3 = pl.scan_csv(data_path+"title.crew.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_episode3 = pl.scan_csv(data_path+"title.episode.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_basics3 = pl.scan_csv(data_path+"title.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_ratings3 = pl.scan_csv(data_path+"title.ratings.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")

title_principals4 = pl.scan_csv(data_path+"title.principals.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
name_basics4 = pl.scan_csv(data_path+"name.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_akas4 = pl.scan_csv(data_path+"title.akas.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_crew4 = pl.scan_csv(data_path+"title.crew.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
#title_episode4 = pl.scan_csv(data_path+"title.episode.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_basics4 = pl.scan_csv(data_path+"title.basics.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")
title_ratings4 = pl.scan_csv(data_path+"title.ratings.tsv", quote_char=None, has_header=True, separator="\t", null_values="\\N")

def write_log_to_csv(filename, row, dir=test_time_dir):
    with open(dir+filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/movies", methods=['GET', 'POST'])
def get_movie_list():
    # ----- Server operation -----
    movie_list=None

    if request.method == "POST":
        req = request.form
        title = req.get("title_textbox")
        
        # ----- DB operation -----
        start_timer = time.time()
        movie_list = title_basics.select([
                pl.col("tconst"),
                pl.col("primaryTitle"),
                pl.col("originalTitle"),
                pl.col("startYear"),
                pl.col("runtimeMinutes"),
                pl.col("titleType")
            ]).filter(            
            pl.col("primaryTitle").str.contains(f".*{title}.*") |
            pl.col("originalTitle").str.contains(f".*{title}.*") ).collect()
        end_timer = time.time()
        delta=round(end_timer-start_timer, 4)
        write_log_to_csv(test_time_log_file, [delta])
    else:
        # ----- DB operation -----
        start_timer = time.time()
        rand = random.randint(1, 4)
        if rand == 1:
            movie_list = title_basics.select([
                    pl.col("tconst"),
                    pl.col("primaryTitle"),
                    pl.col("originalTitle"),
                    pl.col("startYear"),
                    pl.col("runtimeMinutes"),
                    pl.col("titleType")
                ]).fetch(100)
        elif rand == 2:
            movie_list = title_basics2.select([
                    pl.col("tconst"),
                    pl.col("primaryTitle"),
                    pl.col("originalTitle"),
                    pl.col("startYear"),
                    pl.col("runtimeMinutes"),
                    pl.col("titleType")
                ]).fetch(100)
        elif rand == 3:
            movie_list = title_basics3.select([
                    pl.col("tconst"),
                    pl.col("primaryTitle"),
                    pl.col("originalTitle"),
                    pl.col("startYear"),
                    pl.col("runtimeMinutes"),
                    pl.col("titleType")
                ]).fetch(100)
        elif rand == 4:
            movie_list = title_basics4.select([
                    pl.col("tconst"),
                    pl.col("primaryTitle"),
                    pl.col("originalTitle"),
                    pl.col("startYear"),
                    pl.col("runtimeMinutes"),
                    pl.col("titleType")
                ]).fetch(100)
            
        end_timer = time.time()
        delta=round(end_timer-start_timer, 4)
        write_log_to_csv(test_time_log_file, [delta])

    # ----- Server operation -----
    is_empty=movie_list.is_empty()
    movie_list = movie_list.to_dict()

    return render_template('movie_list_page.html', movie_list=movie_list, is_empty=is_empty)


@app.route("/movies/<id>", methods=['GET'])
def get_movie_info(id):

    # ----- DB operation -----
    start_timer = time.time()

    rand = random.randint(1, 4)
    if rand == 1:
        movie = title_basics.filter(pl.col("tconst") == id)
        movie_info=movie.join(title_ratings, on="tconst", how="inner").select(pl.exclude("tconst"))

        cast = title_principals.filter(pl.col("tconst") == id)
        cast_list_info = cast.join(name_basics, on="nconst", how="inner").select(pl.exclude(["tconst", "nconst", "knownForTitles", "ordering"]))
        
        directors=title_crew.filter(pl.col("tconst") == id).select(pl.col("directors").str.split(",").alias("split_str")).explode("split_str")
        writers=title_crew.filter(pl.col("tconst") == id).select(pl.col("writers").str.split(",").alias("split_str")).explode("split_str")
        directors_list_info=directors.join(name_basics, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
        writers_list_info=writers.join(name_basics, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
    elif rand == 2:
        movie = title_basics2.filter(pl.col("tconst") == id)
        movie_info=movie.join(title_ratings2, on="tconst", how="inner").select(pl.exclude("tconst"))

        cast = title_principals2.filter(pl.col("tconst") == id)
        cast_list_info = cast.join(name_basics2, on="nconst", how="inner").select(pl.exclude(["tconst", "nconst", "knownForTitles", "ordering"]))
        
        directors=title_crew2.filter(pl.col("tconst") == id).select(pl.col("directors").str.split(",").alias("split_str")).explode("split_str")
        writers=title_crew2.filter(pl.col("tconst") == id).select(pl.col("writers").str.split(",").alias("split_str")).explode("split_str")
        directors_list_info=directors.join(name_basics2, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
        writers_list_info=writers.join(name_basics2, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
    elif rand == 3:
        movie = title_basics3.filter(pl.col("tconst") == id)
        movie_info=movie.join(title_ratings3, on="tconst", how="inner").select(pl.exclude("tconst"))

        cast = title_principals3.filter(pl.col("tconst") == id)
        cast_list_info = cast.join(name_basics3, on="nconst", how="inner").select(pl.exclude(["tconst", "nconst", "knownForTitles", "ordering"]))
        
        directors=title_crew3.filter(pl.col("tconst") == id).select(pl.col("directors").str.split(",").alias("split_str")).explode("split_str")
        writers=title_crew3.filter(pl.col("tconst") == id).select(pl.col("writers").str.split(",").alias("split_str")).explode("split_str")
        directors_list_info=directors.join(name_basics3, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
        writers_list_info=writers.join(name_basics3, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
    elif rand == 4:
        movie = title_basics4.filter(pl.col("tconst") == id)
        movie_info=movie.join(title_ratings4, on="tconst", how="inner").select(pl.exclude("tconst"))

        cast = title_principals4.filter(pl.col("tconst") == id)
        cast_list_info = cast.join(name_basics4, on="nconst", how="inner").select(pl.exclude(["tconst", "nconst", "knownForTitles", "ordering"]))
        
        directors=title_crew4.filter(pl.col("tconst") == id).select(pl.col("directors").str.split(",").alias("split_str")).explode("split_str")
        writers=title_crew4.filter(pl.col("tconst") == id).select(pl.col("writers").str.split(",").alias("split_str")).explode("split_str")
        directors_list_info=directors.join(name_basics4, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
        writers_list_info=writers.join(name_basics4, how="inner", left_on="split_str", right_on="nconst").select(pl.exclude(["nconst", "knownForTitles"]))
    
    movie_info=movie_info.collect()
    cast_list_info=cast_list_info.collect()
    directors_list_info=directors_list_info.collect()
    writers_list_info=writers_list_info.collect()

    end_timer = time.time()

    delta=round(end_timer-start_timer, 4)
    write_log_to_csv(test_time_log_file, [delta])

    # ----- Server operation -----
    movie_info = movie_info.to_dict()
    cast_list_info = cast_list_info.to_dict()
    directors_list_info = directors_list_info.to_dict()
    writers_list_info = writers_list_info.to_dict()

    return render_template('movie_info.html', movie_info=movie_info, cast_list_info=cast_list_info, directors_list_info=directors_list_info, writers_list_info=writers_list_info)


