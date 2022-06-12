from colorama import init, Fore, Style


def colourful_print(type, str):
    init(wrap=True, autoreset=True)

    if type.upper() == 'INFO':
        print(Fore.BLUE + Style.BRIGHT + str)
    elif type.upper() == 'SUCCESS':
        print(Fore.GREEN + Style.BRIGHT + str)
    elif type.upper() == 'WARNING':
        print(Fore.YELLOW + Style.BRIGHT + str)
    elif type.upper() == 'ERROR':
        print(Fore.RED + Style.BRIGHT + str)
    else:
        print(Style.BRIGHT + str)
