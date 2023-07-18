from lib.banner import Banner
from lib.exct import main_APP
from colorama import Fore as F; from colorama import Style as S

banner = Banner()
class style:
    wrn = f'\n{F.WHITE}[{F.YELLOW}-{F.WHITE}]{F.RESET} ' # Warning ascii msg
    fil = f'\n{F.WHITE}[{F.RED}x{F.WHITE}]{F.RESET} ' # Fail ascii msg
    dne = f'\n{F.WHITE}[{F.GREEN}+{F.WHITE}]{F.RESET} ' # Done ascii msg

def main():
    while True:
        try:
            ip = str(input(f'{F.YELLOW}Pv4, IPv6 or Domain name ~$ '))
            print(style.dne+f'Done info saved to /lib/info.json\n')
            main_APP(ip=ip)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    print(banner)
    main()
