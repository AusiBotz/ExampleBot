import discord
import ezcord
from discord.ext import commands
from discord.commands import *


class BotDB(ezcord.DBHandler):
    def __init__(self):
        super().__init__("System.db")

    async def setupDB(self):
        await self.execute("CREATE TABLE IF NOT EXISTS botMessages(botBy TEXT)")

    async def get_bot_by_msg(self):
        return await self.one("SELECT botBy FROM botMessages") or "Bot by System"

    async def set_default(self):
        await self.execute("INSERT OR IGNORE INTO botMessages(botBy) VALUES ('bot by Lennard & Noah')")


db = BotDB()

class GlobalBotDB(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await db.setupDB()

def setup(bot: commands.Bot):
    bot.add_cog(GlobalBotDB(bot))