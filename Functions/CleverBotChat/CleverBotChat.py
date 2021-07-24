import asyncio
import cleverbotfree
from discord.ext import commands

class CleverBotChat(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
            message_string = message.content[10:]
            if message.content.startswith('Herr Benz '):
                async with cleverbotfree.async_playwright() as p_w:
                    async with message.channel.typing():
                        c_b = await cleverbotfree.CleverbotAsync(p_w)
                        bot = await c_b.single_exchange(message_string)
                        await message.channel.send(bot)

def setup(bot):
    bot.add_cog(CleverBotChat(bot))