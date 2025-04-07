import requests
from send_mail import send_mail

topic = input("Enter your topic: ")
api_key = '1956a9df3d884c4a9f5fb06d920f7aac'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-03-07&"
       "sortBy=publishedAt&"
       "apiKey=1956a9df3d884c4a9f5fb06d920f7aac"
       "&language=en")

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = "Subject: Today's news \n\n"

for article in content['articles'][:20]:
    if article.get('title') and article.get('description') and article.get('url'):
        body += f"{article['title']}\n\n {article['description']}\n{article['url']}\n\n"

body = body.encode('utf-8')
send_mail(message=body)

