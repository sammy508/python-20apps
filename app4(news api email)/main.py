import requests
from send_email import send_email

api_key ="872930a61522403288309122e0c82b84"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=872930a61522403288309122e0c82b84"

request = requests.get(url)
content= request.json()

body = ""
for article in content['articles'][:20]:

    if article['title'] is not None:
        body = "Subject: Todays's news"+body + article['title']+ article['description'] + "\n"+article['url']+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)        
   

