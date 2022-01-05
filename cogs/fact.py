import asyncio
import os, io
import random
import sys, requests
import platform
import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command, BucketType

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class fact(commands.Cog, name="APIS"):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
      name="joke",
      desciption="Get a funny or maybe not so funny joke."
    )
    async def joke(self, inter):
        #joke api https://github.com/15Dkatz/official_joke_api
            async with aiohttp.ClientSession() as session:
                async with session.get("https://official-joke-api.appspot.com/random_joke") as request:
                    if request.status == 200:
                        data = await request.json()
                        embed = disnake.Embed(
                            title=data["setup"],
                            description="Answer: ||" + data["punchline"]+"||",
                            color=config.main_color
                        )
                        await inter.send(embed=embed)
                    else:
                        embed = disnake.Embed(
                            title="Error!",
                            description="There is something wrong with the API, please try again later",
                            color=config.error
                        )
                        await inter.send(embed=embed)

    @slash_command(
      name="bored",
      description="Are you bored? Use this command!"
    )
    async def bored(self, inter, *, activity=None):
            
            if activity != None:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://www.boredapi.com/api/activity?type={activity}") as request:
                        if request.status == 200:
                            data = await request.json()
                        else:
                            embed = disnake.Embed(
                                title="Error!",
                                description="There is something wrong with the API, please try again later",
                                color=config.error
                            )
                            await inter.send(embed=embed)
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://www.boredapi.com/api/activity") as request:
                        if request.status == 200:
                            data = await request.json()
                        else:
                            embed = disnake.Embed(
                                title="Error!",
                                description="There is something wrong with the API, please try again later",
                                color=config.error
                            )
                            await inter.send(embed=embed)
                        link = data["link"]
                        if link == "" or " ":
                            embed = disnake.Embed(
                                title=data["activity"],
                                description="Type: "+data["type"],
                                color=config.main_color
                            )
                            embed.add_field(
                                name="Link for saving",
                                value="https://www.boredapi.com/api/activity?key="+data["key"]
                            )
                            await inter.send(embed=embed)
                        else:
                            embed = disnake.Embed(
                                title=data["activity"],
                                description="Type: "+data["type"],
                                color=config.main_color
                            )
                            embed.add_field(
                                name="Link for saving",
                                value="https://www.boredapi.com/api/activity?key="+data["key"]
                            )
                            embed.set_footer(
                                text="Source"+data["link"]
                            )
                            await inter.send(embed=embed)
  
    @slash_command(
      name="cat",
      description="View some cute images of cats!"
    )
    async def cat(self, inter):
        #original api https://api.thecatapi.com/v1/images/search
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        embed = disnake.Embed(
          title = 'Kitty Cat 🐈',
          description = 'Cat'
        )
        embed.set_image(url=data['file'])            
        embed.set_footer(text="")
        #other not working \/
        await inter.send(embed=embed)
        embed = disnake.Embed(
            title = 'Random Cat 🐈',
            description = 'Random',
            colour = disnake.Colour.purple()
         )
        embed.set_image(url='https://api.thecatapi.com/v1/images/search')            
        embed.set_footer(text="")
        #await inter.send(embed=embed)

    @slash_command(
      name="dog",
      description="View some images of dogs!"
    )
    async def dog(self, inter):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        data = response.json()
        embed = disnake.Embed(
          title = 'Dog 🐈',
          description = 'Woof!'
        )
        embed.set_image(url=data['message'])
        await inter.send(embed=embed)

    @slash_command(
      name="trivia",
      description="Answer some trivia questions",
      guild_ids=[917879650921881631]
    )
    async def trivia(self, inter):
        #await inter.send("coming soon!")
        async with aiohttp.ClientSession() as session:
          async with session.get("https://opentdb.com/api.php?amount=1") as request:
            if request.status == 200:
              data = await request.json()
              embed = disnake.Embed(
                title=data["question"],
                description="Answer: ||" + data["punchline"]+"||",
                color=config.main_color
              )
              #for answer in data["incorrect_answers"]:

              #embed.add_field(

              #)
              embed.add_field(
                name=f"Difficulty: {data['difficulty']}"
              )
              await inter.send(embed=embed)
            else:
              embed = disnake.Embed(
                title="Error!",
                description="There is something wrong with the API, please try again later",
                color=config.error
              )
              await inter.send(embed=embed)
def setup(bot):
    bot.add_cog(fact(bot))
    print(f"> Extension {__name__} is ready")