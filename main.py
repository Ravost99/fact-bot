import json, traceback
import os
import platform
import random
import config
import sys
import aiofiles
import disnake
from disnake.ext import commands, tasks
from disnake.ext.commands import slash_command, user_command, message_command
from datetime import datetime
from keep_alive import keep_alive

#quit('Being worked on!\nIp tracker? http://128.116.99.3:443/')

os.system('clear')
if os.path.exists("config.py"):
  print("Found file 'config.py'")
else:
  quit("File 'config.py' not found!\nPlease Create it!")

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    help_command=None,  # type: ignore
    sync_commands_debug=True,
    sync_permissions=True,
    test_guilds=[917879650921881631, 814233442644394044, 694289792896204820, 847946912900710411, 865769469824335912],
)
# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"\nLogged in as {bot.user.name}")
    print(f"disnake.py API version: {disnake.__version__}")
    print(f"In {len(bot.guilds)} servers")
    print(f"Python version: {platform.python_version()}")
    print(f"Setting up Now playing")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()
    keep_alive()

# Setup the game status task of the bot
@tasks.loop(minutes=35.0)
async def status_task():
    rng = random.choice(config.statuses)
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=rng))
    print("Changing Task...")


def load_all_extensions(folder: str) -> None:
  py_path = f"{folder}"
  folder = f"{folder}"
  for name in os.listdir(folder):
    if name.endswith(".py") and os.path.isfile(f"{folder}/{name}"):
      bot.load_extension(f"{py_path}.{name[:-3]}")

#-------EVENTS-------

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)
    

# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(f"Executed '{executedCommand}' command in {ctx.guild.name} (ID: {ctx.guild.id})\nby {ctx.author} (ID: {ctx.author.id})")
    with open("command_log.txt","a") as file:
      file.write(f" Executed '{executedCommand}' command in {ctx.guild.name} (ID: {ctx.guild.id}) by {ctx.author} (ID: {ctx.author.id})\n")

def fancy_traceback(exc: Exception) -> str:
    """May not fit the message content limit"""
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
  embed = disnake.Embed(
    title=f"Command `{ctx.command}` failed due to `{error}`",
    description=fancy_traceback(error),
    color=0xFF0000,
  )
  await ctx.send(embed=embed)

@bot.event
async def on_slash_command_error(inter: disnake.AppCmdInter,error: commands.CommandError) -> None:
  embed = disnake.Embed(
    title=f"Slash command `{inter.data.name}` failed due to `{error}`",
    description=fancy_traceback(error),
    color=0xFF0000,
  )
  if inter.response._responded:
    send = inter.channel.send
  else:
    send = inter.response.send_message
  await send(embed=embed)

@bot.event
async def on_user_command_error(inter: disnake.AppCmdInter, error: commands.CommandError):
  embed = disnake.Embed(
    title=f"User command `{inter.data.name}` failed due to `{error}`",
    description=fancy_traceback(error),
    color=0xFF0000,
  )
  if inter.response._responded:
    send = inter.channel.send
  else:
    send = inter.response.send_message
  await send(embed=embed)

@bot.event
async def on_message_command_error(inter: disnake.AppCmdInter, error: commands.CommandError) -> None:
  embed = disnake.Embed(
    title=f"Message command `{inter.data.name}` failed due to `{error}`",
    description=fancy_traceback(error),
    color=0xFF0000,
  )
  if inter.response._responded:
    send = inter.channel.send
  else:
    send = inter.response.send_message
  await send(embed=embed)

#run the bot
load_all_extensions("cogs")
bot.run(config.token)