import requests
import sys

def AccountId():
    return requests.get('https://localhost:5000/v1/api/portfolio/accounts', verify= False).json()[0]['accountId']

def ConId(symbol):
    r = requests.get(f'https://localhost:5000/v1/api/trsrv/stocks?symbols={symbol}', verify= False)
    return r.json()[symbol][0]['contracts'][0]['conid']

def PlaceOrder(side, symbol, quantity):
    accountid = AccountId()
    conid = ConId(symbol)
    params = {"orders": [{
        "conid": conid,
        "secType": "STK",
        "orderType": "MKT",
        "quantity": quantity,
        "side": side,
        "tif": "GTC"
    }]}
    return requests.post(f'https://localhost:5000/v1/api/iserver/account/{accountid}/orders', json= params).json()    


def response():
    return requests.get('https://tradingviewsignal.herokuapp.com/v1/bot1/placeorder').json()
    
def BotStatus():
    url = 'https://tradingviewsignal.herokuapp.com/v1/bot1' + '/botstatus'
    res = requests.get(url).json()[0]['botstatus']
    return res    

print('Bot Started!')

while True:
    if BotStatus() is True:
        if len(response()) > 0:
            if response()[-1]['signal'] == 'BUY':
                print(f'Ticker Name: {response()[-1]["ticker"]} \nSignal: {response()[-1]["signal"]} \nQuantity: {response()[-1]["qnty"]}')
                print(PlaceOrder('BUY', response()[-1]['ticker'], response()[-1]['qnty']))
                requests.delete(f'https://tradingviewsignal.herokuapp.com/v1/bot1/placeorder?tickerName={response()[-1]["ticker"]}')

            elif response()[-1]['signal'] == 'SELL':
                print(f'Ticker Name: {response()[-1]["ticker"]} \nSignal: {response()[-1]["signal"]} \nQuantity: {response()[-1]["qnty"]}')
                print(PlaceOrder('SELL', response()[-1]['ticker'], response()[-1]['qnty']))
                requests.delete(f'https://tradingviewsignal.herokuapp.com/v1/bot1/placeorder?tickerName={response()[-1]["ticker"]}')  
    else:
        print('Shutting Down the Bot...')
        sys.exit(0)