import json
import requests
import os
from colorama import Fore as F
from colorama import Style as S

class style:
    wrn = f'\n{F.WHITE}[{F.YELLOW}-{F.WHITE}]{F.RESET} ' # Warning ascii msg
    fil = f'\n{F.WHITE}[{F.RED}x{F.WHITE}]{F.RESET} ' # Fail ascii msg
    dne = f'\n{F.WHITE}[{F.GREEN}+{F.WHITE}]{F.RESET} ' # Done ascii msg

def get_latest_info_file():
    # Find all files with the pattern 'infoX.json' and get the latest X.
    existing_files = [f for f in os.listdir() if f.startswith("info") and f.endswith(".json")]
    if existing_files:
        last_file = max(existing_files)
        last_number = int(last_file.split("info")[1].split(".json")[0])
    else:
        last_number = 0

    # Create a new file name with an incremented X.
    new_file_name = f"info{last_number + 1}.json"
    return new_file_name

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

    # Get the latest info file name and save data to that file.
    info_file_name = get_latest_info_file()
    with open(info_file_name, 'w') as json_file:
        json_file.write(json_formatted_str)
    
    return style.dne + f'Done info saved to {info_file_name}\n'

# Test the main_APP function
if __name__ == "__main__":
    ip_address = "YOUR_IP_ADDRESS_HERE"
    result = main_APP(ip_address)
    print(result)
