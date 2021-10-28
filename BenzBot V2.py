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
bot.load_extension("Functions.Talk")
bot.load_extension("Functions.CleverBotChat.CleverBotChat")
bot.load_extension("Functions.Music.Join")
bot.load_extension("Functions.Music.Play")
bot.load_extension("Functions.Music.Stream")
bot.load_extension("Functions.Music.Volume")
bot.load_extension("Functions.Music.Stop")
bot.load_extension("Functions.Selenium.BeresoCrawler")
bot.run(TOKEN)
