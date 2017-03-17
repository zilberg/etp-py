import requests
'''
#STEP 1
r1 = requests.get("https://dev-com.roseltorg.ru/")
if r1.status_code == 200:
    t = r1.headers
    setcook = dict()
    for i in t["Set-Cookie"].split(";"):
        p=i.split("=")
        if len(p):
            p.append(None)
        setcook[p[0]]=p[1]
else:
    print("error get site, step1, status code ",r1.status_code)
headers = {'Cookies':"etpsid="+setcook["etpsid"]}'''
auth = {
    "action":"Authentication",
    "method":"login","data":["demo","789456123",{"lock_ip":"on"}],
    "type":"rpc",
    "tid":13,
    "token":"bT6lgW1735a8qdsZwvyGdA"}
r2 = requests.post("https://dev-com.roseltorg.ru/index.php?rpctype=direct&module=default", auth)
print(r2.text)