import os

def load_config(filename):
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()
    return config

config = load_config('config.txt')

os.system('cls' if os.name == 'nt' else 'clear')
menu = """

 ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗ ██████╗     ██████╗  █████╗ ██╗██████╗ ███████╗
██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║     ██║     ██║   ██║██║   ██║██║  ██║███████╗██║   ██║    ██████╔╝███████║██║██║  ██║███████╗
██║     ██║     ██║   ██║██║   ██║██║  ██║╚════██║██║▄▄ ██║    ██╔══██╗██╔══██║██║██║  ██║╚════██║
╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝███████║╚██████╔╝    ██║  ██║██║  ██║██║██████╔╝███████║
 ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝ ╚══▀▀═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝
                                                                                                  


"""
menu2 = f"""
> Tool Name     : CloudSQ RAIDS
> Version       : 1.0
> Creator       : cloudfrankito.
> Coding        : Python/Batch
> Discord [W]   : https://discord.gg/cloudsq
> GitHub [W]    : https://github.com/cloudfran/cloudraidtool
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")
    input("\n\033[31mPress Enter to return to the main menu...\033[0m")
    os.system('python cyb3rtech.py')

if __name__ == "__main__":
    show_menu()
