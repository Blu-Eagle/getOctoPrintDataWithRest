import requests


url='http://192.168.1.30/api/job?apikey=D643A7C8C0E24575B84C7A55D0313C79'
data = requests.get(url, headers={'accept': 'application/json'})
#print(data.json())
data = data.json()
print(f"status: {data['state']} -> progress: {int(data['progress']['completion']*100)/100}%")


url='http://192.168.1.30/api/printer?apikey=D643A7C8C0E24575B84C7A55D0313C79'
data = requests.get(url, headers={'accept': 'application/json'})
#print(data.json())
data = data.json()
print(f"bed temp: {data['temperature']['bed']['actual']}   nozzle temp: {data['temperature']['tool0']['actual']} ")
