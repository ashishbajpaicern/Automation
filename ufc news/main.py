import time
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.espn.com/mma/news"
data = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the news articles on the page
    articles = soup.find_all("p", string=lambda text: "UFC" in text)

    # Extract the text of each article and store them in data
    for article in articles:
        data.append(article.text)

    # dump data to json file
    with open("ufc_articles.json", "w") as f:
        json.dump(data, f)

    # load data from json file
    with open("ufc_articles.json", "r") as f:
        json_data = json.load(f)

    # print json data
    print(json.dumps(json_data, indent=4))

    # delay for 10 seconds before making the next request
    time.sleep(10)
