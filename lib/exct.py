import json
import requests

from colorama import Fore as F; from colorama import Style as S

class style:
    wrn = f'\n{F.WHITE}[{F.YELLOW}-{F.WHITE}]{F.RESET} ' # Warning ascii msg
    fil = f'\n{F.WHITE}[{F.RED}x{F.WHITE}]{F.RESET} ' # Fail ascii msg
    dne = f'\n{F.WHITE}[{F.GREEN}+{F.WHITE}]{F.RESET} ' # Done ascii msg

def main_APP(ip):
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://ipbase.com',
        'Connection': 'keep-alive',
        'Referer': 'https://ipbase.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    params = {
        'apikey': 'sgiPfh4j3aXFR3l2CnjWqdKQzxpqGn9pX5b3CUsz',
        'ip': f'{ip}',
    }


    response = requests.get('https://api.ipbase.com/v2/info', params=params, headers=headers).text
    json_object = json.loads(response)
    json_formatted_str = json.dumps(json_object, indent=2)

    #open and read the file after the appending:
    with open('info.json', 'w') as json_file:
        json_file.write(json_formatted_str)
        print(style.dne+f'Done info saved to info.json\n')
