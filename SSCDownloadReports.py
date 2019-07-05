import requests
import sys
token = sys.argv[1]
report_id = 1

auth_token='MDUxN2JjOTktMGFhMS00YTk3LTkyMmItZTQxYTVkMjFlNzlj'
hed = {'Authorization': 'FortifyToken ' + auth_token }

url = 'http://localhost:8080/ssc/transfer/reportDownload.html?mat=' + token + '&id=' + str(report_id)

response = requests.get(url, headers=hed)
# If the HTTP GET request can be served
if response.status_code == 200:
    local_file_path = "demofile.pdf"
    # Write the file contents in the response to a file specified by local_file_path
    with open(local_file_path, 'wb') as local_file:
        for chunk in response.iter_content(chunk_size=128):
            local_file.write(chunk)

  
