import requests

url = 'https://api-tradingview.herokuapp.com/v1/bot1'

r = requests.get(url).json()

for i in r[::-1]:
    if len(r) < 3:
        print('Done')
        exit()    
    print(i['symbol'])
    requests.delete('{}?symbol={}'.format(url,i["symbol"]))