import os

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or("Benz "),
                   help_command=None)

bot.load_extension("Functions.Base")
bot.load_extension("Functions.Music")
bot.load_extension("Functions.Talk")
bot.run(TOKEN) 