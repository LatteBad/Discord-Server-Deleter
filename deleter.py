import discord
from colorama import Fore, init, Style


def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')


def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')


class Delete:
    @staticmethod
    async def roles_delete(guild_target: discord.Guild):
        for role in guild_target.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print_delete(f"Deleted Role: {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Delete Role: {role.name}")

    @staticmethod
    async def channels_delete(guild_target: discord.Guild):
        for channel in guild_target.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Channel: {channel.name}")

    @staticmethod
    async def categories_delete(guild_target: discord.Guild):
        categories = guild_target.categories
        for category in categories:
            try:
                await category.delete()
                print_delete(f"Deleted Category: {category.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Category: {category.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Category: {category.name}")

    @staticmethod
    async def emojis_delete(guild_target: discord.Guild):
        for emoji in guild_target.emojis:
            try:
                await emoji.delete()
                print_delete(f"Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Emoji: {emoji.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Emoji: {emoji.name}")

    @staticmethod
    async def icon_delete(guild_target: discord.Guild):
        icon_image = None
        await guild_target.edit(name=f'Empty Server')
        await guild_target.edit(icon=icon_image)
        print_delete(f"Server Deleted")
