#!/usr/bin/python
"""
Run the CLI with python
Enter command:
    get <key>s
    put <key> <value>
    exit
"""
import requests
import json

base_url = "http://localhost:8080/keyvaluestore"
session = requests.Session()
msg = """
Enter command:
    get <key>
    put <key> <value>
    exit
>>> """

while True:
    command = raw_input(msg)
    if command:
        out = command.split()
        if out[0] == 'get' and len(out) == 2:
            url = base_url + '/' + out[1]
            resp = session.get(url, verify=False)
            if resp.status_code in [200, 202]:
            	print (resp.text)
            else:
            	print ('GET failed - ' + resp + ' - ' + resp.text)
        elif out[0] == 'put' and len(out) == 3:
            headers = {'content-type': 'application/json'}
            json_data = '{"key" : "' + out[1] + '", "value" : "' + out[2] +'"}'
            resp = session.put(base_url, data=json_data	, verify=False, headers=headers)
            if resp.status_code in [200, 202]:
            	print (resp.text)
            else:
            	print ('PUT failed - ' + resp + ' - ' + resp.text)
        elif out[0].lower() == "exit":
        	session.close()
        	break
        else:
            print ('Invalid command')




