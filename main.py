import imp
import pyshorteners
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from apikey import *




while True:
    urlm = input("URL girin: ")

    if "https" and "https" not in urlm:
      urlm = "https://"+urlm 

    access_token = key
    metod = pyshorteners.Shortener(api_key=access_token)
    kisaltilmis_url = metod.bitly.short(urlm)  
    print('')
    print('|------------------------------------------|')
    print('')
    print(f"{Fore.GREEN}  Kısaltılmış URL: {kisaltilmis_url}") 
    print('')
    print('|------------------------------------------|')
    print('')
    
