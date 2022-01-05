import asyncio
import os, io
import random
import sys
import platform
import aiohttp
import disnake, json
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command, BucketType

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="General"):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
      name="fact",
      description="Get a random fact, the reason the bot is here."
    )
    async def fact(self, inter):            
            async with aiohttp.ClientSession() as session:
                async with session.get("https://useless-facts.sameerkumar.website/api") as request:
                    if request.status == 200:
                        data = await request.json()
                        embed = disnake.Embed(description=data["data"], color=config.main_color)
                        await inter.send(embed=embed)
                    else:
                        embed = disnake.Embed(
                            title="Error!",
                            description="There is something wrong with the API, please try again later",
                            color=config.error
                        )
                        await inter.send(embed=embed)
          
    @slash_command(
      name="ping",
      description="Check if the bot is alive."
    )
    async def ping(self, inter):
        embed = disnake.Embed(
            color=config.success
        )
        embed.add_field(
            name="Pong! :ping_pong:",
            value=f"{round(self.bot.latency * 1000)}ms.",
            inline=True
        )
        embed.set_footer(
            text=f"Pong request by {inter.author}"
        )
        await inter.send(embed=embed)
    
    @slash_command(
      name="invite",
      description="Get the invite link of the bot to be able to invite it."
    )
    async def invite(self, inter):
        await inter.send("I sent you a private message!")
        #await inter.author.send(f"Invite me by clicking here: https://disnake.com/api/oauth2/authorize?client_id=867059114005626901&permissions=2681208305&scope=bot")
        await inter.author.send(f"https://fact-bot.ravost.repl.co/invite")

    @slash_command(
      name="bitcoin",
      description="Get the current price of a bitcoin"
    )
    async def bitcoin(self, inter):
          url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
          # Async HTTP request
          import json
          async with aiohttp.ClientSession() as session:
              raw_response = await session.get(url)
              response = await raw_response.text()
              response = json.loads(response)
              embed = disnake.Embed(
                  title=":information_source: Info",
                  description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                  color=config.info
              )
              await inter.send(embed=embed)

    @slash_command(
      name="info",
      description="Get some useful (or not) information about the bot."
    )
    async def info(self, inter):
          embed = disnake.Embed(
              title="Bot Information",
              description="Info about the bot",
              color=config.info
          )
          embed.add_field(
              name="Bot Information",
              value=f"Name: {self.bot.user}",
              inline=False
          )
          embed.add_field(
              name="Python Version:",
              value=f"{platform.python_version()}",
              inline=True
          )
          embed.add_field(
            name="Fact API #1",
            value="[uselessfacts](https://uselessfacts.jsph.pl/random.json?language=en)",
            inline=False
          )
          embed.add_field(
            name="Fact API #2",
            value="[useless-facts](https://useless-facts.sameerkumar.website/api)",
            inline=True
          )
          embed.add_field(
            name="Joke API",
            value="[random_joke](https://official-joke-api.appspot.com/random_joke)",
            inline=False
          )
          embed.add_field(
            name="Trivia API",
            value="[trivia](https://opentdb.com/)",
            inline=False
          )
          embed.set_footer(
              text=f"Requested by {inter.author}"
          )
          await inter.send(embed=embed)

    @user_command(
      name="botInfo"
    )
    async def botInfo(self, inter):
          embed = disnake.Embed(
              title="Bot Information",
              description="Info about the bot",
              color=config.info
          )
          embed.add_field(
              name="Bot Information",
              value=f"Name: {self.bot.user}",
              inline=False
          )
          embed.add_field(
              name="Python Version:",
              value=f"{platform.python_version()}",
              inline=True
          )
          embed.add_field(
            name="Fact API #1",
            value="[uselessfacts](https://uselessfacts.jsph.pl/random.json?language=en)",
            inline=False
          )
          embed.add_field(
            name="Fact API #2",
            value="[useless-facts](https://useless-facts.sameerkumar.website/api)",
            inline=True
          )
          embed.add_field(
            name="Joke API",
            value="[random_joke](https://official-joke-api.appspot.com/random_joke)",
            inline=False
          )
          embed.add_field(
            name="Trivia API",
            value="[trivia](https://opentdb.com/)",
            inline=False
          )
          embed.set_footer(
              text=f"Requested by {inter.author}"
          )
          await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(general(bot))
    print(f"> Extension {__name__} is ready")