import requests
from send_mail import send_mail
api_key = '1956a9df3d884c4a9f5fb06d920f7aac'
url = ("https://newsapi.org/v2/everything?q=n8n&"
       "from=2025-03-07&sortBy=publishedAt&"
       "apiKey=1956a9df3d884c4a9f5fb06d920f7aac")

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n" + 2*"\n"

body = body.encode('utf-8')
send_mail(message=body)

