from colorama import Fore as F; from colorama import Style as S
from requests import get

def Banner():
  v = get('https://')
  loc_st = f'''
    .@@@@
    @*  @@
     @@@@
      @@ '''
   
  ascii_banner = f'''
 _ ___ _   __   ___ __ _____ ___  .@@@@
| | _,\ | /__\ / _//  \_   _| __| @*  @@
| | v_/ || \/ | \_| /\ || | | _|   @@@@
|_|_| |___\__/ \__/_||_||_| |___|   @@\n V.{v} BDadmehr0 | IP Address Lookup'''

  return ascii_banner
