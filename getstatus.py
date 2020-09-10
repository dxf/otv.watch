import requests
import auth
headers = {
    'Authorization': auth.auth,
    'Client-ID': 'lr8ok7604ketqe6qq5kq1bdieibcpu',
}

params = (
('user_login', 'pokimane'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:
    poki = False
else:
    poki = True
print(j)

params = (
('user_login', 'scarra'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:     
    scarra = False
else:
    scarra = True

params = (
('user_login', 'lilypichu'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:
    lily = False
else:
    lily = True

params = (
('user_login', 'yvonnie'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:
    yvonne = False
else:
    yvonne = True

params = (
('user_login', 'monstercat'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:
    monstercat = False
else:
    monstercat = True

params = (
('user_login', 'michaelreeves'),
)
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
j = response.json()
if len(str(j)) < 100:
    mykull = False
else:
    mykull = True