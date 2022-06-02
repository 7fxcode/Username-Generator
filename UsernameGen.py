import random
import os
from tracemalloc import start
from colorama import Fore

Start = ['sweaty', 'rainy', 'drilla', 'trigger', 'glock', 'freezed', 'razer', 'lean', 'may',
'dev', 'haunted', 'gen', 'really', 'fr', 'fx', 'slava', 'dynamic', 'slice', 'traced', 'epic',
'boolean', 'ideal', 'undefined', 'dead', 'right']

End = ['grave', 'proof', 'west', 'forest', 'fluid', 'project', 'supreme', 'ukraini', 'dev',
'stranger', 'erase', 'rend', 'ridical', 'angle', 'tribe', 'frozen', 'defined', 'razor', 'synapse',
'log', 'dreamer', 'indeed', 'bash']

Sum = len(Start) + len(End)
Sum2 = Sum * Sum
CurrentVersion = '1.0'

while 1==1:
    os.system('cls')
    print(Fore.MAGENTA + '''
██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗███╗   ██╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝''')
    print('')
    print('Current Usernames:', Sum2)
    print('Version:', CurrentVersion)
    print('')
    print(Fore.MAGENTA + random.choice(Start) + random.choice(End))
    input(Fore.RED + 'Enter to generate a new username')
    os.system('cls')
    print(Fore.MAGENTA + '''
██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗███╗   ██╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝''')
    print('')
    print('Current Usernames:', Sum2)
    print('Version:', CurrentVersion)
    print('')
    print(Fore.MAGENTA + random.choice(Start) + random.choice(End))
    input(Fore.RED + 'Enter to generate a new username')
    os.system('cls')