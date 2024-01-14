import discord
from discord.ext import commands
from discord.commands import *

import ezcord


class AdminDB(ezcord.DBHandler):
    def __init__(self):
        super().__init__("Admins.db")

    async def setupDB(self):
        await self.execute("CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, adminname VARCHAR(255))")


db = AdminDB()

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py was loaded")
        await db.setupDB()

    admin = SlashCommandGroup(name="botowner", description="Bot Owner Commands")

    @admin.command(name="help")
    async def _help(self, ctx: discord.ApplicationContext):
        await ctx.respond("Admin Help successfully")

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))