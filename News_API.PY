                                             NEWS API

#Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
#Go to: https://newsapi.org/ and explore the various options to build you application




SOLUTION:

import requests

query = input("What type of news are you interested in?: ")
# Set up the request parameters
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',
    'apiKey': '52e5eb7afc1f45f5934fe377d11a9d04'
}

# Send the request to the API endpoint
response = requests.get(url, params=params)

# Parse the response JSON data
data = response.json()

# Print the news articles
for article in data['articles']:
    print(article['title'])
    print(article['description'])
    print(article['url'])
    print()
    print("--------------------------------------")

