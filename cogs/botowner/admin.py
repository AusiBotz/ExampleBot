import discord
from discord.ext import commands
from discord.commands import *

import ezcord


class AdminDB(ezcord.DBHandler):
    def __init__(self):
        super().__init__("Admins.db")

    async def setupDB(self):
        await self.execute("CREATE TABLE IF NOT EXISTS admins (userid INTEGER PRIMARY KEY, adminname VARCHAR(255))")

    async def add_admin(self, userid: int, adminname: str):
        await self.execute("INSERT OR IGNORE INTO admins (userid, adminname) VALUES (?, ?)", (userid, adminname))


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

    @admin.command(name="add", description="Add a Bot Owner / Admin to the Panel")
    @commands.has_permissions(administrator=True)
    async def _add(self, ctx: discord.ApplicationContext, user: Option(discord.Member, "Choose a User", required=True)):
        try:
            await db.add_admin(userid=user.id, adminname=user.name)
            await ctx.respond(f"Added {user.name} to {ctx.guild.name} Admins", ephemeral=True)
        except:
            await ctx.respond(f"There was an Error while we trying to add an Admin with the ID(||{user.id}||)", ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))