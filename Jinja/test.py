import requests
name = 'Shivam'
request = requests.get(url='https://api.genderize.io', params={'name':name})

print(request.json()['gender'])