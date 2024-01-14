import os

import discord
import ezcord

from discord.ext import commands
from discord.commands import *

from dotenv import load_dotenv

class ExampleBot(ezcord.Bot):
    def __init__(self, **options):
        super().__init__(**options)

load_dotenv()

client = ExampleBot(intents=discord.Intents.default())

if __name__ == "__main__":
    client.load_cogs(subdirectories=True)
    client.run(token=os.getenv('TOKEN'))