import requests

nameUrl = "https://playground.learnqa.ru/api/long_redirect"

reasponce = requests.post(nameUrl,allow_redirects = False)

if reasponce.status_code>=300 and reasponce.status_code<400:
    reasponce = requests.post(nameUrl, allow_redirects=True)
    size = len(reasponce.history)
    print('Редиректов :',str(size))
    print("Lasr url",reasponce.history[size-1].url)
else:
    print(f'У ссылки {nameUrl} редиректа нет')