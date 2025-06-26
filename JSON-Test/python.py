import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



DNAC_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"


def GetAPIToken():
    url = f"{DNAC_URL}/dna/system/api/v1/auth/token"
    response = requests.post(url, auth=(USERNAME, PASSWORD), verify=False)
    token = response.json()["Token"]
    return(token)


def GetRequest(token):
    headers = {"X-Auth-Token": token}
    url = f"{DNAC_URL}/dna/intent/api/v1/network-device"
    response = requests.get(url, headers=headers, verify=False)
    return (response.json())

def ParseJSON(response):
    #response is received as Python dict (Via .json())
    GoodLookingJSON = json.dumps(response, indent=2) 
    #print(GoodLookingJSON)
    #print(response["response"][0]["macAddress"])
    for device in response["response"]:
        print(device["hostname"],"runs",device["platformId"])
        print("with an ip adress of -",device["managementIpAddress"],"and uptime of",device["upTime"])

def RunAll():
    token = GetAPIToken()
    response = GetRequest(token)
    ParseJSON(response)



RunAll()