import requests 

endpoint = "https://httpbin.org/status/200"

get_response = requests.get(endpoint)
print(get_response)
