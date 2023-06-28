import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

logitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (logitude, latitude)
print(iss_position)










# Different response code meanings:
# 1XX = Hold on
# 2XX = Here you go
# 3XX = GO Away (you dont have permission)
# 4XX = You screwed Up (Problem from user end)
# 5XX = Devloper Screwed Up
# -----> httpstatuses.com
