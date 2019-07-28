import requests



auth_token='Y2Y4MzQ3Y2EtYzY3NS00MjhkLTlhYjUtZDZiOTkxMjVhYmZh'
findVersionName = "*demo*"

hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }

url = 'http://localhost:8080/ssc/api/v1/projectVersions?q=name:' + findVersionName

response = requests.get(url, headers=hed)
rawjson = response.json()

projectname = rawjson['data'][0]['project']['name']
projectversionId = rawjson['data'][0]['id']

print(str(projectversionId) +  "-" + projectname)

url2 = 'http://localhost:8080/ssc/api/v1/projectVersions/' + str(projectversionId) + '/issues?filterset:BH Security Auditor&limit=-1&start=0&showhidden=false&showremoved=false&showsuppressed=false&showshortfilenames=false'

response2 = requests.get(url2, headers=hed)
rawjson = response2.json()

totalissues = str(len(rawjson['data']))

print("total Issues: " + totalissues)

criticals = [ ]
highs = [ ]
meds = [ ]
lows = [ ]
others = [ ]
for issue in rawjson['data']:
    if issue['friority'] == "Critical":
       criticals.append(issue['issueName'])
    elif issue['friority'] == "High":
       highs.append(issue['issueName'])
    elif issue['friority'] == "Medium":
       meds.append(issue['issueName'])
    elif issue['friority'] == "Low":
       lows.append(issue['issueName'])
    else:
       others.append(issue['issueName'])   

print("Criticals: " + str(len(criticals)))
print("High: " + str(len(highs)))
print("Med: " + str(len(meds)))
print("Low: " + str(len(lows)))
print("Others: " + str(len(others)))


