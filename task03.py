import requests
import json
def geticket():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data["username"] = "devnetuser"
    data["password"] = "Cisco123!"
    data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    print(response.json()['response']['serviceTicket'])

geticket()

