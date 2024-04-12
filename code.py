import requests

print("----- Jokes Generator -----")
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {"Accept":"application/json"})

if response.ok :
  data = response.json()
  joke = data.get("joke")
  print("Joke:",joke)
  
else:
  print("Error fetching the data , try again!! ")
