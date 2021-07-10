import discord
from discord import message
from discord.ext import commands

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Herr Benz '):
            await message.channel.send('Ja, aber zuerst müssen sie die Projektdokumentation schreiben')

def setup(bot):
    bot.add_cog(Talk(bot))