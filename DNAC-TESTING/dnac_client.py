#API Calls to Playground DNAC collecting data.

import requests

DNAC_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

def get_token():
    url = f"{DNAC_URL}/dna/system/api/v1/auth/token"
    resp = requests.post(url, auth=(USERNAME, PASSWORD), verify=False)
    resp.raise_for_status()
    return resp.json()["Token"]

def get_devices(token):
    headers = {"X-Auth-Token": token}
    url = f"{DNAC_URL}/dna/intent/api/v1/network-device"
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()["response"]

def get_topology(token):
    headers = {"X-Auth-Token": token}
    url = f"{DNAC_URL}/dna/intent/api/v1/topology/physical-topology"
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()["response"]
