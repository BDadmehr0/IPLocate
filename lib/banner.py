from colorama import Fore as F; from colorama import Style as S

def Banner():
  loc_st = f'''
    .@@@@
    @*  @@
     @@@@
      @@ '''
   
  ascii_banner = f'''
    _ ___ _   __   ___ __ _____ ___  
    | | _,\ | /__\ / _//  \_   _| __| 
    | | v_/ || \/ | \_| /\ || | | _|  
    |_|_| |___\__/ \__/_||_||_| |___| {loc_st}\n'''

  return ascii_banner
