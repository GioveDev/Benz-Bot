from discord.ext import commands
from discord_slash import cog_ext

from Functions.Music.MusicExtensions import VoiceChannelExtensions
class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "stop")
    async def command_stop(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Leaving")
    
    @cog_ext.cog_slash(name = "stop", description = "Leave channel")
    async def slash_stop(self, ctx):
        voice_client = VoiceChannelExtensions.get_voice_client(self.bot, ctx)
        await voice_client.disconnect()
        await ctx.send("Leaving")

def setup(bot):
    bot.add_cog(Stop(bot))