# This is a simple discord bot.

import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with y'all"))
    print(f'{client.user} has connected to discord!')

client.run(TOKEN)
