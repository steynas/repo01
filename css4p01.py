# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:18:13 2024

@author: SteynAS
"""

import pandas as pd
from collections import Counter

file = 'movie_dataset.csv'
df = pd.read_csv(file)
print(df)
df.info()

# Print the maximum rating
max_rating = df.iloc[:, 8].max()
# Find the corresponding text in column 1 where the max value occurs in col 8
title_1 = df.loc[df.iloc[:, 8] == max_rating, df.columns[1]].values[0]

print("Maximum rating was:", max_rating)
print("Corresponding movie was:", title_1)

# Calculate the average of the revenue values in col 10
ave_revenue = df.iloc[:, 10].mean()
print("Average revenue of all movies was:", ave_revenue, "million")

# Filter the DataFrame to include only movies with years from 2015 to 2017
filtered_df = df[(df.iloc[:, 6] >= 2015) & (df.iloc[:, 6] <= 2017)]
# Calculate the average revenue for the filtered DataFrame
ave_revenue_filter = filtered_df.iloc[:, 10].mean()
print("Average revenue for movies released from 2015 to 2017:", ave_revenue_filter)

# Filter the DataFrame to include only movies with the year 2016
movies_2016 = df[df.iloc[:, 6] == 2016]
# Count the number of movies with the year 2016
num_movies_2016 = movies_2016.shape[0]
print("Number of movies released in the year 2016:", num_movies_2016)

# Filter the DataFrame to include only movies directed by "Christopher Nolan"
nolan_movies = df[df.iloc[:, 4] == "Christopher Nolan"]
# Count the number of movies directed by "Christopher Nolan"
num_nolan_movies = nolan_movies.shape[0]
print("Number of movies directed by Christopher Nolan:", num_nolan_movies)
# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan = nolan_movies.iloc[:, 8].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)

# Filter the DataFrame to include only movies with a rating of at least 8.0
high_rated_movies = df[df.iloc[:, 8] >= 8.0]
# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = high_rated_movies.shape[0]
print("Number of movies with a rating of at least 8.0:", num_high_rated_movies)

# Group the DataFrame by the year and calculate the average rating for each year
ave_rating_by_year = df.groupby(df.iloc[:, 6])[[df.columns[8]]].mean()
# Find the year with the highest average rating
year_highest_ave_rating = ave_rating_by_year.idxmax()[0]
print("Year with the highest average rating:", year_highest_ave_rating)

# Count the number of movies made in 2006 and 2016
num_movies_2006 = df[df.iloc[:, 6] == 2006].shape[0]
num_movies_2016 = df[df.iloc[:, 6] == 2016].shape[0]
# Calculate the percentage increase
percent_inc = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print("Percentage increase in number of movies made between 2006 and 2016:", percent_inc, "%")

# Split the actor names and create a list of all actors
all_actors = df.iloc[:, 5].str.split(',').explode()
# Count the occurrences of each actor
actor_counts = Counter(all_actors)
# Find the top 3 most common actors
top_3_actors = actor_counts.most_common(3)
print("Top 3 most common actors:")
for actor, count in top_3_actors:
    print(f"{actor}: {count} occurrences")
# Create a new DataFrame with actor names and corresponding ratings
actor_ratings_df = pd.DataFrame({'Actor': all_actors, 'Rating': df.iloc[:, 8]})
# Calculate the average rating for each actor
average_rating_per_actor = actor_ratings_df.groupby('Actor')['Rating'].mean()
# Find the top and bottom 3 actors based on their average rating
top_3_actors = average_rating_per_actor.nlargest(3)
bottom_3_actors = average_rating_per_actor.nsmallest(3)
print("Top 3 actors based on average rating:")
print(top_3_actors)
print("Bottom 3 actors based on average rating:")
print(bottom_3_actors)
    
# Split the genre names and create a list of all genres
all_genres = df.iloc[:, 2].str.split(',').explode()
# Count the number of unique genres
num_unique_genres = all_genres.nunique()
print("Number of unique genres in the dataset:", num_unique_genres)  

# Select the columns of interest for correlation analysis
selected_columns = df.iloc[:, [7, 8, 9, 10, 11]]  
# Calculate the correlation matrix
correlation_matrix = selected_columns.corr()
print("Correlation matrix:")
print(correlation_matrix) 

# Calculate the average rating for each director
average_rating_per_director = df.groupby('Director')['Rating'].mean()
# Find the director with the highest average rating
director_highest_rating = average_rating_per_director.idxmax()
print("Director with the highest average rating:", director_highest_rating)