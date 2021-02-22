import requests

def quote():
  url = "http://breaking-bad-quotes.herokuapp.com/v1/quotes"
  response = requests.get(url)
  quote = response.json()[0]['quote']
  author = response.json()[0]['author']
  return f"{quote} - {author}"
