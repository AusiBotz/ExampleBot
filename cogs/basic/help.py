import discord
from discord.ext import commands
from discord.commands import *

import ezcord


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("hep.py was loaded")

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))