'''Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''

import json
import requests
import time
import pprint
from dnacentersdk import DNACenterAPI
from dnacentersdk.exceptions import ApiError

#Suppressing warning due to lack of certificate verificaton in https connection
requests.packages.urllib3.disable_warnings() 

#open cred file for dnac connection establishment
with open('cred.json') as json_file:
    data = json.load(json_file)


#Create DNA api object "dnac"
dnac = DNACenterAPI(base_url=data['dnacurl'],
username=data['username'],password=data['passwd'], verify=False)

#Get All Devices
devs=dnac.devices.get_device_list()
devlist=[x['id'] for x in devs['response']]

#Start task to create configuration files
mypayload={"deviceId":devlist,"password":"Cisco123#"}
headers={"content-type" : "application/json"}
url="/dna/intent/api/v1/network-device-archive/cleartext"
response = dnac.custom_caller.call_api(method="POST", resource_path=url, headers=headers, json=mypayload)

#Wait for task to complete and then retrieve task details
time.sleep(5)
mytaskid=response["response"]["taskId"]
response = dnac.task.get_task_by_id(mytaskid)

#Parse response to get URL and call the URL to download zip file of configs
url =response["response"]["additionalStatusURL"]
response = dnac.custom_caller.call_api(method="GET", resource_path=url, original_response=True)

#Response is in bytes, write bytes to file.
with open("dnacconfall.zip","wb") as r:
    r.write(response.content)

