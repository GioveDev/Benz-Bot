import os

from discord.ext import commands
from discord_slash import SlashCommand

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or("Benz "),
                   help_command=None)
slash = SlashCommand(bot, sync_commands=True)

bot.load_extension("Functions.Base")
bot.load_extension("Functions.Music")
bot.load_extension("Functions.Talk")
bot.run(TOKEN) 