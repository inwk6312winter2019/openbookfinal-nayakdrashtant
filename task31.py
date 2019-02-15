import requests
import json
def GetToken():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data['username'] = "devnetuser"
    data['password'] = "Cisco123!" 
    data= json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    return response.json()['response']['serviceTicket']

def getNetworkData():
    token = GetToken()
    #print(token)
    mydict = dict()
    url = "https://sandboxapicem.cisco.com/api/v1/host"
    headers = {'Content-type': 'application/json','X-Auth-Token':token}
    response = requests.get(url,headers=headers,verify=False)
    response =  response.json()['response']
    for r in response:  
      #  for i in r:
        ip = r["hostIp"]
        ip = tuple(ip)
        mydict[ip] = r["hostMac"]

    print(mydict)

getNetworkData()

