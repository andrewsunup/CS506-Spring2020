import time
import requests

url = "http://127.0.0.1:5000"
numRequests = 1000

for i in range(numRequests):
    response = requests.get(url)
    print(response.text)
    time.sleep(.01)
