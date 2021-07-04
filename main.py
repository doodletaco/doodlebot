# This is a simple discord bot.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("with y'all"))
    print(f'{bot.user} has connected to discord!')

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong! :ping_pong:")

@bot.command()
async def echo(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)

bot.run(TOKEN)
