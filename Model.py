from random import choice


import requests
import pandas as pd
import mysql.connector

#This is a test --
#use jikan for scraping data for anime and then putting it into the database
#pandas - for reading and extracting for the database
#mysql - for the database
#find another api for books/movies

# this is me connecting to the API and printing out the responses from one of the sections ---------

# Fetch recommendations from the Jikan API
response = requests.get("https://api.jikan.moe/v4/recommendations/anime")

if response.status_code == 200:
    db = response.json()  # Convert the response to a dictionary

    # Loop through each recommendation in the data
    for recommendation in db['data']:
        # The recommendation might have multiple "entry" items
        if 'entry' in recommendation:
            for entry in recommendation['entry']:
                # Safely extract details from each entry
                anime_id = entry.get('mal_id', 'No ID')  # Use default 'No ID' if missing
                title = entry.get('title', 'No Title')  # Use default 'No Title' if missing
                image_url = entry.get('images', {}).get('jpg', {}).get('image_url', 'No Image')

                print(f"ID: {anime_id}, Title: {title}, Image: {image_url}")

        # Additional details outside "entry"
        content = recommendation.get('content', 'No Content')
        print(f"Content: {content}\n")

else:
    print(f"Failed to fetch recommendations: {response.status_code}")
# Was struggling with figuring out the API so most of this code is not my own, however i do understand it fully(i think)

