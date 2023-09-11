# Shimoku-dashboard
This project uses the Shimoku python api to create an online dashboard. A jupyter notebook is waiting for you to check the different steps of this project, includin an EDA, data processing, charts creation and a quick ML model.
## Data
In particular, we will work with two datasets of TV shows and films with the following information:<br>
<br>
**all_titles.csv** includes the next columns:

<pre>- id: ID for the title<br>
- title: Name of the movie or show<br>
- type: indicates if it is a movie or a show<br>
- description: brief synopsis of the title<br>
- release year: Year where the movie/show was first released<br>
- age_certification: certification type of age limitation, if any<br>
- runtime: duration of the full movie or duration of each show episode<br>
- genres: list of main movie or show genres<br>
- production_countries: list of countries where the title was produced<br>
- seasons: number of seasons of the show<br>
- imdb_id: identifier of the Internet Movie DataBase (IMDB) dataset<br>
- imdb_score: average public rating of the title in IMDB<br>
- imdb_votes: number of votes used to compute the imdb_score field<br>
- tmdb_popularity: popularity score of the title on the The Movie DataBase (TMDB) platform<br>
- tmdb_score: average rating of the title in TMDB<br>
- streaming: name of the streaming service listing the film<br></pre>

**all_credits.csv** includes the next columns:<br>

<pre>- person_id: identifier of the person doing the role<br>
- id: ID for the title (same ID used on all_titles.csv)<br>
- name: name of the person doing the role<br>
- character: name of the character in the title, if any<br>
- role: indicates if the person has the role actor or a director</pre><br>

The aim is to answer these three questions:<br>
1. How have genre trends evolved over the years?<br>
2. How does each platform manage movies?<br>
3. What impact do actors or directors have on the evaluation of movies?<br>


## Installation
You can find on [Shimoku](https://docs.shimoku.com/development/getting-started/quickstart) website all the steps to activate your account and start creating your dashboards, as well as tips on how to use them.<br>

And in the Python +3.9 install it with pip:<br><br>
```pip install shimoku-api-python```<br><br>
Also, you can check their [Github](https://github.com/shimoku-tech/shimoku-api-python)


