import requests

auth_token='YzcyYWE0NGEtYWEzOS00NjM0LTkyMmMtY2E0OWMwODc4YTcy'
#c72aa44a-aa39-4634-922c-ca49c0878a72
hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
data = { "artifactIds": [ 2 ] }
url = 'http://localhost:8080/ssc/api/v1/artifacts/action/purge'

response = requests.post(url, json=data, headers=hed)
#response = requests.get(url, headers=hed)
print(response)
#print(response.json())