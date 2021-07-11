import discord
from discord.ext import commands
from discord_slash import cog_ext

from Functions.Music.MusicExtensions import VoiceChannelExtensions

class Join(commands.Cog):
    def __init__(self, bot):
            self.bot = bot

    async def join(self, ctx, channel):
        voice_client = VoiceChannelExtensions.get_voice_client(self.bot, ctx)

        if voice_client is not None:
            return await voice_client.move_to(channel)

        await channel.connect()
        await ctx.send(f'Joining {channel}')

    @commands.command(name = "join")
    async def command_join(self, ctx, *, channel: discord.VoiceChannel):
        await self.join(ctx, channel)

    @cog_ext.cog_slash(name = "join", description = "Join a channel")
    async def slash_join(self, ctx, channel: discord.VoiceChannel):
        await self.join(ctx, channel)

def setup(bot):
    bot.add_cog(Join(bot))