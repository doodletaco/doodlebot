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
    await ctx.channel.send("pong! <:yall_cute:743358483822280816>")

@bot.command()
async def echo(ctx):
    response = ctx.message.content[5:]

    if len(response) > 0:
        await ctx.channel.send(response)
    else:
        await ctx.channel.send("Please stop breaking my bot. <:pandi_screm:727673331758661694>")

    await ctx.message.delete(delay=1)

bot.run(TOKEN)
