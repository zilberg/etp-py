import json
import requests
data = {
    "action": "cron",
    "method": "procedures",
    "data": {},
    "type": "rpc",
    "tid":0,
    "token":"f4nj4VfaqX8ZSTV+LXWy2A"
}
r = requests.post("http://debug.178fz.chama.pro/indes.php?rpctype=direct&module=default", data=json.dumps(data))
print(r.text)