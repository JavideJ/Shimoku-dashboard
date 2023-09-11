from collections import Counter

def common_genres(df_movies, df_shows):
    """
    Get the 8 most common genres on TV shows and movies separately.
    
    Parameters:
    df_movies: Pandas Dataframe filtered by movies
    df_shows: Pandas Dataframe filtered by shows
    """
    # Get the genres appearences on each one
    movie_genres = []
    show_genres = []
    for m_genres, s_genres in zip(df_movies['genres'], df_shows['genres']):
        movie_genres.extend(m_genres)
        show_genres.extend(s_genres)

    movie_genres_freq = Counter(movie_genres).most_common()
    show_genres_freq = Counter(show_genres).most_common()

    # Filter the 8 most common genres
    main_movie_genres = list(dict(movie_genres_freq[0:8]).keys())
    main_show_genres = list(dict(show_genres_freq[0:8]).keys())
    
    return main_movie_genres, main_show_genres


def get_movie_genres_data(df_movies, main_movie_genres):
    """
    Data with movie genres percentages per year.
    Returns a list of dictionaries where each one has the following structure:
    {genre_1:float(% movies),
     genre_2:float(% movies),
     ...
     year:str(year)
    }
    
    Parameters:
    df_movies: Pandas Dataframe filtered by movies
    main_movie_genres: list with 8 main movie genres
    """
    # Get an ordered years list
    years_unique = sorted(df_movies.release_year.unique())

    # Now let´s create a list of dictionaries with the number of genres appearances on each year
    movie_genres_data = []
    for year in years_unique:
        df_year = df_movies[df_movies['release_year'] == year]
        genres_by_year = []

        for genres in df_year['genres']:
            for genre in genres:
                if genre in main_movie_genres:
                    genres_by_year.append(genre)

        genres_by_year_dict = dict(Counter(genres_by_year))
        total = sum(dict(Counter(genres_by_year)).values())

        # Put it as percentage
        for k in genres_by_year_dict:
            old_value = genres_by_year_dict[k]
            genres_by_year_dict[k] = round(old_value/total, 2)
        genres_by_year_dict['year'] = str(year)

        # Let´s add the genres with 0 appearances to the dict (in case there are)
        genres_zero = set(main_movie_genres) - set(genres_by_year_dict.keys())

        for gen_zero in genres_zero:
            genres_by_year_dict[gen_zero] = 0

        movie_genres_data.append(genres_by_year_dict)
        
    return movie_genres_data


def get_show_genres_data(df_shows, main_show_genres):
    """
    Data with show genres percentages per year.
    Returns a list of dictionaries where each one has the following structure:
    {genre_1:float(% movies),
     genre_2:float(% movies),
     ...
     year:str(year)
    }
    
    Parameters:
    df_shows: Pandas Dataframe filtered by shows
    main_show_genres: list with 8 main show genres
    """
    years_unique = sorted(df_shows.release_year.unique())

    # Now let´s create a list of dictionaries with the number of genres appearances on each year
    show_genres_data = []
    for year in years_unique:
        df_year = df_shows[df_shows['release_year'] == year]
        genres_by_year = []

        for genres in df_year['genres']:
            for genre in genres:
                if genre in main_show_genres:
                    genres_by_year.append(genre)

            # There´s an empty genre, delete it
            # try:
            #     genres_by_year.remove('')
            # except:
            #     pass

        genres_by_year_dict = dict(Counter(genres_by_year))
        total = sum(dict(Counter(genres_by_year)).values())

        # Put it as percentage
        for k in genres_by_year_dict:
            old_value = genres_by_year_dict[k]
            genres_by_year_dict[k] = old_value/total
        genres_by_year_dict['year'] = str(year)

        # Let´s add the genres with 0 appearances to the dict
        genres_zero = set(main_show_genres) - set(genres_by_year_dict.keys())

        for gen_zero in genres_zero:
            genres_by_year_dict[gen_zero] = 0

        show_genres_data.append(genres_by_year_dict)
        
    return show_genres_data



def html_style(platform):
    """
    Define the html title style for each platform.
    
    Parameters:
    platform: str with the name of the platform
    """
    if platform == 'netflix':
        html = '''<style>
        .netflix-text {
        font-family: Arial, sans-serif;
        font-size: 50px;
        color: #E50914;
        }
        </style>
        <p class="netflix-text">Netflix</p>
        '''
    elif platform == 'disney':
        html = '''<style>
        .disney-text {
        font-family: Waltograph, Arial, sans-serif;
        font-size: 50px;
        color: #0063E1;
        }
        </style>
        <p class="disney-text">Disney</p>
        '''
    elif platform == 'amazon':
        html = '''<style>
        .amazon-text {
        font-family: Amazon Ember, Arial, sans-serif;
        font-size: 50px;
        color: #00A8E1;
        }
        </style>
        <p class="amazon-text">Amazon</p>
        '''
    elif platform == 'hbo':
        html = '''<style>
        .hbo-text {
        font-family: Arial, sans-serif;
        font-size: 50px;
        color: #941de8;
        }
        </style>
        <p class="hbo-text">HBO</p>
        '''
    elif platform == 'hulu':
        html = '''<style>
        .hulu-text {
        font-family: Proxima Nova, Arial, sans-serif;
        font-size: 50px;
        color: #1CE783;
        }
        </style>
        <p class="hulu-text">hulu</p>
        '''
    return html



def get_platform_genres_data(df_platform_movies):
    """
    Generate the list of dictionaries with the information of genres amount per platform.
    
    Parameters:
    df_platform_movies: Pandas Dataframe filtered by platform and movies
    """
    # Get the genres distribution
    platform_genres = []
    for genre in df_platform_movies['genres']:
        platform_genres.extend(genre)

    platform_genres_freq = dict(Counter(platform_genres).most_common())
    
    ## Build the list made of dictionaries. If a genre represent less than a 3% sum it as 'other'
    total_genres = sum(platform_genres_freq.values())
    platform_genres_data = []
    other = 0

    for k in platform_genres_freq.keys():
        genre_share = round(platform_genres_freq[k] / total_genres, 2)
        if  genre_share < 0.03:
            other += genre_share
        else:
            platform_genres_data.append({'genre':k.capitalize(), 'value':round(genre_share, 2)})

    platform_genres_data.append({'genre':'Other', 'value':round(other, 2)})
    
    return platform_genres_data



def get_platform_countries_data(df_platform_movies):
    """
    Generate the list of dictionaries with the information of countries amount per platform.
    
    Parameters:
    df_platform_movies: Pandas Dataframe filtered by platform and movies
    """
    # Get the countries distribution
    platform_countries = []
    for c in df_platform_movies['production_countries']:
        platform_countries.extend(c)

    platform_countries_freq = dict(Counter(platform_countries).most_common())
    
    ## Build the list made of dictionaries. If a country represent less than a 2% sum it as 'other'
    total_countries = sum(platform_countries_freq.values())
    platform_countries_data = []
    other = 0

    for k in platform_countries_freq.keys():
        country_share = round(platform_countries_freq[k] / total_countries, 2)
        if  country_share < 0.02:
            other += country_share
        else:
            platform_countries_data.append({'country':k, 'value':round(country_share, 2)})

    platform_countries_data.append({'country':'Other', 'value':round(other, 2)})
    
    return platform_countries_data



def create_runtime_groups(df):
    """
    Create runtime groups by 30 mins from 0-30 min to >=180 min.
    
    Parameters:
    df: Pandas Dataframe where the column will be created
    """
    runtime_groups = []
    for time in df.runtime:
        if (time>0) & (time<=30):
            runtime_groups.append('0_30')
        elif (time>30) & (time<=60):
            runtime_groups.append('30_60')
        elif (time>60) & (time<=90):
            runtime_groups.append('60_90')
        elif (time>90) & (time<=120):
            runtime_groups.append('90_120')
        elif (time>120) & (time<=150):
            runtime_groups.append('120_150')
        elif (time>150) & (time<=180):
            runtime_groups.append('120_150')
        else:
            runtime_groups.append('>=180')
            
    return runtime_groups



def top10_countries(df):
    """
    Returns a list with the top 10 countries with more appearances
    
    Parameters:
    df:Pandas Dataframe
    """

    countries = []
    for c in df['production_countries']:
        countries.extend(c)

    countries_freq = Counter(countries).most_common()
    countries_top10 = list(dict(countries_freq[:10]).keys())
    
    return countries_top10



def countries_dummy_dict(df, countries_top10):
    """
    Returns a dictionary where keys are the countries and values are lists with a 0 if the country did not appear on that row and 1 if it appeared
    
    Parameters:
    df: Pandas Dataframe
    countries_top10:  list with the top 10 countries with more appearances
    """
    # Create a dictionary to save each country appearance
    dummies_dict = {}
    for i in countries_top10:
        dummies_dict['dummy_' + i] = []

    dummies_dict['dummy_OTHER_countries'] = []

    for countries in df['production_countries']:
        if 'US' in countries:
            dummies_dict['dummy_US'].append(1)
        else:
            dummies_dict['dummy_US'].append(0)

        if 'GB' in countries:
            dummies_dict['dummy_GB'].append(1)
        else:
            dummies_dict['dummy_GB'].append(0)

        if 'IN' in countries:
            dummies_dict['dummy_IN'].append(1)
        else:
            dummies_dict['dummy_IN'].append(0)

        if 'CA' in countries:
            dummies_dict['dummy_CA'].append(1)
        else:
            dummies_dict['dummy_CA'].append(0)

        if 'FR' in countries:
            dummies_dict['dummy_FR'].append(1)
        else:
            dummies_dict['dummy_FR'].append(0)

        if 'DE' in countries:
            dummies_dict['dummy_DE'].append(1)
        else:
            dummies_dict['dummy_DE'].append(0)

        if 'JP' in countries:
            dummies_dict['dummy_JP'].append(1)
        else:
            dummies_dict['dummy_JP'].append(0)

        if 'ES' in countries:
            dummies_dict['dummy_ES'].append(1)
        else:
            dummies_dict['dummy_ES'].append(0)

        if 'IT' in countries:
            dummies_dict['dummy_IT'].append(1)
        else:
            dummies_dict['dummy_IT'].append(0)

        if 'AU' in countries:
            dummies_dict['dummy_AU'].append(1)
        else:
            dummies_dict['dummy_AU'].append(0)

        other_countries = set(countries) - set(countries_top10)

        if len(other_countries) > 0:
            dummies_dict['dummy_OTHER_countries'].append(1)
        else:
            dummies_dict['dummy_OTHER_countries'].append(0)
            
    return dummies_dict



def top10_genres(df):
    """
    Returns a list with the top 10 genres with more appearances
    
    Parameters:
    df:Pandas Dataframe
    """

    genres = []
    for c in df['genres']:
        genres.extend(c)

    genres_freq = Counter(genres).most_common()
    genres_top10 = list(dict(genres_freq[:10]).keys())
    
    return genres_top10



def genres_dummy_dict(df, genres_top10):
    """
    Returns a dictionary where keys are the genres and values are lists with a 0 if the genre did not appear on that row and 1 if it appeared
    
    Parameters:
    df: Pandas Dataframe
    genres_top10:  list with the top 10 genres with more appearances
    """
    # Create a dictionary to save each country appearance
    dummies_dict = {}
    for i in genres_top10:
        dummies_dict['dummy_' + i] = []

    dummies_dict['dummy_OTHER_genres'] = []

    for genres in df['genres']:
        if 'drama' in genres:
            dummies_dict['dummy_drama'].append(1)
        else:
            dummies_dict['dummy_drama'].append(0)

        if 'comedy' in genres:
            dummies_dict['dummy_comedy'].append(1)
        else:
            dummies_dict['dummy_comedy'].append(0)

        if 'thriller' in genres:
            dummies_dict['dummy_thriller'].append(1)
        else:
            dummies_dict['dummy_thriller'].append(0)

        if 'action' in genres:
            dummies_dict['dummy_action'].append(1)
        else:
            dummies_dict['dummy_action'].append(0)

        if 'romance' in genres:
            dummies_dict['dummy_romance'].append(1)
        else:
            dummies_dict['dummy_romance'].append(0)

        if 'crime' in genres:
            dummies_dict['dummy_crime'].append(1)
        else:
            dummies_dict['dummy_crime'].append(0)

        if 'family' in genres:
            dummies_dict['dummy_family'].append(1)
        else:
            dummies_dict['dummy_family'].append(0)

        if 'fantasy' in genres:
            dummies_dict['dummy_fantasy'].append(1)
        else:
            dummies_dict['dummy_fantasy'].append(0)

        if 'european' in genres:
            dummies_dict['dummy_european'].append(1)
        else:
            dummies_dict['dummy_european'].append(0)

        if 'scifi' in genres:
            dummies_dict['dummy_scifi'].append(1)
        else:
            dummies_dict['dummy_scifi'].append(0)

        other_genres = set(genres) - set(genres_top10)

        if len(other_genres) > 0:
            dummies_dict['dummy_OTHER_genres'].append(1)
        else:
            dummies_dict['dummy_OTHER_genres'].append(0)
            
    return dummies_dict