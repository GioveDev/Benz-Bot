import discord
from discord.ext import commands
from discord_slash import cog_ext

from Functions.Music import Extensions

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def play(self, ctx, url):
        voice_client = await Extensions.Functions.ensure_voice(self.bot, ctx)

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))
        voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    
    @commands.command(name = "play")
    async def command_play(self, ctx, *, url):
        await self.play(ctx, url)

    @cog_ext.cog_slash(name = "play", description = "Play a file from the local system")
    async def slash_play(self, ctx, url):
        await self.play(ctx, url)

def setup(bot):
    bot.add_cog(Play(bot))
