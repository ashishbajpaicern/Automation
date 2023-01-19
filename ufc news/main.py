import time
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.espn.in/mma/"
data = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the news headlines on the page
    headlines = soup.find_all("h1", class_="headline")[
        :5]  # Get top 5 headlines

    # Extract the text of each headline and store them in data
    for headline in headlines:
        data.append(headline.text)

    # dump data to json file
    with open("ufc_news.json", "w") as f:
        json.dump(data, f)

    # load data from json file
    with open("ufc_news.json", "r") as f:
        json_data = json.load(f)

    # print json data
    print(json_data)

    # delay for 10 seconds before making the next request
    time.sleep(10)
