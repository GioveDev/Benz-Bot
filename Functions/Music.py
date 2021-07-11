from re import A
import discord
import discord.ext
from discord.ext import commands
from discord_slash import cog_ext

from Functions import YTDL

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def join(self, ctx, channel):
        voice_client = self.get_voice_client(ctx)

        if voice_client is not None:
            return await voice_client.move_to(channel)

        await channel.connect()
        await ctx.send(f'Joining {channel}')

    async def play(self, ctx, url):
        voice_client = await self.ensure_voice(ctx)

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))
        voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {url}')

    async def stream(self, ctx, url):
        voice_client = await self.ensure_voice(ctx)

        if type(ctx) is commands.context.Context:
            text_channel = ctx.message.channel
        else:
            text_channel = self.bot.get_channel(ctx.channel_id)

        async with text_channel.typing():
            player = await YTDL.Source.from_url(url, loop=self.bot.loop, stream=True)
            voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send(f'Now playing: {player.title}')

    
    async def volume(self, ctx, volume):
        voice_client = self.get_voice_client(ctx)

        if voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        if voice_client.source is None:
            return await ctx.send("No Audio Playing")

        voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")
    
    async def ensure_voice(self, ctx):
        voice_client = self.get_voice_client(ctx)
        if voice_client is None:
            if ctx.author.voice:
                voice_client = await ctx.author.voice.channel.connect()
                return voice_client
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif voice_client.is_playing():
            voice_client.stop()
            return voice_client
        elif voice_client.is_connected():
            return voice_client

    def get_voice_client(self, ctx):
        if type(ctx) is commands.context.Context:
            return ctx.voice_client
        else:
            guild = self.bot.get_guild(ctx.guild_id)
            return guild.voice_client

    @commands.command(name = "join")
    async def command_join(self, ctx, *, channel: discord.VoiceChannel):
        await self.join(ctx, channel)

    @cog_ext.cog_slash(name = "join", description = "Join a channel")
    async def slash_join(self, ctx, channel: discord.VoiceChannel):
        await self.join(ctx, channel)

    @commands.command(name = "play")
    async def command_play(self, ctx, *, url):
        await self.play(ctx, url)

    @cog_ext.cog_slash(name = "play", description = "Play a file from the local system")
    async def slash_play(self, ctx, url):
        await self.play(ctx, url)

    @commands.command(name = "stream")
    async def command_stream(self, ctx, *, url):
        await self.stream(ctx, url)

    @cog_ext.cog_slash(name = "stream", description = "Stream audio from URL")
    async def slash_stream(self, ctx, url):
        await self.stream(ctx, url)

    @commands.command(name = "volume")
    async def command_volume(self, ctx, volume: int):
        await self.volume(ctx, volume)

    @cog_ext.cog_slash(name = "volume", description = "Change volume")
    async def slash_volume(self, ctx, volume: int):
        await self.volume(ctx, volume)

    @commands.command(name = "stop")
    async def command_stop(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Leaving")
    
    @cog_ext.cog_slash(name = "stop", description = "Leave channel")
    async def slash_stop(self, ctx):
        voice_client = self.get_voice_client(ctx)
        await voice_client.disconnect()
        await ctx.send("Leaving")

def setup(bot):
    bot.add_cog(Music(bot))