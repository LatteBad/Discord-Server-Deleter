from os import system
mytitle = "Deleter - by latte#0406"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from deleter import Delete

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.MAGENTA}

                                    ██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
                                    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
                                    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██████╔╝
                                    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██╔══██╗
                                    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗██║  ██║
                                    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
                                                {Fore.RED}by latte#0406{Style.RESET_ALL}
                                                
*Use at your own risk. Actions executed are irreversible.
        """)
token = input(f'Please enter your token:\n >')
guild_id = input('Please enter the target server ID:\n >')
token = token  # <-- Account token
choice = input('Please enter the content you want to delete. 1=Channels, 2=Roles, 3=Emojis, 4=Categories, 5=Everything\n >')

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Hello, {client.user}.")
    print("Deleting Content...")
    guild_target = client.get_guild(int(guild_id))
    try:
        if choice=='1':
            await Delete.channels_delete(guild_target)
        elif choice=='2':
            await Delete.roles_delete(guild_target)
        elif choice=='3':
            await Delete.emojis_delete(guild_target)
        elif choice=='4':
            await Delete.categories_delete(guild_target)
        elif choice=='5':
            await Delete.channels_delete(guild_target)
            await Delete.roles_delete(guild_target)
            await Delete.emojis_delete(guild_target)
            await Delete.categories_delete(guild_target)
            await Delete.icon_delete(guild_target)
        else:
            print("Invalid choice, please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input, please enter a number.")
        return
    
    print(f"""{Fore.GREEN}


                                            ██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
                                            ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
                                            ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██║  ██║
                                            ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔
                                            ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██║  ██║
                                            ██████╔╝███████╗███████╗███████╗   ██║   ███████╗██████╔╝
                                            ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═════╝                 

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
                                                         
