import discord

from discord.ext import commands
from discord.commands import *

class BanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="ban", description="Ban a User from your Discord Server.")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx: discord.ApplicationContext, member: Option(discord.Member, "Choose a User", required=True)):
        try:
            await member.ban(reason="Banned by a Admin")
        except discord.DiscordException as de:
            await ctx.respond(f"{de}", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(BanCommand(bot))