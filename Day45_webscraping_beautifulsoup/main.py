# Import required libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://news.ycombinator.com/"

# Send an HTTP GET request to the URL and retrieve the HTML content
response = requests.get(url)
html = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find an element by tag and class
element = soup.find_all('span', class_='titleline')

print(element[0].text)

print(element[0].getText)

print(len(element))

