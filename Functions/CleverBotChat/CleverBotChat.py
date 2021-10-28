import json
from json.decoder import JSONDecodeError
import requests
import re

from discord.ext import commands

error_message = "An error has occurred, if this issue persists contact my master"

class CleverBotChat(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Herr Benz ') or self.client.user.mentioned_in(message):
            message_string = message.content.replace('Herr Benz ', '')
            message_string = re.sub(r'<@.*>\W?','', message_string )
            print(message_string)

            try:
                async with message.channel.typing():
                    reply = requests.get("", params = { 'message': message_string })
                    reply_text = json.loads(reply.text)

            except requests.ConnectionError:
                await message.channel.send(error_message)

            await message.channel.send(reply_text)

def setup(bot):
    bot.add_cog(CleverBotChat(bot))