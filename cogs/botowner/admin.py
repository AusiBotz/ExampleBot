import discord
from discord.ext import commands
from discord.commands import *

import ezcord


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py was loaded")

    admin = SlashCommandGroup(name="botowner", description="Bot Owner Commands")

    @admin.command(name="help")
    async def _help(self, ctx: discord.ApplicationContext):
        await ctx.respond("Admin Help successfully")

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))