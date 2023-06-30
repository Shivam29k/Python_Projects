import requests
from datetime import datetime

USERNAME = "shivamk"
TOKEN = "dcjbsdhbcjdsbhbvcascjk"
GRAPHID = "graph1"

# ---------------------------------------------> Creating a user <-------------------------------------
pixela_endpint = "https://pixe.la/v1/users"
user_prams = {
    "token" : TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpint, json=user_prams)
# print(response.text)


# ----------------------------------------> creating graph <--------------------------------------------
graph_endpoint = f"{pixela_endpint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name" : "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# -------------------------------------------> posting a pixel <------------------------------------------

today = datetime.now()
# yesterday = datetime(year=2023, month=6, day=29)
date = today.strftime("%Y%m%d")
add_pixel_endpoint = f"{pixela_endpint}/{USERNAME}/graphs/{GRAPHID}"

add_pixel_prams = {
    "date": date,
    "quantity": input("How may Kilometers you cycled today ? "),
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_prams, headers=headers)
print(response.text)

# ----------------------------------------> updating pixel <------------------------------------------------

update_pixel_endpoint = f"{pixela_endpint}/{USERNAME}/graphs/{GRAPHID}/{date}"

update_pixel_prams = {
    "quantity":"8"
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_prams, headers=headers)
# print(response.text)

# -----------------------------------------> deleting a pixel <----------------------------------------------

delete_pixel_endpoint = f"{pixela_endpint}/{USERNAME}/graphs/{GRAPHID}/{date}"
# response = requests.delete(url=update_pixel_endpoint,headers=headers)
# print(response.text)
