import requests

UID = input('UID -> ')
p = requests.post('http://192.168.178.57:8000/anmelden/',data={'UID':UID})
print(p.content)
