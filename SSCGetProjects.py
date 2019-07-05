import requests

auth_token='NDUyY2ZkMTYtZjc3ZC00OWRkLWEyOTctYTg4MjM0OTRiNGM3'
hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
data = { "applicationName": "string" }

url = 'http://localhost:8080/ssc/api/v1/projects'

#response = requests.post(url, json=data, headers=hed)
response = requests.get(url, headers=hed)

print(response)
print(response.json())