import discord

import ezcord

from discord.ext import commands
from discord.commands import *

class KickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="kick", description="Kick a User from your Discord Server")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: discord.ApplicationContext, member: Option(discord.Member, "Choose a User", required=True)):
        try:
            await member.kick(reason="Kicked by an Admin")
        except discord.DiscordException as de:
            await ctx.respond(f"{de}", ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(KickCommand(bot))