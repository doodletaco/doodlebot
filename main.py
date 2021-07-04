# This is a simple discord bot.
import os
from datetime import datetime

import discord
from dotenv import load_dotenv
from discord.ext import commands
from dateutil import tz


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=".")

# commands that make sure bot is up and running
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("with y'all"))
    print(f'{bot.user} has connected to discord!')

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong! :ping_pong:")

# fun command thingies
@bot.command()
async def echo(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)

@bot.command()
# note: this needs YYYY-MM-DD HH:MM to be the input
async def convert(ctx, f, t, time):
    formatstring = "%Y-%m-%d %H:%M"
    if "/" in f.lower():
        f_zone = tz.gettz(f)
        t_zone = tz.gettz(t)

        f_time = datetime.strptime(time, formatstring)
        f_time = f_time.replace(tzinfo=f_zone)
        t_time = f_time.astimezone(t_zone)

        await ctx.channel.send("Your converted time is: **" + t_time.strftime("%d %b %Y %H:%M") + "**")

    else:
        await ctx.channel.send("This command currently only supports timezones in the tz database.\nYou can find a list here: <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>")


bot.run(TOKEN)
