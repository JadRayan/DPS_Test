import requests

url = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge'

data = {
    'github': 'https://github.com/JadRayan/DPS_Test',
    'email': 'j.r.elhalabi@gmail.com',
    'url': 'https://dps-app-halabi-v2.herokuapp.com/',
    'notes': 'NOTES' # optional
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
