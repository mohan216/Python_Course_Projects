# Import required libraries
import requests
from bs4 import BeautifulSoup
import datetime

d_day = datetime.date(1988,6,21)

print(d_day)

# Define the URL of the website you want to scrape
url = f"https://www.billboard.com/charts/hot-100/{d_day}"

print(url)

# Send an HTTP GET request to the URL and retrieve the HTML content
response = requests.get(url)
html = response.text


# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

song = soup.select('li ul li span', class_ ="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")

#li ul li span

#print(len(song))

print(song[0].text)

#print(soup)

#print(html)