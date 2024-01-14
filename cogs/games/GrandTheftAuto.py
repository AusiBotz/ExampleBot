import discord
import ezcord
from discord.ext import commands
from discord.ext.pages import Page, Paginator

from discord.commands import *

class GrandTheftAuto(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gay")


def setup(bot: commands.Bot):
    bot.add_cog(GrandTheftAuto(bot))