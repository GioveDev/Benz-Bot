from discord.ext import commands

class Base(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Succesfully logged in!')
        print('------')
        
    @commands.command()
    async def help(self, ctx):
        await ctx.send("Ich lutsche Ihren Schwanz und spiele Musik \n-**join** <channel name> \n-**play** <local file name> \n-**stream** <video link> \n-**volume** <0-100> \n-**stop** \n-**Herr Benz** wenn sie mit mir reden wollen")
            
def setup(bot):
    bot.add_cog(Base(bot))