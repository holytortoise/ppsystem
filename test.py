import requests

UID = input('UID -> ')
p = requests.post('http://192.168.0.8:8000/anmelden/',data={'UID':UID})
print(p.content)
