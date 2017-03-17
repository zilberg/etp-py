import requests
#GET api.php
g = requests.get("https://dev-com.roseltorg.ru/api.php?_dc=1465555402759")
if g.status_code ==200:
    print(g.headers)
    print(g.text)
else:
    print("Error GET ",g.status_code)
#print(type(g.status_code))
token=""

#Если получили token
#POST authentication
Auth = {
  "action": "Authentication",
  "method": "login",
  "data": [
    "demo",
    "789456123",
    {
      "lock_ip": "on"
    }
  ],
  "type": "rpc",
  "tid": 45,
  "token": token
}
url = "https://dev-com.roseltorg.ru/index.php?rpctype=direct&module=default"
r = requests.post(url,Auth)
if r.status_code == 200:
    '''f = open("test.html","w")
    f.write(r.text)'''
    print(r.text)
else:
    print(r.status_code)
