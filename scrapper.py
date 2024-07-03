from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
import time
import sys


# Function to check time difference and end program if program run for too long
def check_time_passed():
    current_time = datetime.now()
    time_difference = current_time - start_time
    if time_difference > timedelta(minutes=1):
        print("\nKilling script!!")
        sys.exit()  # Terminate the program
    return 

def fetch_parse_webpage(url, key):
    #check time passes
    check_time_passed()

    # Fetch webpage content
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # finding all <p> tags
    paragraphs = soup.find_all('p')

    #check time passes
    check_time_passed()

    for paragraph in paragraphs:
        if any(keyword in paragraph.text for keyword in key.split(',')):
            print("\n->", paragraph.text)


def link_generator(url, key):
    #check time passes
    check_time_passed()

    # Fetch webpage content
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags (links) in the webpage
    links = soup.find_all('a')

    #check time passes
    check_time_passed()

    for link in links:
      href = link.get('href')
      if href and  href.startswith('http'):
        fetch_parse_webpage(href, key)



# Get the current time
start_time = datetime.now()
# Print the current time
print("=========================================")
print("Start Time:", start_time)
print("=========================================\n\n")


# Enter relevent news outlets:
urls = [
    'https://timesofindia.indiatimes.com/news', 'https://www.ndtv.com/',
    'https://indianexpress.com/',
    'https://timesofindia.indiatimes.com/home/headlines',             
     'https://scroll.in/',
    'https://www.indiatoday.in/', 'https://www.hindustantimes.com/',
    'https://www.thehindu.com/', 'https://thewire.in/',
    'https://www.india.gov.in/news_lists?a840680091'
]
key = 'India'
keywords = key.split(',')
for keyword in keywords:
    for url in urls:
        fetch_parse_webpage(url, keyword)
        link_generator(url, keyword)
