import discord

from discord import commands
from discord.commands import *

class BanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="ban", description="Ban a User from your Discord Server.")
    @commands.guild_only()
    @commands.has_permission(ban_members=True)