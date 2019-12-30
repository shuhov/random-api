
import requests


def request_quote_api():
    url = 'https://api.quotable.io/random'
    return requests.get(url)


def get_random_quote(q):
    quotes = []
    for i in range(q):
        response = request_quote_api()
        quote = response.json()
        quotes.append(f"\"{quote['content']}\"\t{quote['author']}")
    return quotes
