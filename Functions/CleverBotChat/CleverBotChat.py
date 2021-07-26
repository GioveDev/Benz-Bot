import asyncio
from json.decoder import JSONDecodeError
import cleverbotfree
from discord.ext import commands

import json
import requests

#Honestly this is fucking jank but it works

class CleverBotChat(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Herr Benz '):
            message_string = message.content[10:]

            try:
                async with message.channel.typing():
                    reply = requests.get("http://192.168.1.30:5000/chat", params = { 'message':message_string })
                    reply_text = json.loads(reply.text)
            except JSONDecodeError:
                await message.channel.send("An error has occurred, if this issue persists contact my master")
            except requests.ConnectionError:
                await message.channel.send("An error has occurred, if this issue persists contact my master")

            await message.channel.send(reply_text)

def setup(bot):
    bot.add_cog(CleverBotChat(bot))