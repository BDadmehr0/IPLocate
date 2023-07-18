from colorama import Fore as F; from colorama import Style as S
from requests import get


def Banner():
  v = get('https://raw.githubusercontent.com/BDadmehr0/IPLocate/master/lib/version?token=GHSAT0AAAAAACE6HCQBAXC3U4SQVX6E6AUCZFV2IXQ').text
  loc_st = f'''
    .@@@@
    @*  @@
     @@@@
      @@ '''
   
  ascii_banner = f'''{F.GREEN}{S.DIM}
 _ ___ _   __   ___ __ _____ ___  .@@@@
| | _,\ | /__\ / _//  \_   _| __| @*  @@
| | v_/ || \/ | \_| /\ || | | _|   @@@@
|_|_| |___\__/ \__/_||_||_| |___|   @@\n {S.BRIGHT}{F.BLUE}V{v}{S.NORMAL} BDadmehr0 | IP Address Lookup\n{F.YELLOW}'''

  return ascii_banner
