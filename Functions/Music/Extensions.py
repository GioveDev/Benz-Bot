from discord.ext import commands

class Functions(commands.Cog):
    @classmethod
    async def ensure_voice(cls, bot, ctx):
        voice_client = cls.get_voice_client(bot, ctx)
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

    @classmethod
    def get_voice_client(cls, bot, ctx):
        if type(ctx) is commands.context.Context:
            return ctx.voice_client
        else:
            guild = bot.get_guild(ctx.guild_id)
            return guild.voice_client