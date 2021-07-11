
from discord.ext import commands
from discord_slash import cog_ext

from Functions.Music import Extensions

class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def volume(self, ctx, volume):
        voice_client = Extensions.Functions.get_voice_client(self.bot, ctx)

        if voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        if voice_client.source is None:
            return await ctx.send("No Audio Playing")

        voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command(name = "volume")
    async def command_volume(self, ctx, volume: int):
        await self.volume(ctx, volume)

    @cog_ext.cog_slash(name = "volume", description = "Change volume")
    async def slash_volume(self, ctx, volume: int):
        await self.volume(ctx, volume)

def setup(bot):
    bot.add_cog(Volume(bot))