import json
import requests

from colorama import Fore as F; from colorama import Style as S
from bs4 import BeautifulSoup

def main_APP(ip):
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga_DHL4YQEJFS=GS1.1.1694805215.2.1.1694806225.59.0.0; _ga=GA1.2.1062077168.1694434314; _omappvp=xi6c0vSDcfgZKPHgT6QrE0288vBdZAYI6KtI7eKdyVFAcKeI1WhZx7csrdirIoBh25Zc5H9aDcJrFFdnD3rpfNEcaaMzit4p; _clck=5qnjkx|2|fex|0|1349; __qca=P0-1824596116-1694434321765; _pbjs_userid_consent_data=3524755945110770; cookie=533a36d5-bd14-44da-a945-ce610cb37a1b; __gads=ID=fa4a869be6ae4227-226283106ede0005:T=1694434354:RT=1694806174:S=ALNI_MZwxpG70c_dr9iSBL15VABA4dXOSQ; __gpi=UID=00000c9fdb7ba745:T=1694434354:RT=1694806174:S=ALNI_MYeBTxxrnMES1qzQQSIQSYly7wnYA; cto_bundle=G-HIsl84T04lMkJLMzlqVjRxQXhraGhPS0tUSWZmM242RUc1WUJFOUhPUDRyYmZUSENmQ2tmWmRxeWFHYzlTWTJaJTJGblptaWN3bE1xQ0dvSEtBd2dmUVhwTWdRalAlMkZacFpITHNTRVk3Sm9YaDdyRm9UbUpmb3QzM08yVHIxM2VUYmxzd3dBREQ2NCUyQjZJWEc0RW1HSjA3dFBkenV0emlIMFZOS3FTTDNtbUVOM2xNRTlMdyUzRA; cto_bidid=a3CiwF9MYW9UN3VNTjlZdXBnTUZISHFlJTJGYnlBcnYyY0pyZFMya2pnMTVpdEJ3eVVHaGklMkZFZW5HZUhnbkNDTVBsSlZJTkhjMGVtd3d1Zm1XOGJvaThZVGZGYVhTYVdsNDVUOEdYSlhxbVI0eXNaV3g1M3h6R0JIUHdlUjZmbzl0c01TbHg; cto_dna_bundle=00MzfF9QUzlFVlN0YXlsWGJrUDdyVnhxWnkzWkN2U0ZXOUdOdjE5UUdlM2VEQ3FYdFlMZnhDZ3RZVlluTUhDJTJCbHNDSEpuU2NuQkhGemQwOHdJOTh5MzJrS2JRJTNEJTNE; pt=c8d50fd8d99794e6af65fd793eac87f9; __cf_bm=9cQjhKOgXevj8EGaCiW8OjxEom40rkKAsCnOIEQ39Zg-1694806180-0-AdE7YCfuYgfWpHLOIKLUNhBrCDZlmwmZSXbrBwa+fJWPluzEnolOUncZXuSuwV9VLvR0yxZYXgelweKiRbxpfFc=; _gid=GA1.2.1721439361.1694805227; _cc_id=3b0c145a50cce2d2f28db274fe821346; panoramaId_expiry=1695410067287; panoramaId=3198e903f40daf19bb458a188c9416d53938d90c0ba404ca5624377d86b42107; panoramaIdType=panoIndiv',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }



    response = requests.get(f'https://whatismyipaddress.com/ip/{ip}', headers=headers)
    div_element = BeautifulSoup.soup.find('div', class_='ip-detail expanded')
    text = div_element.text.strip()  # حذف فاصله‌های اضافی از متن
    
    # json_object = json.loads(response)
    # json_formatted_str = json.dumps(json_object, indent=2)

    #open and read the file after the appending:
    with open('info.json', 'w') as json_file:
        json_file.write(text)
