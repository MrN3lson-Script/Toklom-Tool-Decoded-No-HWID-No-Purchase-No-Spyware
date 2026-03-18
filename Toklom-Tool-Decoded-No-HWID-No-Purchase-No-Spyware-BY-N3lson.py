import colorama # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from colorama import Fore, Style # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import pystyle # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from pystyle import Colorate, Colors, Center, Anime, Write # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import requests # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import hashlib # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import platform # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import cpuinfo # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import psutil # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import sys # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import whois # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from selenium import webdriver # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from selenium.webdriver.common.by import By # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import time # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import os # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import phonenumbers # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import ctypes # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
import validators # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from phonenumbers import carrier, geocoder, timezone # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
from bs4 import BeautifulSoup # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def maximize_console_window(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    kernel32 = ctypes.windll.kernel32 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    user32 = ctypes.windll.user32 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    SW_MAXIMIZE = 3 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    hwnd = kernel32.GetConsoleWindow() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    user32.ShowWindow(hwnd, SW_MAXIMIZE) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def disable_resize_and_maximize(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    GWL_STYLE = -16 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    WS_SIZEBOX = 262144 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    WS_MAXIMIZEBOX = 65536 # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    hwnd = ctypes.windll.kernel32.GetConsoleWindow() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    style &= ~WS_SIZEBOX # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    style &= ~WS_MAXIMIZEBOX # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

disable_resize_and_maximize() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
maximize_console_window() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

intro = '''                                                                                                 
           __________  ________  ___  __    ___       ________  _____  ______      
          |\___   ___|\   __  \|\   \ \  \ |\  \     |\   __  \|\   _ \ \ _  \    
          \|___ \  \  \ \ \ \  \ \   \/  /|\ \  \    \ \  \ \  \ \  \ \__\ \  \   
               \ \  \  \ \ \ \  \ \    ___  \ \  \    \ \  \ \  \ \  \ |__| \  \  
                \ \  \  \ \ \ \  \ \   |\ \  \ \  \____\ \  \ \  \ \  \    \ \  \ 
                 \ \__\  \ \______\  \__|\ \__\ \_______\ \_______\ \__\    \ \__\    
                  \|__|   \|_______|\|__| \|__|\|_______|\|_______|\|__|     \|__|    
                                                                                            
                  Welcome in Toklom Tool. Please Press "Enter" for start this Tool           
                                       Developed: Mefoskvit | DECODED, No HWID, No Purchase, No Spyware: By N3lson                                  
''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(intro))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
Anime.Fade(Center.Center(intro), Colors.yellow_to_red, Colorate.Vertical, 0.045, True) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def check_Term_validity(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    if Term: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        return True # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    return False # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def generate_user_links(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    links = [] # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.minecraft.net/en-us/profile/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://steamcommunity.com/id/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.roblox.com/users/{Term}/profile') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.epicgames.com/site/en-US/home?lang=en-US#!/profile/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.reddit.com/user/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.quora.com/profile/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.stackabuse.com/users/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.kaggle.com/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.facebook.com/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.twitter.com/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.instagram.com/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.tiktok.com/@{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://t.me/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.whatsapp.com/profile/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.snapchat.com/add/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(f'https://www.discord.com/users/{Term}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    return links # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def print_valid_links(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    if not check_Term_validity(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print('Невалидное имя пользователя.', Colors.red, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        return # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    links = generate_user_links(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    for link in links: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if validators.url(link): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print(link, Colors.green, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print(link, Colors.red, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def ip_lookup(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    url = f'http://ip-api.com/json/{Term}' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    try: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        response = requests.get(url) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        data = response.json() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if data.get('status') == 'fail': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print('[!] Произошла ошибка : ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print(f'[!] {data['message']}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        info = '' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        for key, value in data.items(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            info = Write.Print(f'[+] {key} : ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print(f'{value}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        return info # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    except Exception as e: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print('[!] Произошла ошибка: ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'{str(e)}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def get_website_info(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    domain_info = whois.whois(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Домен -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.domain_name}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Зарегистрирован -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.creation_date}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Истекает -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.expiration_date}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Владелец -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_name}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Организация -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.dregistrant_organization}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Адрес -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_address}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Город -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_city}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Штат -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_state}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Почтовый индекс -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_postal_code}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] Страна -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.registrant_country}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print('[+] IP -> ', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    Write.Print(f'{domain_info.name_servers}\n', Colors.white, interval=0.005) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def search_banner(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    if platform.system() == 'Windows': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        ban_word = '''
        ,----,                                                    
      ,/   .`|                                                    
    ,`   .'  :              ,-.  ,--,                      ____   
  ;    ;     /          ,--/ /|,--.'|                    ,'  , `. 
.'___,/    ,'  ,---.  ,--. :/ ||  | :     ,---.       ,-+-,.' _ | 
|    :     |  '   ,'\ :  : ' / :  : '    '   ,'\   ,-+-. ;   , || 
;    |.';  ; /   /   ||  '  /  |  ' |   /   /   | ,--.'|'   |  || 
`----'  |  |.   ; ,. :'  |  :  '  | |  .   ; ,. :|   |  ,', |  |, 
    '   :  ;'   | |: :|  |   \ |  | :  '   | |: :|   | /  | |--'  
    |   |  ''   | .; :'  : |. \|  : |__'   | .; :|   : |  | ,     
    '   :  ||   :    ||  | ' \ \  | '.'|   :    ||   : |  |/      
    ;   |.'  \   \  / '  : |--';  :    ;\   \  / |   | |`-'       
    '---'     `----'  ;  |,'   |  ,   /  `----'  |   ;/           
                      '--'      ---`-'           '---'                                                                                                                                                          
''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(ban_word, Colors.yellow, interval=5e-19) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def clear_screen(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def phoneinfo(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    try: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        parsed_number = phonenumbers.parse(Term, None) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if not phonenumbers.is_valid_number(parsed_number): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            Write.Print('[!] Недействительный номер телефона', Colors.white, interval=5e-13) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            return # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        carrier_info = phonenumbers.carrier.name_for_number(parsed_number, 'en') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        country = phonenumbers.geocoder.description_for_number(parsed_number, 'en') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        region = phonenumbers.geocoder.description_for_number(parsed_number, 'ru') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        is_valid = phonenumbers.is_valid_number(parsed_number) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        is_possible = phonenumbers.is_possible_number(parsed_number) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        timezona = phonenumbers.timezone.time_zones_for_number(parsed_number) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'[+] Номер телефона: {formatted_number} ', Colors.white, interval=5e-08) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Страна: {country}', Colors.white, interval=5e-12) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Регион: {region}', Colors.white, interval=5e-12) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Оператор: {carrier_info}', Colors.white, interval=5e-11) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Активен: {is_possible}', Colors.white, interval=5e-12) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Валид: {is_valid}', Colors.white, interval=5e-14) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Таймзона: {timezona}', Colors.white, interval=5e-12) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Telegram: https://t.me/{Term}', Colors.white, interval=5e-12) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Whatsapp: https://wa.me/{Term}', Colors.white, interval=5e-10) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'\n[+] Viber: https://botapi.co/viber/{Term}', Colors.white, interval=5e-10) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    except Exception as e: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print('[!] Произошла ошибка -> ', Colors.white, interval=5e-08) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print(f'{str(e)}', Colors.white, interval=5e-09) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def Search(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    def make_request(Term): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        data = {'token': '7173216407:onr7iCG8', 'request': Term, 'limit': 100, 'lang': 'ru'} # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        url = 'https://server.leakosint.com/' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        response = requests.post(url, json=data) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        return response.json() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    data = make_request(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    for source in data['List']: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if source == 'No results found': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print('[!] Ничего не найдено') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            time.sleep(2) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print(f'\n[-] База данных: {source}') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        for item in data['List'][source]['Data']: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if str(item) not in set(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                continue # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            for key, value in item.items(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(f'[+] {key}: ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(f'[+] {value}\n') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    if 'No results found' not in data['List']: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

banner = '''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                                                                                 █
█         ███      ▄██████▄     ▄█   ▄█▄  ▄█        ▄██████▄    ▄▄▄▄████▄▄▄▄       █
█     ▀███████████▄ ███    ███   ███ ▄███▄ ███       ███    ███ ▄██▀▀▀████▀▀▀██▄     █
█        ▀███▀▀██ ███    ███   ███▀███▀   ███       ███    ███ ███   ███   ███     █
█         ███   ▀ ███    ███  ▄██▀███▄    ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███ ▀███▀▀████    ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███   ███   ███   ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███   ███   ███ ▄█ ███▄▄▄    ▄█ ███    ███ ███   ███   ███     █
█        ▄████    ▀██████▀    ███   ███ ██████████▀   ▀████████▀   ▀█   ███   ▀█      █
█                                                                                 █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                                   Version: 1.2.0                                █
█                                Изменить тему: themes                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                         █                          █                            █
█   [1] Поиск по Номеру   █  [4] Поиск по Паспорту   █  [7] Поиск по Домену       █
█   [2] Поиск по Почте    █  [5] Поиск по VIN        █  [8] Поиск по ИНН          █
█   [3] Поиск по IP       █  [6] Поиск по ФИО        █  [9] Поиск по СНИЛС        █
█                         █                          █                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                         █                          █                            █
█   [10] Поиск по Авто    █  [13] Поиск по Телеграм  █  [16] Поиск по Никнейму    █
█   [11] Поиск по VK ID   █  [14] Поиск по Инстаграм █  [17] Поиск по Адресу      █
█   [12] Поиск по Паролю  █  [15] Поиск по Facebook  █  [18] Глобальный Поиск     █
█                         █                          █                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
            ''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

mob_banner = '''
 _____     _    _                 
|_   _|   | |  | |                
  | | ___ | | _| | ___  _ __ ___  
  | |/ _ \| |/ / |/ _ \| '_ ` _ \ 
  | | (_) |   <| | (_) | | | | | |
  \_/\___/|_|\_\_|\___/|_| |_| |_|

[1] Поиск по Номеру   [4] Поиск по Паспорту   [7] Поиск по Домену       
[2] Поиск по Почте    [5] Поиск по VIN        [8] Поиск по ИНН          
[3] Поиск по IP       [6] Поиск по ФИО        [9] Поиск по СНИЛС     

[10] Поиск по Авто    [13] Поиск по Телеграм   [16] Поиск по Никнейму    
[11] Поиск по VK ID   [14] Поиск по Инстаграм  [17] Поиск по Адресу      
[12] Поиск по Паролю  [15] Поиск по Facebook   [18] Глобальный Поиск                              
''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

if platform.system() == 'Windows': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    print(Colorate.Horizontal(Colors.yellow_to_red, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

def selector(): # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    banner_sel = '''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                                                                                 █
█         ███      ▄██████▄     ▄█   ▄█▄  ▄█        ▄██████▄    ▄▄▄▄████▄▄▄▄       █
█     ▀███████████▄ ███    ███   ███ ▄███▄ ███       ███    ███ ▄██▀▀▀████▀▀▀██▄     █
█        ▀███▀▀██ ███    ███   ███▀███▀   ███       ███    ███ ███   ███   ███     █
█         ███   ▀ ███    ███  ▄██▀███▄    ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███ ▀███▀▀████    ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███   ███   ███   ███       ███    ███ ███   ███   ███     █
█         ███     ███    ███   ███   ███ ▄█ ███▄▄▄    ▄█ ███    ███ ███   ███   ███     █
█        ▄████    ▀██████▀    ███   ███ ██████████▀   ▀████████▀   ▀█   ███   ▀█      █
█                                                                                 █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                                   Version: 1.2.0                                █
█                                Изменить тему: themes                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                         █                          █                            █
█   [1] Поиск по Номеру   █  [4] Поиск по Паспорту   █  [7] Поиск по Домену       █
█   [2] Поиск по Почте    █  [5] Поиск по VIN        █  [8] Поиск по ИНН          █
█   [3] Поиск по IP       █  [6] Поиск по ФИО        █  [9] Поиск по СНИЛС        █
█                         █                          █                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█                         █                          █                            █
█   [10] Поиск по Авто    █  [13] Поиск по Телеграм  █  [16] Поиск по Никнейму    █
█   [11] Поиск по VK ID   █  [14] Поиск по Инстаграм █  [17] Поиск по Адресу      █
█   [12] Поиск по Паролю  █  [15] Поиск по Facebook  █  [18] Глобальный Поиск     █
█                         █                          █                            █
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
            ''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    mob_banner_sel = '''
 _____     _    _                 
|_   _|   | |  | |                
  | | ___ | | _| | ___  _ __ ___  
  | |/ _ \| |/ / |/ _ \| '_ ` _ \ 
  | | (_) |   <| | (_) | | | | | |
  \_/\___/|_|\_\_|\___/|_| |_| |_|
  
[1] Поиск по Номеру   [4] Поиск по Паспорту   [7] Поиск по Домену       
[2] Поиск по Почте    [5] Поиск по VIN        [8] Поиск по ИНН          
[3] Поиск по IP       [6] Поиск по ФИО        [9] Поиск по СНИЛС     

[10] Поиск по Авто    [13] Поиск по Телеграм   [16] Поиск по Никнейму    
[11] Поиск по VK ID   [14] Поиск по Инстаграм  [17] Поиск по Адресу      
[12] Поиск по Паролю  [15] Поиск по Facebook   [18] Глобальный Поиск                              
''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    select = Write.Input('[+] Выбери Опцию: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    if select == '1': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос (c +): ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по открытым данным!') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        phoneinfo(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по базам данных') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '2': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '3': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=6e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по открытым данным!') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        ip_lookup(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по базам данных') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '4': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-09) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '5': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = Write.Input('Continue? (y/n): ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '6': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = Write.Input('Continue? (y/n): ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '7': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по открытым данным!') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        get_website_info(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по базам данных') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '8': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '9': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '10': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '11': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '12': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '13': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '14': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '15': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '16': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по открытым данным!') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print_valid_links(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print('Выполняю поиск по базам данных') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(1) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '17': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == '18': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        search_banner() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Term = Write.Input('Введите запрос: ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Search(Term) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = input('Continue? (y/n): ') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == 'y': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == 'n': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner_sel))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    elif select == 'themes': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        theme = '''
            ╔═══════════════════════╗
            ║      1) Blue      ║ 
            ║═══════════════════════║
            ║      2) Red       ║
            ║═══════════════════════║
            ║     3) Violet     ║
            ║═══════════════════════║ 
            ║     4) Green      ║
            ║═══════════════════════║
            ║     5) Pink       ║
            ║═══════════════════════║
            ║   6) Orange (Def) ║
            ╚═══════════════════════╝
            ''' # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        print(Colorate.Horizontal(Colors.purple_to_blue, theme)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        choice = Write.Input('[+] Выбери Тему > ', Colors.red_to_yellow, interval=5e-06) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        if choice == '1': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.blue_to_white, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.blue_to_white, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == '2': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_white, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == '3': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.purple_to_blue, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == '4': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.green_to_white, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == '5': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_purple, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        elif choice == '6': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            if platform.system() == 'Android': # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('clear') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_yellow, mob_banner)) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
                print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(banner))) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            print('Такой темы не существует!') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            time.sleep(3) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
            selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
    else: # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        Write.Print('Такой опции не существует!', Colors.red_to_yellow, interval=5e-07) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        time.sleep(2) # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        os.system('cls') # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
        selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script

selector() # Decoded, No HWID, No Purchase, No Spyware, BY https://github.com/MrN3lson-Script
  