import json
from json.decoder import JSONDecodeError
import requests

from discord.ext import commands

error_message = "An error has occurred, if this issue persists contact my master"

class CleverBotChat(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Herr Benz '):
            message_string = message.content[10:]

            try:
                async with message.channel.typing():
                    reply = requests.get("", params = { '': ''})
                    reply_text = json.loads(reply.text)

            except requests.ConnectionError:
                await message.channel.send(error_message)

            await message.channel.send(reply_text)

def setup(bot):
    bot.add_cog(CleverBotChat(bot))