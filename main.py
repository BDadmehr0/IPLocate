from colorama import Fore as F; from colorama import Style as S

from lib.banner import Banner
banner = Banner()

class style:
    wrn = f'{F.WHITE}[{F.YELLOW}-{F.WHITE}]{F.RESET}' # Warning ascii msg
    fil = f'{F.WHITE}[{F.RED}x{F.WHITE}]{F.RESET}' # Fail ascii msg
    dne = f'{F.WHITE}[{F.GREEN}+{F.WHITE}]{F.RESET}' # Done ascii msg

def main():
    while True:
        try:
            ip = str(input('Pv4, IPv6 or Domain name ~$ '))
        except KeyboardInterrupt:
            exit()



if __name__ == '__main__':
    print(banner)
    main()
