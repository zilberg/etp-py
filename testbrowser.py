import webbrowser
new = 2

url='https://dev-com.roseltorg.ru'
#webbrowser.open(url, new=new)
b = webbrowser.get('google-chrome')
b.open(url,new=new)
