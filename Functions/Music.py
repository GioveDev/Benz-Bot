import discord
import discord.ext
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

from Functions import YTDL

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, url):

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {url}')

    async def stream(self, ctx, url):
        voice_channel = await self.ensure_voice(ctx)

        if type(ctx) is commands.context.Context:
            text_channel = ctx.message.channel
        else:
            text_channel = self.bot.get_channel(ctx.channel_id)

        async with text_channel.typing():
            player = await YTDL.Source.from_url(url, loop=self.bot.loop, stream=True)
            voice_channel.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name="stream")
    async def command_stream(self,ctx, *, url):
        await self.stream(ctx, url)

    @cog_ext.cog_slash(name="stream", guild_ids= [170601909349122049] )
    async def slash_stream(self, ctx, url):
        await self.stream(ctx, url)
        
    async def ensure_voice(self, ctx):
        if type(ctx) is commands.context.Context:
            voice_client = ctx.voice_client
        else:
            guild = self.bot.get_guild(ctx.guild_id)
            voice_client = guild.voice_client

        if voice_client is None:
            if ctx.author.voice:
                voice_channel = await ctx.author.voice.channel.connect()
                return voice_channel
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif voice_client.is_playing():
            voice_client.stop()
            return voice_client

            

def setup(bot):
    bot.add_cog(Music(bot))