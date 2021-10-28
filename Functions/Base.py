from discord.ext import commands
from discord_slash import cog_ext

description_string = "I suck your dick and play music " \
                     "\n-**join** <channel name> " \
                     "\n-**play** <local file name> " \
                     "\n-**stream** <video link or youtube query> " \
                     "\n-**volume** <0-100> " \
                     "\n-**stop** to stop the music and leave the channel" \
                     "\n-**bereso** i'll check if bereso is done " \
                     "\n-**Herr Benz** when you want to talk with me " \
                     "\nI also react to @mentions"

class Base(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Succesfully logged in!')
        print('------')
        
    @commands.command(name = "help")
    async def command_help(self, ctx):
        await ctx.send(description_string)

    @cog_ext.cog_slash(name = "help", description = "fucking help me pls")
    async def slash_help(self, ctx):
        await ctx.send(description_string)
            
def setup(bot):
    bot.add_cog(Base(bot))