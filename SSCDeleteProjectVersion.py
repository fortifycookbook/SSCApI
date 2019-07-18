import requests
import json

auth_token='YTVmNGYyMGItNmU2MS00MTRmLWE4YjUtYmJmZmMwYTNjYmI2'

hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
data = { } 

for projectVersionId in (1,2,3,4,5,6,7,8,23,24,25):

   url = "http://localhost:8080/ssc/api/v1/projectVersions/" + str(projectVersionId)
   print(url)
   response = requests.delete(url, headers=hed)

   if ( response.status_code == 201):
      myprojectjson = response.json()
      print(myprojectjson["data"]["currentState"]["id"])
      print("_____________________________________________")
   else: 
      print("Error: " + str(response.status_code))
