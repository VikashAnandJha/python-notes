import requests
import time
import os
import random

from bs4 import BeautifulSoup


def getScore():
    # URL of the cricket World Cup page
    random_integer = random.randint(1, 1000000000000)

    url = "https://www.espncricinfo.com/series/new-zealand-a-in-australia-2023-1392778/australia-a-vs-new-zealand-a-1st-unofficial-test-1392782/live-cricket-score?random=" + \
        str(random_integer)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all match elements
        data_21_4_ov = soup.find(
            'span', class_='ds-text-compact-s').text.strip()
        score_147 = soup.find('strong', class_='ds-text-typo-mid3').text
        score_81_1 = soup.find('strong', class_='').text

        print("Data  :", data_21_4_ov)
        print("Score :", score_147)
        print("Score :", score_81_1)

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)


while True:
    os.system('clear')
    getScore()
    time.sleep(5)  # Sleep for 5 seconds
