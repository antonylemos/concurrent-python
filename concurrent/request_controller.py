import requests

def getCoffeeImageUrl():
  response = requests.get('https://coffee.alexflipnote.dev/random.json')
  print(response.text)
  return response.json()['file']