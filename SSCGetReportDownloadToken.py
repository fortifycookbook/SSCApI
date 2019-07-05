import requests
import subprocess

auth_token='MDUxN2JjOTktMGFhMS00YTk3LTkyMmItZTQxYTVkMjFlNzlj'
hed = {'Authorization': 'FortifyToken ' + auth_token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
data = { "fileTokenType": "REPORT_FILE"}

url = 'http://localhost:8080/ssc/api/v1/fileTokens'

response = requests.post(url, json=data, headers=hed)
#response = requests.get(url, headers=hed)

print(response)
print(response.json())
res1 = response.json()
print("Token:(" + str(res1["data"]["token"]) + ")")
token = str(res1["data"]["token"])

subprocess.call("python3 SSCDownloadReports.py \"" + token + "\"", shell=True)
#/transfer/reportDownload.html?mat=7e8d912e-2432-6496-3232-709b05513bf2&id=<Saved_Report_Id>