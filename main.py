from colorama import Fore as F; from colorama import Style as S
import sys

class style:
    wrn = '{F.WHITE}[{F.YELLOW}-{F.WHITE}]{F.RESET}' # Warning ascii msg
    fil = '{F.WHITE}[{F.RED}x{F.WHITE}]{F.RESET}' # Fail ascii msg
    dne = '{F.WHITE}[{F.GREEN}+{F.WHITE}]{F.RESET}' # Done ascii msg

def main():
    while True:
        ip = str(input('Pv4, IPv6 or Domain name ~$ '))



if __name__ == '__main__':
    main()
