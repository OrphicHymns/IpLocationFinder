import requests
from os import system
from ctypes import windll
import json



system('cls')
windll.kernel32.SetConsoleTitleW(f'IpLocationFinder | Brought by FallingAether')



logo = '''
  ___       _                    _   _             _____ _           _           
 |_ _|_ __ | |    ___   ___ __ _| |_(_) ___  _ __ |  ___(_)_ __   __| | ___ _ __ 
  | || '_ \| |   / _ \ / __/ _` | __| |/ _ \| '_ \| |_  | | '_ \ / _` |/ _ \ '__|
  | || |_) | |__| (_) | (_| (_| | |_| | (_) | | | |  _| | | | | | (_| |  __/ |   
 |___| .__/|_____\___/ \___\__,_|\__|_|\___/|_| |_|_|   |_|_| |_|\__,_|\___|_|   
     |_|                                                                         
'''
print(logo)
ip = input('''
           Enter the IP address you'd like to get information about:
           
           ''')

request = requests.get(f"http://ip-api.com/json/{ip}")

r = json.loads(request.text)

print(f'''
      Status: {r["status"]}
      Country: {r["country"]}
      Country Code: {r["countryCode"]}
      Region: {r["region"]}
      City: {r["city"]}
      ZIP: {r["zip"]}
      ISP: {r["isp"]}
      ''')
input()