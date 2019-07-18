import requests
import json

sscHostAndPortURLPrefix = "http://localhost:8080/ssc/api/v1"

auth_token='YTVmNGYyMGItNmU2MS00MTRmLWE4YjUtYmJmZmMwYTNjYmI2'
projectName = "Replace_With_Project_Name"
projectDescription = "Replace with Your Description" 
projectId = "2"

projectVersionName = "ReplaceWithVersionName003"
projectVersionDescription = "Replace with Project Version Description"


hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }

data = { "name": projectVersionName,  "description": projectVersionDescription, "project": { "name": projectName, "description": projectDescription, "issueTemplateId": "Prioritized-HighRisk-Project-Template", "id": projectId }, "issueTemplateId": "Prioritized-HighRisk-Project-Template" } 

url = sscHostAndPortURLPrefix + "/projectVersions"

response = requests.post(url, json=data, headers=hed)

if ( response.status_code == 201):

   myprojectjson = response.json()
   projectVersionId = myprojectjson["data"]["currentState"]["id"]
   print(projectVersionId)


   hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }

   data =  '{ "active": true, "committed": true }'

   url = sscHostAndPortURLPrefix + "/projectVersions/" + str(projectVersionId)

   response = requests.put(url, data, headers=hed)
   if ( response.status_code == 200):
      print("SUCCESS: " + str(response.json()))
   else:
      print("Error on Commit: " + str(response.status_code))    
else: 
   print("Error on Create: " + str(response.status_code))
