import requests

def getCoffeeImageUrl():
  response = requests.get('https://coffee.alexflipnote.dev/random.json')
  return response.json()['file']