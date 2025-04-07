import requests
from certifi import contents

api_key = '1956a9df3d884c4a9f5fb06d920f7aac'
url = ("https://newsapi.org/v2/everything?q=n8n&"
       "from=2025-03-07&sortBy=publishedAt&"
       "apiKey=1956a9df3d884c4a9f5fb06d920f7aac")

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
