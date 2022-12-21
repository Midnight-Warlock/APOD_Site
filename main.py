import streamlit as sl
import requests

# Prepare API key and API url
API_KEY = "hBtqNgXk3FMeX5kwaiBJApHIgMchsnRybd8PW47b"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&hd=True"

# Get the request data as dictionary
response = requests.get(url)
data = response.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["hdurl"]
explanation = data["explanation"]

# Download the image
image_filepath = "image.jpg"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

sl.title(title)
sl.image(image_filepath)
sl.write(explanation)
