from discord.ext import commands
from discord_slash import cog_ext
from selenium.webdriver.common.by import By

from selenium import webdriver


class BeresoCrawler(commands.Cog):
    def __init__(self, bot):
        self.driver = webdriver.Chrome(executable_path='C:/ChromeDriver/chromedriver.exe')

    @commands.command(name="bereso")
    async def command_help(self, ctx):
        await self.crawl(self, ctx)

    @cog_ext.cog_slash(name="bereso", description="i'll check if bereso is done")
    async def slash_help(self, ctx):
        await self.crawl(self, ctx)

    @staticmethod
    async def crawl(self, ctx):
        self.driver.get('https://bereso.com')
        assert r"Bereso" in self.driver.title
        if self.driver.find_element(By.XPATH, "//*[contains(text(), 'Meine Webseite wird zurzeit vollständig überarbeitet und demnächst aufgeschaltet')]"):
            await ctx.send('Bereso still is not done')
        else:
            await ctx.send('Bereso under construction page is no more!')


def setup(bot):
    bot.add_cog(BeresoCrawler(bot))



