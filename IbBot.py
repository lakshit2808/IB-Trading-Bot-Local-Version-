from time import sleep
import pyautogui
import os
import requests
import psutil
from win10toast import ToastNotifier


scriptPath = './app.exe'
Ib_Trader_Token = '5478898420:AAFOevsAx7vdeVRybBTPDHN8wsAbnKsxeWI'

def StatusCode():
    return requests.get('https://localhost:5000/v1/api/portfolio/accounts', verify= False).status_code

def BotStatus():
    url = 'https://tradingviewsignal.herokuapp.com/v1/bot1' + '/botstatus'
    res = requests.get(url).json()[0]['botstatus']
    return res  

def AlreadyRunning():
    return "app.exe" in (p.name() for p in psutil.process_iter())

toast = ToastNotifier()
toast.show_toast("IB Trading Bot", "IB Trading Bot is running", duration=5)
os.chdir(r'D:/Desktop/Bots/C - Bot/IB Bot/Bot_Device') ## Change
print('Script Started')

while True:
    if StatusCode() == 200 and AlreadyRunning() is False:
        os.system("start powershell.exe")
        sleep(2)
        pyautogui.write(scriptPath)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.write('exit()')
        pyautogui.press('enter')     
    else:
        print('Please Login to Client Portal API')
        sleep(10)    
    