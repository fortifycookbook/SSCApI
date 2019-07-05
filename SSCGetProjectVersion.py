import requests

auth_token='MDUxN2JjOTktMGFhMS00YTk3LTkyMmItZTQxYTVkMjFlNzlj'
hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
#data = { "applicationName": "ssscapp" }

url = 'http://localhost:8080/ssc/api/v1/projectVersions'

#response = requests.post(url, json=data, headers=hed)
response = requests.get(url, headers=hed)

print(response.json())