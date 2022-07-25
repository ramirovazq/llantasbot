import requests
import os

MYBOTTOKEN = os.getenv("MYBOTTOKEN")
url = f"https://api.telegram.org/bot{MYBOTTOKEN}/getUpdates"
print(url)
response = requests.get(url)
if response.ok:
  print(response)
  print(response.text)
else:
  print("something wrong")
  print(response.text)

