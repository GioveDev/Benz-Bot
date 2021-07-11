import discord
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
    async def play(self, ctx, *, query):

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def stream(self, ctx, *, url):

        async with ctx.typing():
            player = await YTDL.Source.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

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
        
    @play.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            
    @cog_ext.cog_slash(name="test", guild_ids= [170601909349122049] )
    async def _test(self, ctx, url: SlashContext):
        vc = await ctx.author.voice.channel.connect()
        
        player = await YTDL.Source.from_url(url, loop=self.bot.loop, stream=True)
        vc.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send("Playing")

def setup(bot):
    bot.add_cog(Music(bot))