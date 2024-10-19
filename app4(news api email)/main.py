import requests

api_key ="872930a61522403288309122e0c82b84"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=872930a61522403288309122e0c82b84"

request = requests.get(url)
content= request.json()

for article in content['articles']:
    print()
    print(article['title'])
    
    print(article['description'])
