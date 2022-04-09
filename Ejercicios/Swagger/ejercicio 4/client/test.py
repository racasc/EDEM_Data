import requests


print("#######################")
print("ONBOARDING")
print("#######################")
data ={
  "image": "value",
  "ip": "1.2.3.4",
  "name": "Pedro"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url = 'http://localhost:8080/swagger-ui/onboarding', json = data, headers=headers)
print(r)
data ={
  "image": "value",
  "ip": "5.6.7.8",
  "name": "Juan"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url = 'http://localhost:8080/swagger-ui/onboarding', json = data, headers=headers)
print(r)


print("#######################")
print("LIST PLAYERS")
print("#######################")

r = requests.get('http://localhost:8080/swagger-ui/getallplayers')
print(r.json())
print(r)


print("#######################")
print("NEW GAME")
print("#######################")

r = requests.get('http://localhost:8080/swagger-ui/newgame')
print(r.json())
print(r)


print("#######################")
print("NEW CARD")
print("#######################")

data = {}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url = 'http://localhost:8080/swagger-ui/nextcard',json=data, headers=headers)
print(r)