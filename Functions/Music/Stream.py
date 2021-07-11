from discord.ext import commands
from discord_slash import cog_ext

from Functions.Music.YTDL import Source
from Functions.Music.MusicExtensions import VoiceChannelExtensions

class Stream(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def stream(self, ctx, url):
        voice_client = await VoiceChannelExtensions.ensure_voice(self.bot, ctx)

        if type(ctx) is commands.context.Context:
            text_channel = ctx.message.channel
        else:
            text_channel = self.bot.get_channel(ctx.channel_id)

        async with text_channel.typing():
            player = await Source.from_url(url, loop=self.bot.loop, stream=True)
            voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send(f'Now playing: {player.title}')

    @commands.command(name = "stream")
    async def command_stream(self, ctx, *, url):
        await self.stream(ctx, url)

    @cog_ext.cog_slash(name = "stream", description = "Stream audio from URL")
    async def slash_stream(self, ctx, url):
        await self.stream(ctx, url)


def setup(bot):
    bot.add_cog(Stream(bot))
