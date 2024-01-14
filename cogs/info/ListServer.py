import discord
import ezcord

from discord.commands import slash_command

class ServerList(ezcord.Cog):

    @slash_command()
    async def list_servers(self, ctx):
        desc = ""
        counter = 1
        pages = []

        for i in self.chunks(self.bot.guilds, 10):
            embed = discord.Embed(title="Server List", color=0x00ff00)
            counter + 1
            for j in i:
                desc += f"{counter}. {j.name} - `{j.id}`\n"

            embed.description = desc
            pages.append(embed)

        if len(pages) > 0:
            await ctx.respond(embed=pages[0], view=Paginator(pages))
        else:
            await ctx.respond(embed=pages[0])

        await ctx.respond(embed=embed)

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]


def setup(bot: discord.Bot):
    bot.add_cog(ServerList(bot))


class Paginator(discord.ui.View):
    def __init__(self, pages: list):
        super().__init__()
        self.pages = pages
        self.i = 0
        self.children[0].disabled = True
        self.children[1].disabled = True

    @discord.ui.button(label='<<', style=discord.ButtonStyle.danger)
    async def backtCallback(self, interaction: discord.Interaction, button: discord.Button):
        if self.i > 0:
            self.i -= 1
            self.pages[self.i].set_footer(text=f'Seite {self.i + 1} / {len(self.pages)}')
            if self.i == 0:
                self.children[1].disabled = True
                button.disabled = True
            if self.i < len(self.pages):
                self.children[2].disabled = False
            await interaction.response.edit_message(embed=self.pages[self.i], view=self)

    @discord.ui.button(label='🏠', style=discord.ButtonStyle.blurple)
    async def homeCallback(self, interaction: discord.Interaction, button: discord.Button):
        if self.i > 0:
            self.i = 0
            self.pages[self.i].set_footer(text=f'Seite 1 / {len(self.pages)}')
            self.children[0].disabled = True
            self.children[2].disabled = False
            button.disabled = True
            await interaction.response.edit_message(embed=self.pages[self.i], view=self)

    @discord.ui.button(label='>>', style=discord.ButtonStyle.success)
    async def nextCallback(self, interaction: discord.Interaction, button: discord.Button):
        if self.i < len(self.pages):
            self.i += 1
            self.pages[self.i].set_footer(text=f'Seite {self.i + 1} / {len(self.pages)}')
            if self.i + 1 == len(self.pages):
                button.disabled = True
            if self.i < len(self.pages):
                self.children[0].disabled = False
                self.children[1].disabled = False
            await interaction.response.edit_message(embed=self.pages[self.i], view=self)