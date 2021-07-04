# This is a simple discord bot.
import os
import re
from datetime import datetime

import discord
from dotenv import load_dotenv
from discord.ext import commands
from dateutil import tz
import zoneinfo


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=".")

# regex for iso format
iso = re.compile(r"\d{4}-\d\d-\d\d \d\d:\d\d")
# list of supported timezones
timezone_ls = zoneinfo.available_timezones()

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
async def timezones(ctx):
    await ctx.channel.send("You can find a list of supported timezones here: <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>")

@bot.command()
# note: this needs YYYY-MM-DD HH:MM to be the input
async def convert(ctx, f, t, time):
    formatstring = "%Y-%m-%d %H:%M"
    if len(time) == 16 and iso.match(time):
        if f in timezone_ls and t in timezone_ls:
            f_zone = tz.gettz(f)
            t_zone = tz.gettz(t)

            f_time = datetime.strptime(time, formatstring)
            f_time = f_time.replace(tzinfo=f_zone)
            t_time = f_time.astimezone(t_zone)

            await ctx.channel.send("Your converted time is: **" + t_time.strftime("%d %b %Y %H:%M") + "**")

        else:
            await ctx.channel.send("This command currently only supports timezones in the tz database.\nYou can find a list here: <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>")
    else:
        await ctx.channel.send("Not sent in ISO format. Please use **YYYY-MM-DD HH:MM** for your time input.")


bot.run(TOKEN)
