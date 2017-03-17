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
ETP = {
    'dev-com': 'https://dev-com.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-com': 'https://demo-com.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-178fz': 'https://dev-178fz.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-178fz': 'https://demo-178fz.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-com-ip': 'https://dev-com-ip.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-russianpost': 'https://demo-russianpost.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-rt': 'https://dev-rt.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-rt': 'https://demo-rt.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-rosgeo': 'https://dev-rosgeo.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-opk': 'https://demo-opk.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-vtb': 'https://dev-vtb.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'demo-vtb': 'https://demo-vtb.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-rt-ip': 'https://dev-rt-ip.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-atom2': 'https://dev-atom2.roseltorg.ru/indes.php?rpctype=direct&module=default',		
    'dev2-com': 'https://dev2-com.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'rushydro': 'https://dev-rushydro.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'dev-fkr': 'https://dev-fkr.roseltorg.ru/indes.php?rpctype=direct&module=default',
    'fsk':'https://fsk-ees.roseltorg.ru/indes.php?rpctype=direct&module=default'
}
EISENDPackets = {"action": "cron",
                  "method":"sendOOSPackets",
                  "data":{},
                  "type":"rpc",
                  "tid":5,
                  "token":"f4nj4VfaqX8ZSTV+LXWy2A"}


def derncronAll(ETP, EIS=True):
    r = requests.post(ETP, data=json.dumps(data))
    if EIS:
        r_eis = requests.post(ETP, data=json.dumps(EISENDPackets))
        return r.text, r_eis.text
    return r.text
print(derncronAll(ETP["rushydro"]))
input()
'''
area = input()
if area in ETP:
    print(derncronAll(ETP[area]))
    input()
else:
    print(area+' Данная площадка не найдена в доступном списке.')
    input()
'''
