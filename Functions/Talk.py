from discord.ext import commands

class Talk(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Secret '):
            await message.channel.send('Ja, aber zuerst müssen sie die Projektdokumentation schreiben')

def setup(bot):
    bot.add_cog(Talk(bot))