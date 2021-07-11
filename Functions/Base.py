from discord.ext import commands
from discord_slash import cog_ext

description_string = "Ich lutsche Ihren Schwanz und spiele Musik \n-**join** <channel name> \n-**play** <local file name> \n-**stream** <video link> \n-**volume** <0-100> \n-**stop** \n-**Herr Benz** wenn sie mit mir reden wollen"

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