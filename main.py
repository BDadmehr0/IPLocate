from lib.banner import Banner
from lib.exct import main_APP
from colorama import Fore as F; from colorama import Style as S


def main():
    
    try:
        ip = str(input(f'{F.YELLOW}Pv4, IPv6 or Domain name ~$ '))
        print(main_APP(ip=ip))
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    banner = Banner()
    print(banner)
    main()
