#Client Credentials Grant method
import config
import http.client
import json

connection = http.client.HTTPSConnection('target.my.com')
headers = {"Content-type":"application/x-www-form-urlencoded"}
body='grant_type=client_credentials&client_id=%s&client_secret=%s'%(config.client_id, config.client_secret )

#POST
print("getting token")
connection.request('POST', '/api/v2/oauth2/token.json', body, headers)
print("token ok")
responsepost = connection.getresponse()
result=json.loads(responsepost.read().decode("utf-8"))
token=result['access_token']

#GET
print("getting stats")
connection._send_request('GET', '/api/v2/campaigns.json',[], {"Authorization":"Bearer " + token})

responseget = connection.getresponse()
result=json.loads(responseget.read().decode("utf-8"))
print(result['items'])
print(responseget.read())


