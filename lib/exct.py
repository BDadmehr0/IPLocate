import json
import requests
from colorama import Fore as F
from colorama import Style as S
from bs4 import BeautifulSoup

def main_APP(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    url = 'https://whatismyipaddress.com/ip/'+ip
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'html.parser')

    #Scraping Data
    div_text = str(soup.find("div",{"class":"ip-detail expanded"}).text.replace("\n","").strip())
    
    # ذخیره متن به عنوان یک فایل JSON
    data = {'ip_detail': div_text}
    with open('info.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)