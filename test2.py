import requests
import json

url = "https://dev-com.roseltorg.ru/api.php"
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'br',
'Referer': 'https://dev-com.roseltorg.ru/',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
}
payload = {'_dc': '1465894725997'}
#Выполняю get запрос для получения и последующего использования значения параметра etpsid
#из полученного ответа(например) Set-Cookie: etpsid=NyqhlGexp7yeRoqOjhBSj2R5zDI; expires=Mon, 27-Nov-2062 20:32:10 GMT; Max-Age=1465985765; path=/; secure; HttpOnly
r=requests.get(url,headers=headers, params=payload)
print("1. Get api.php")
#etpsid id Cookie, need
etpsid = ""
for i in r.headers["Set-Cookie"]:
    if i != ";":
        etpsid +=i
    else:
        break
print("2. Split Cookie")
#при запросе api.php получили success = true
if r.json()["success"]:
    print("3. connect status success")
    #парсим modules
    #type r.json()["modules"] is <list>
    #type r.json()["modules"][0] is <dict>, if [1] then IndexError: list index out of range

    #get url in r.json()["modules"][0]
    print("4. get parametrs url")
    dop_url = r.json()["modules"][0]["url"]
    headers2={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'br',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://dev-com.roseltorg.ru/',
        'Content-Length': 79,
        'Cookie': etpsid,
        'Connection': 'keep-alive'
    }
    #POST: index.php(module,rctype)({"action":"Index","method":"index",)
    method_index = {"action":"Index",
                    "method":"index",
                    "data":None,
                    "type":"rpc",
                    "tid":2,
                    "token":""}
    #get auth_token. And data = json.dumps(data)
    #result>auth_token
    print("5. Post method index and get token")
    q = requests.post("https://dev-com.roseltorg.ru/"+dop_url,data=json.dumps(method_index),headers=headers2)
    token_session =json.loads(q.text)["result"]["auth_token"]
    #POST: index.php(module,rpctype)("action":"Index","method":"serverinfo",)
    '''data2 = {"action":"Index","method":"serverinfo","data":None,"type":"rpc","tid":16,"token": token_session}
    w = requests.post("https://dev-com.roseltorg.ru/"+dop_url,data=json.dumps(data2),headers=headers2)
    print(json.loads(w.text))'''
    method_login = {
            "action":"Authentication",
             "method":"login",
             "data":["demo","789456123",{"lock_ip":"on"}],
             "type":"rpc",
             "tid":3,
             "token":token_session
                    }
    print("Post method Authentication")
    e = requests.post("https://dev-com.roseltorg.ru/"+dop_url, data=json.dumps(method_login), headers = headers2 )
    if json.loads(e.text)["result"]["success"]:
        print(json.loads(e.text)["result"]["message"])
        method_index_login = {"action":"Index",
                    "method":"index",
                    "data":None,
                    "type":"rpc",
                    "tid":4,
                    "token":token_session}
        t = requests.post("https://dev-com.roseltorg.ru/"+dop_url, data=json.dumps(method_index_login), headers = headers2)
        print("6.Status code method index(login)",t.status_code)
        #serverinfo
        method_serverinfo={
            "action":"Index",
            "method":"serverinfo",
            "data":None,
            "type":"rpc",
            "tid":5,
            "token":token_session
        }
        y = requests.post("https://dev-com.roseltorg.ru/"+dop_url,headers=headers2,data=json.dumps(method_serverinfo))
        if json.loads(y.text)["result"]["success"]:
            print("7. Results of serverinfo True")
            method_list=[
                {
                    "action":"Procedure",
                    "method":"list",
                    "data":[{"sort":"id","dir":"DESC"}],
                    "type":"rpc","tid":6,"token":token_session
                },
                {
                "action":"Reference",
                 "method":"regionslist",
                 "data":[{"sort":"name","dir":"ASC"}],
                 "type":"rpc","tid":7,
                 "token":token_session
                 },
                {
                    "action":"Reference",
                    "method":"currency",
                    "data":None,
                    "type":"rpc",
                    "tid":8,
                    "token":token_session
                },
                {
                    "action":"Reference",
                    "method":"regionslist",
                    "data":[{"sort":"name","dir":"ASC"}],
                    "type":"rpc",
                    "tid":9,
                    "token":token_session
                }
            ]
            u =requests.post("https://dev-com.roseltorg.ru/"+dop_url,headers=headers2,data=json.dumps(method_list))
            print(json.loads(u.text))


