#-*-Code:Latin-1*-
import discord
from discord.ext import commands
from async_timeout import timeout
import youtube_dl
import asyncio
import time
import functools
import itertools
import math
import random
import time
from discord import channel, client
import json
import aiohttp
import os 
import datetime
import psutil # to get system details
import requests # to make http requests
import platform
from ffmpeg import image
from discord.ext.commands.bot import Bot
from datetime import datetime
from discord.ext import commands
from discord.ext import tasks
import sys
import re # needed for regex
from discord import Embed, guild, member
from youtube_dl.extractor import reddit
from datetime import datetime
import pydoc_data.topics
from random import randint
#import basc_py4chan
import sqlite3
#from pixivpy3 import *
import urllib
#import PySide2
#import PySide2.examples
import datetime
import subprocess
#from tinydb import TinyDB, Query
from discord.utils import get
import datetime
from datetime import datetime
import embedlinks
from notes import help, note, examples, ratings

prefix = "/"
bot = commands.Bot(command_prefix = f"{prefix}", description = "", intents=discord.Intents.default())
#-------------------------------------------------------------------------------------------
role = 'Fondateurs'
musics = {}
ytdl = youtube_dl.YoutubeDL()

role3 = "Sans-Fiche" 


#---------------------------[Hentai Command]-------------------------------------------

def get_gelImage(tags):
    """Returns pictures from Gelbooru with given tags."""
    tags = list(tags)
    formatted_tags = ""
    rating = ""

    ratings = {
        "re": "rating%3aexplicit",
        "rq": "rating%3aquestionable",
        "rs": "rating%3asafe"
    }

    if tags:  # if there are any tags, check for ratings
        if tags[0] in ratings:
            rating = ratings[tags[0]]
            tags.remove(tags[0])

    if rating == "":  # if rating wasn't specified, set safe one
        rating = ratings["rs"]

    # make tags suitable for Gelbooru API url
    formatted_tags = "_".join(tags).replace("/", "+")

    print(rating, formatted_tags)

    api_url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=50&tags={rating}+{formatted_tags}"
    response = requests.get(api_url)
    try:
        # parsing json
        json_api_url = json.loads(response.text)
        image = random.choice(json_api_url)["file_url"]
        return image
    except ValueError:
        return "No results with given tags or they are incorrect."


@bot.event
async def on_ready():
    """Sends information when the bot starts running."""
    print('We have logged in as {0.user}'.format(bot))

# commands below take messages from notes.py file
@bot.command()
async def hhelp(ctx):
    """Sends the help message."""
    message = help
    await ctx.send(message)


@bot.command()
async def hnote(ctx):
    """Sends the disclaimer."""
    message = note
    await ctx.send(message)


@bot.command()
async def gelexamples(ctx):
    """Sends the examples."""
    message = examples
    await ctx.send(message)


@bot.command()
async def gelratings(ctx):
    """Sends information about ratings."""
    message = ratings
    await ctx.send(message)


@bot.command()
async def pic(ctx, *tags):
    """Calls get_gelImage() with tags specified by user, then sends an image."""
    if "rq" in tags or "re" in tags:
        if ctx.channel.is_nsfw():  # check if channel is suitable for given rating
            img = get_gelImage(tags)
            return await ctx.send(img)

        else:
            message = "For rating questionable or explicit NSFW channel is required!"
            return await ctx.send(message)

    img = get_gelImage(tags)
    await ctx.send(img)


#---------------------------[Meme commands]------------------------------------------
 
@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Ritsu meme",url="https://ritsu-shop.000webhostapp.com/", description="Et pef un meme ", color=0xb429ff)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


#------------------------------[Ecchi commande]---------------------------------------
@bot.command()
async def ecchi(ctx):
    ecchiiii = randint(1, 10)
    print(ecchiiii)
    if ecchiiii == 1:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
         
    ⠄⢸⣿⣿⣿⡇⣏⣾⡞⡯⣥⣽⣷⡘⢶⡀⠡⣌⡔⢣⣿⣿⠄⠄⠄⠄⠄⠄
    ⠄⢸⣿⣿⣿⣷⢹⡖⠬⣚⣛⣯⣭⣛⢂⣙⠦⠈⡇⣾⣿⣿⡆⠄⠄⠄⠄⠄
    ⠄⠘⣿⣿⣿⣿⢰⣾⣿⣿⣿⣿⣿⣿⡼⣿⣿⣷⡆⣿⣿⣿⣧⠄⠄⠄⠄⠄
    ⠄⠄⣿⣿⣿⣿⠘⡿⢛⣿⣿⣿⣿⣿⣧⢻⣿⣿⠃⠸⣿⣿⣿⠄⠄⠄⠄⠄
    ⠄⠄⣿⣿⣿⣿⢀⠼⣛⣛⣭⢭⣟⣛⣛⣛⠿⠿⢆⡠⢿⣿⣿⠄⠄⠄⠄⠄
    ⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄⠄⠄⠄⠄
    ⠄⠄⠄⢹⠣⣛⣣⣭⣭⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄⠄⠄
    ⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀⠄⠄
    ⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⣿⡆⠄
    ⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿⣿⠄
    ⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠄
    ⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
    ⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿⣿⠄
    ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄
    ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⡿⢟⣣⣀⡀
    
    
    ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 2:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
        
    
    ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
    ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
    ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
    ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
    ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
    ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
    ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
    ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
    ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
    ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
    ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
    ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
    
        
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 3:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⣿⣯⣿⣟⣟⡼⣿⡼⡿⣷⣿⣿⣿⠽⡟⢋⣿⣿⠘⣼⣷⡟⠻⡿⣷⡼⣝⡿⡾⣿
    ⣿⣿⣿⣿⢁⣵⡇⡟⠀⣿⣿⣿⠇⠀⡇⣴⣿⣿⣧⣿⣿⡇⠀⢣⣿⣷⣀⡏⢻⣿
    ⣿⣿⠿⣿⣿⣿⠷⠁⠀⠛⠛⠋⠀⠂⠹⠿⠿⠿⠿⠿⠉⠁⠀⠘⠛⠛⠛⠃⢸⣯
    ⣿⡇⠀⣄⣀⣀⣈⣁⠈⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠠⠎⠈⠀⣀⣁⣀⣀⡠⠈⠉ 
    ⣿⣯⣽⡿⢟⡿⠿⠛⠛⠿⣶⣄⠀⠀⠀⠀⠀⠀⠈⢠⣴⣾⠛⠛⠿⠻⠛⠿⣷⣶
    ⣿⣿⣿⠀⠀⠀⣿⡿⣶⣿⣫⠉⠀⠀⠀⠀⠀⠀⠀⠈⠰⣿⠿⠾⣿⡇⠀⠀⢺⣿ 
    ⣿⣿⠻⡀⠀⠀⠙⠏⠒⡻⠃⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠐⡓⢚⠟⠁⠀⠀⡾⢫     
    ⣿⣿⠀⠀⡀⠀⠀⡈⣉⡀⡠⣐⣅⣽⣺⣿⣯⡡⣴⣴⣔⣠⣀⣀⡀⢀⡀⡀⠀⣸
    ⣿⣿⣷⣿⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢾⣷⣿
    ⣿⣿⣟⠫⡾⠟⠫⢾⠯⡻⢟⡽⢶⢿⣿⣿⡛⠕⠎⠻⠝⠪⢖⠝⠟⢫⠾⠜⢿⣿
    ⣿⣿⣿⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀⣰⣋⣀⣈⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⢸⣿
    ⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿
    ⣿⣿⣿⣿⣦⡔⠀⠀⠀⠀⠀⠀⢻⣿⡿⣿⣿⢽⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿
    ⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠘⠛⢅⣙⣙⠿⠉⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣅⠀⠓⠀⠀⣀⣠⣴⣺⣿⣿⣿⣿⣿⣿⣿⣿
    
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 4:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⣿⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿   
    ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿   
    ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀   
    ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀   
    ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀   
    ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀   
    ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀   
    ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀   
    ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀   
    ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀   
    ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀   
    ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀   
    ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀   
    ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀   
    ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀
       
        
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 5:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⣿⠟⣽⣿⣿⣿⣿⣿⢣⠟⠋⡜⠄⢸⣿⣿⡟⣬⢁⠠⠁⣤⠄⢰⠄⠇⢻⢸
    ⢏⣾⣿⣿⣿⠿⣟⢁⡴⡀⡜⣠⣶⢸⣿⣿⢃⡇⠂⢁⣶⣦⣅⠈⠇⠄⢸⢸
    ⣹⣿⣿⣿⡗⣾⡟⡜⣵⠃⣴⣿⣿⢸⣿⣿⢸⠘⢰⣿⣿⣿⣿⡀⢱⠄⠨⢸
    ⣿⣿⣿⣿⡇⣿⢁⣾⣿⣾⣿⣿⣿⣿⣸⣿⡎⠐⠒⠚⠛⠛⠿⢧⠄⠄⢠⣼
    ⣿⣿⣿⣿⠃⠿⢸⡿⠭⠭⢽⣿⣿⣿⢂⣿⠃⣤⠄⠄⠄⠄⠄⠄⠄⠄⣿⡾
    ⣼⠏⣿⡏⠄⠄⢠⣤⣶⣶⣾⣿⣿⣟⣾⣾⣼⣿⠒⠄⠄⠄⡠⣴⡄⢠⣿⣵
    ⣳⠄⣿⠄⠄⢣⠸⣹⣿⡟⣻⣿⣿⣿⣿⣿⣿⡿⡻⡖⠦⢤⣔⣯⡅⣼⡿⣹
    ⡿⣼⢸⠄⠄⣷⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣕⡜⡌⡝⡸⠙⣼⠟⢱⠏
    ⡇⣿⣧⡰⡄⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣋⣪⣥⢠⠏⠄
    ⣧⢻⣿⣷⣧⢻⣿⣿⣿⡇⠄⢀⣀⣀⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠄⠄
    ⢹⣼⣿⣿⣿⣧⡻⣿⣿⣇⣴⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣰⠄⠄⠄
    ⣼⡟⡟⣿⢸⣿⣿⣝⢿⣿⣾⣿⣿⣿⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⡀⡀
    ⣿⢰⣿⢹⢸⣿⣿⣿⣷⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠄⠄⣸⢰⡇
    ⣿⣾⣹⣏⢸⣿⣿⣿⣿⣿⣷⣍⡻⣛⣛⣛⡉⠁⠄⠄⠄⠄⠄⠄⢀⢇⡏⠄
    

        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 6:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⣿⣿⣷⡁⢆⠈⠕⢕⢂⢕⢂⢕⢂⢔⢂⢕⢄⠂⣂⠂⠆⢂⢕⢂⢕⢂⢕⢂⢕⢂
    ⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕
    ⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂
    ⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂
    ⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔
    ⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿
    ⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿
    ⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⠋⠐⢉⢍⢄⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈
    ⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠠⠈
    ⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⢋⢜⠠⠈
    ⠄⠁⠕⢝⡢⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣕⣑⣑⣑⣵⣿⣿⣿⡿⢋⢔⢕⣿⠠⠈
    ⠨⡂⡀⢑⢕⡅⠂⠄⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⢔⢕⢕⣿⣿⠠⠈
    ⠄⠪⣂⠁⢕⠆⠄⠂⠄⠁⡀⠂⡀⠄⢈⠉⢍⢛⢛⢛⢋⢔⢕⢕⢕⣽⣿⣿⠠⠈
      
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 7:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
           
    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠠⠄⠤⠐⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠢⠤⣀⠀⠀⠀
⠀⠀⠀⠀⢀⠤⣖⣶⣭⣷⣼⣄⠁⠀⠀⠀⠀⠀⠀⢐⣫⣭⣴⣶⣦⢄⠀⠀⠀⠀
⠀⠀⠀⣪⣿⣿⣿⠿⢿⣿⣿⠻⣄⠀⠀⠀⠀⠀⢀⣼⠿⠿⢿⣿⣿⣿⣧⡀⠀⠀
⠀⠀⣩⣿⣿⡟⣿⣠⣼⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠁⢸⣤⣼⣿⣿⠻⣿⣿⠀⠀
⠀⢀⣿⣿⡟⠀⠹⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠏⠀⢹⣿⡄⠀
⠀⠈⢿⣿⡃⠀⠀⠀⠉⢁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⠈⠀⠀⠀⢰⠟⡇⠀
⠀⠀⠀⠉⠗⠖⠀⠊⠉⠉⠁⠀⠀⠀⠀⠀⠀⠰⠀⠀⠈⠙⠛⠒⠀⠐⠆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣒⣢⣤⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣝⠿⣿⣿⣿⣿⣿⠿⣻⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀
    

        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')
    
    if ecchiiii == 8:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⢀⠍⠙⢿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠹⣿⣿⣿⣿⣿⣿⣿⠁⠈⢀⡤⢲⣾⣗⠲⣿⣿⣿⣿⣿⣿⣟⠻
    ⡀⢙⣿⣿⣿⣿⣿⣿⢀⠰⠁⢰⣾⣿⣿⡇⢀⣿⣿⣿⣿⣿⣿⡄
    ⣇⢀⢀⠙⠷⣍⠛⠛⢀⢀⢀⢀⠙⠋⠉⢀⢀⢸⣿⣿⣿⣿⣿⣷
    ⡙⠆⢀⣀⠤⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⣿⣿⣿⣿
    ⣷⣖⠋⠁⢀⢀⢀⢀⢀⢀⣀⣀⣄⢀⢀⢀⢀⢸⠏⣿⣿⣿⢿⣿
    ⣿⣷⡀⢀⢀⢀⢀⢀⡒⠉⠉⢀⢀⢀⢀⢀⢀⢈⣴⣿⣿⡿⢀⡿
    ⣿⣿⣷⣄⢀⢀⢀⢀⠐⠄⢀⢀⢀⠈⢀⣀⣴⣿⣿⣿⡿⠁⢀⣡
    ⠻⣿⣿⣿⣿⣆⠢⣤⣄⢀⢀⣀⠠⢴⣾⣿⣿⡿⢋⠟⢡⣿⣿⣿
    ⢀⠘⠿⣿⣿⣿⣦⣹⣿⣀⣀⣀⣀⠘⠛⠋⠁⡀⣄⣴⣿⣿⣿⣿
    ⢀⢀⢀⠈⠛⣽⣿⣿⣿⣿⣿⣿⠁⢀⢀⢀⣡⣾⣿⣿⣿⡟⣹⣿
    ⢀⢀⢀⢀⢰⣿⣿⣿⣿⣿⣿⣿⣦⣤⣶⣿⡿⢛⢿⡇⠟⠰⣿⣿
    ⢀⢀⢀⢀⣿⣿⣿⡿⢉⣭⢭⠏⣿⡿⢸⡏⣼⣿⢴⡇⢸⣿⣶⣿
    ⢀⢀⢀⢰⣿⣿⣿⢃⣶⣶⡏⠸⠟⣱⣿⣧⣛⣣⢾⣿⣿⣿⣿⣿
    ⢀⢀⢀⣾⣿⣿⣿⣾⣿⣿⠟⢻⡿⡉⣷⣬⡛⣵⣿⣿⣿⣿⣿⣿
    ⢀⢀⣸⣿⣿⣿⣿⣿⣿⡿⢰⠘⣰⣇⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿
    ⢀⢀⠘⢿⣿⣿⣿⣿⣿⡷⢺⣿⠟⣩⣭⣽⣇⠲⠶⣿⣿⣿⣿⣿
    ⢀⠐⢀⣾⣿⣿⣿⣿⠟⢐⡈⣿⣷⣶⠎⣹⡟⠟⣛⣸⣿⣿⣿⣿
    ⠠⢀⣼⣿⣿⣿⣿⣯⣼⣿⣷⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    
 
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 9:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    
    ⣿⢸⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⢿⣿⡇⡇⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⠄⢸⣿
    ⡟⢸⣿⣿⣭⣭⡭⣼⣶⣿⣿⣿⣿⢸⣧⣇⠇⢸⣿⣿⠈⣿⣿⣿⣿⣿⣿⡆⠘⣿
    ⡇⢸⣿⣿⣿⣿⡇⣻⡿⣿⣿⡟⣿⢸⣿⣿⠇⡆⣝⠿⡌⣸⣿⣿⣿⣿⣿⡇⠄⣿
    ⢣⢾⣾⣷⣾⣽⣻⣿⣇⣿⣿⣧⣿⢸⣿⣿⡆⢸⣹⣿⣆⢥⢛⡿⣿⣿⣿⡇⠄⣿
    ⣛⡓⣉⠉⠙⠻⢿⣿⣿⣟⣻⠿⣹⡏⣿⣿⣧⢸⣧⣿⣿⣨⡟⣿⣿⣿⣿⡇⠄⣿
    ⠸⣷⣹⣿⠄⠄⠄⠄⠘⢿⣿⣿⣯⣳⣿⣭⣽⢼⣿⣜⣿⣇⣷⡹⣿⣿⣿⠁⢰⣿
    ⠄⢻⣷⣿⡄⢈⠿⠇⢸⣿⣿⣿⣿⣿⣿⣟⠛⠲⢯⣿⣒⡾⣼⣷⡹⣿⣿⠄⣼⣿
    ⡄⢸⣿⣿⣷⣬⣽⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⢀⠉⠙⠛⠛⠳⠽⠿⢠⣿⣿
    ⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢄⣹⡿⠃⠄⠄⣰⠎⡈⣾⣿⣿
    ⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣽⣖⣄⣴⣯⣾⢷⣿⣿⣿
    ⣧⠸⣿⣿⣿⣿⣿⣿⠯⠊⠙⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⣿⣿
    ⣿⣦⠹⣿⣿⣿⣿⣿⠄⢀⣴⢾⣼⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣿⣿⣿⣿
    ⣿⣿⣇⢽⣿⣿⣿⡏⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⡿⣿⣛⣻⠿⣟⣼⣿⣿⣿⣿⢃
    ⣿⣿⣿⡎⣷⣽⠻⣇⣿⣿⣿⡿⣟⣵⣿⣟⣽⣾⣿⣿⣿⣿⢯⣾⣿⣿⣿⠟⠱⡟
    ⣿⣿⣿⣿⢹⣿⣿⢮⣚⡛⠒⠛⢛⣋⣶⣿⣿⣿⣿⣿⣟⣱⠿⣿⣿⠟⣡⣺⢿ 
    
    ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

    if ecchiiii == 10:
        embed = discord.Embed(title= 'Ritsu Bot', url='https://ritsu-shop.000webhostapp.com/', description=f'''
    ###########################################
    #⡿⠋⠄⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠻⣿⣿#
    #⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿#
    #⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹#
    #⣿⣿⡟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣮⠛⣿⣿⣿⣿⣿⣿⡆#
    #⡟⢻⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠄⡀⢬⣭⣻⣷⡌⢿⣿⣿⣿⣿⣿#
    #⠃⣸⡀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣆⢹⣿⣿⣿⡈⢿⣿⣿⣿⣿#
    #⠄⢻⡇⠄⢛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠹⣿⣆⠸⣆⠙⠛⠛⠃⠘⣿⣿⣿⣿#
    #⠄⠸⣡⠄⡈⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⣠⣉⣤⣴⣿⣿⠿⠿⠿⡇⢸⣿⣿⣿#
    #⠄⡄⢿⣆⠰⡘⢿⣿⠿⢛⣉⣥⣴⣶⣿⣿⣿⣿⣻⠟⣉⣤⣶⣶⣾⣿⡄⣿⡿⢸#
    #⠄⢰⠸⣿⠄⢳⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⡇⢻⡇⢸#
    #⢷⡈⢣⣡⣶⠿⠟⠛⠓⣚⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⠇⠘#
    #⡀⣌⠄⠻⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⢿⣿⣿⣿⣿⣿⡟⠘⠄⠄#
    #⣷⡘⣷⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡋⢀⣠⣤⣶⣶⣾⡆⣿⣿⣿⠟⠁⠄⠄⠄⠄#
    #⣿⣷⡘⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⣿⣷⡿⠟⠉⠄⠄⠄⠄⡄⢀#
    #⣿⣿⣷⡈⢷⡀⠙⠛⠻⠿⠿⠿⠿⠿⠷⠾⠿⠟⣛⣋⣥⣶⣄⠄⢀⣄⠹⣦⢹⣿#
    ###########################################
        ''', color=0xb429ff)
        if ctx.channel.is_nsfw():
            await ctx.send(embed = embed)
        else:
            await ctx.send('Vous devez être dans un salon NSFW pour cette commande')

#--------------------------------[Level system]---------------------------------------------

#-------------------------------------------------------------------------------------------

#-----------------------[Gif system]------------------------------------

@bot.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.purple())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=wqoVrsN7V692nghEYwPvug2r6hSxCgAp=10')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=wqoVrsN7V692nghEYwPvug2r6hSxCgAp&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.send(embed=embed)


#-----------------------[mute]------------------------------------

async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command(name='mute')
@commands.has_role(role)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")


@bot.command(name='unmute')
@commands.has_role(role)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")
    
#------------------------[Fin du programme anti mot pas gentil]---------------------------------------------
@bot.command()
async def coucou(ctx):          # Permet d'envoyé une commande dans le serveur 
    print("coucou")
    await ctx.send("coucou ! Moi c'est Ritsu ! ^^")
#-------------------------------------------------------------------------------------------


@bot.command()
async def serverInfo(ctx): #nom de la commande a dire
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    NumberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description              
    numberOfPoeple = server.member_count
    serverName = server.name

    embed = discord.Embed(title = "Ritsu Bot" , url="https://ritsu-shop.000webhostapp.com/", description=f'''

                    ===[Voici les Informations server]===

    ===========================[{serverName}]===========================

    
    
    {serverDescription}

    

    ======[Information supplémentaire]======

    Il y a {numberOfPoeple} de membres dans le serveurs
    Il y a {numberOfTextChannels} channels écrit
    Il y a {NumberOfVoiceChannels} channels vocaux

    ======[Informations supplémentaire]======
    
    ''', color=0xb429ff)
    
    embed.set_thumbnail(url = "https://zupimages.net/up/20/49/gnd7.png")
    embed.add_field(name = "Ritsu Project", value="2020", inline=False)
    embed.set_footer(text = "Si besoin intéresser contacter -> ristu.contact.team@gmail.com")
    embed.set_image(url='https://i.pinimg.com/originals/34/6f/ef/346fefc41ed36dc38f58cf9a1b0f1b22.gif')
    await ctx.send(embed = embed)      
  
#--------------------[Ritsu description with embed]----------------------------


@bot.command()
async def Ritsu(ctx):
    print("Ritsu Bot")
    embed = discord.Embed(title = "Ritsu Bot" , url="https://ritsu-shop.000webhostapp.com/", description=f"""  

    [+] Le programme Ritsu est opérationnel 
    
    [+] Merci de ne pas abuser de ce bot 


    Le bot Discord Ritsu vient du projet réalisé par deux jeunes créateurs.

    Ceux-ci m'ont créé pour que je sois universel (besoin que d'un seul bot), 

    et à la disposition de tout le monde (prix très bas...) !

    Tu peux également aller visiter notre site en cliquant sur "Ritsu Bot" ou grace à ce lien https://ritsu-shop.000webhostapp.com/ 
    
    """, color=0xb429ff)
    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com")
    await ctx.send(embed = embed)      #affiche le programme Ritsu et des emotes
    


#-------------------------------------------------------------------------------------------


@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))             
#-------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
@bot.command()
async def aide(ctx):                            # liens du site a rajouter
    embed=discord.Embed(title="Ritsu Bot ", url="https://ritsu-shop.000webhostapp.com/", description=f""" 
    [+] Voici le menu d'aide de commande de notre bot              
     
    [+] En cas de bug veuillez contacter ---->                      
     
    ===[Commande 1]===                 
    {prefix}aide -> pour demander de l'aide   

    ===[Commande 2]===                
    {prefix}coucou -> affiche une message coucou  

    ===[Commande 3]===                 
    {prefix}sayCh -> transforme vos caractère en caractère chinois 

    ===[Commande 4]===                 
    {prefix}say -> faire parler le bot ( merci de ne pas en abuser ! )  

    ===[Commande 5]===                 
    {prefix}serverInfo -> donne les informations server            

    ===[Commande 6]===                 
    {prefix}unban + id -> permet de dé ban une personne bannie du serveur 

    ===[Commande 7]===                 
    {prefix}Ritsu -> Donne accès aux informations Ritsu          

    ===[Commande 8]===                 
    {prefix}soutiens -> Permet d'afficher des moyens de soutenir Alex'B channel  

    ===[Commande 9]===                 
    {prefix}contact -> affiche les contact du créateur           

    ===[Commande 10]===                 
    {prefix}MH -> affiche le menu d'aide pour les musiques

    ===[Commande 11]===
    {prefix}ecchi -> affiche du ecchi en dot art (une chance sur dix d'avoir le bonus)

    ===[Commande 12]===
    {prefix}pic rs (description) -> affiche du contenu safe 

    ===[Commande 13]===
    {prefix}pic rq (description) -> affiche du contenu questionable

    ===[Commande 14]===
    {prefix}pic re (description) -> affiche du contenu explicit

    ===[commande 15]
    {prefix}meme -> vous affiche un meme au hasard

    """, color=0xb429ff)
    
    
    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")

    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    
    await ctx.send(embed=embed)
 
                                                         #image qui va avec le menu des commandes 
    
#---------------------------------[Menu Musique aide]---------------------------------------
@bot.command()
async def MH(ctx):
    embed=discord.Embed(title="Ritsu Bot ", url="https://ritsu-shop.000webhostapp.com/", description=f"""     
    
    [+] Bienvenue dans le menu d'aide pour la musique      
    
    ===[Commande 1]===     
    {prefix}join -> Fsais venir le bot dans un salon ou vous êtes   

    ===[Commande 2]===     
    {prefix}play -> Vous permets de jouer un sons [ATTENTION veuillez utiliser un url !]   

    ===[Commande 3]===     
    {prefix}skip -> Vous permets de skip une musique  

    ===[Commande 4]===     
    {prefix}loop -> Permet de jouer une musique ne boucle   

    ===[Commande 5]===     
    {prefix}leave -> Permet de déconnecter le bot d'un channel

    ===[Commande 6]===     
    {prefix}volume -> Vous permet de gèrer le volume du bot    

    ===[Commande 7]===     
    {prefix}summon + channel -> Vous permet d'invoquer le bot dans un channel bien précis  

    ===[Commande 8]===     
    {prefix}remove + sons dans la file d'attente -> Permet de retirer un sons de la file d'attente  

    ===[Commande 9]===     
    {prefix}now -> Affiche la musique qui est en train d'être diffusée  

    ===[Commande 10]===     
    {prefix}queue -> Affiche la file d'attente pour jouer une musique 

    ===[Commande 11]===     
    {prefix}shuffle -> Permet de mélanger la file d'attente
    
    ===[Commande 12]===
    {prefix}pause -> merpet de mettre la musique en pause

    ===[Commande 13]===
    {prefix}resume -> permet de re mettre la musique qui à été mise en pause 
    
    """, color=0xb429ff)


    embed.set_thumbnail(url="https://zupimages.net/up/20/06/3fgf.gif")
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ou visiter notre site https://ritsu-shop.000webhostapp.com/ ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)
    


#---------------------------[Menu Admin]-----------------------------------------


@bot.command(name='AdminMenu')
@commands.has_role(role)
async def AdminMenu(ctx):
    embed=discord.Embed(title="Ritsu Bot ", url="", description=(f"""

    [+] Bienvenue dans le menu des commandes Administrateurs  

    ===[Commande 1]===     
    {prefix}del + nombre -> permet de clear des messages 

    ===[Commande 2]===     
    {prefix}bansId -> affiche les id des utilisateurs bannis du serveur

     ===[Commande 3]===     
    {prefix}ban utilisateur + raison  

     ===[Commande 4]===    
    {prefix}kick utilisateur + raison 
    
    ===[Commande 5]===
    {prefix}mute + mention + raison

    ===[Commande 6]===
    {prefix}unmute + mention + raison 

    ===[Commande 7]===
    {prefix}genServerRp + génère un début de serv RP 

    ===[Commande 8]===
    {prefix}genRoleRp -> génère les roles pour le serv Rp

    ===[Commande 9]===
    {prefix}warn + memebres + raison -> war n un membre

    ===[Commande 10]===
    {prefix}warnings + membre -> affiche les warn d'un membre
    
    """), color=0xff0000)

    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_footer(text="Si besoin intéresser contacter ->  ristu.contact.team@gmail.com  ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------


@bot.command()
async def sayCh(ctx, *text):
    chineeseChar = '丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙'
    chineeseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")                    
                transformed = chineeseChar[index]                   # commande d'écriture chinoise 
                chineeseText.append(transformed)
            else:
                chineeseText.append(char)
        chineeseText.append(" ")
    print(chineeseText)
    await ctx.send(" ".join(chineeseText))


# ------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------


@bot.command(name='kick')
@commands.has_role(role)
async def kick(ctx, user : discord.User, *reason):
    embed = discord.Embed(title = "Ritsu Bot", description = (f"""
    
    Un Administrateurs à frapper !
    
    {user} à été kick 
    
    """),color=0xff0000)
    
    embed.set_footer(text="Si besoin intéresser contacter ->  ristu.contact.team@gmail.com  ")
    reason = " ".join(reason)
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    await ctx.guild.kick(user, reason = reason)  
    await ctx.send(embed=embed)

                                                  # commande de kick
    

#-------------------------------------------------------------------------------------------

@bot.command(name='ban')
@commands.has_role(role)
async def ban(ctx, user : discord.User, *reason,):  #https://www.vhv.rs/dpng/d/464-4640395_anime-ban-hammer-png-download-ban-hammer-emoji.png
    embed = discord.Embed(title = "Ritsu Bot", description = (f"""
    Un administrateur à frapper du 

    {user} à été bannis pour la raison de : {reason}

     """),color=0xff0000)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)                   # commande de ban 
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_thumbnail(url="https://www.vhv.rs/dpng/d/464-4640395_anime-ban-hammer-png-download-ban-hammer-emoji.png") #image marteau de ban
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------


@bot.command(name='unban')
@commands.has_role(role)
async def unban(ctx, user : discord.User,*reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans() 
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:                      # commande de déban 
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} à été unban")
            return
    await ctx.send(f"```L'utilisateur {user} n'est pas dans la liste de de bans```")
#-------------------------------[Permet de signaler un bug]--------------------------------------------


#indisponible pour le moment...



#-----------------------------------[Permet de voir les id bannie]-----------------------------------------

@bot.command(name='bandsId')
@commands.has_role(role)
async def bansId(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("```La liste des id des utilisateurs bannius du serveurs est :```")            #affiche la liste des personnes bannie sur le serveur 
    await ctx.send("\n".join(ids))


#-------------------------------------------------------------------------------------------
@bot.command()
async def contact(ctx):                 #permet d'afficher les contacts de Alex
    embed = discord.Embed(title="Ritsu Bot",url="https://ritsu-shop.000webhostapp.com/", description=f"""
    ============[Site :]===========
    https://ritsu-shop.000webhostapp.com/

    ============[Contact :]===========
    ritsu.contact.team@gmail.com


    """,color=0xb429ff)

    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_footer(text="Si besoin intéresser contacter ->  ristu.contact.team@gmail.com - https://ritsu-shop.000webhostapp.com/ ")
    await ctx.send(embed=embed)

@bot.command()
async def soutiens(ctx):                # permet d'afficher les moyens de soutenir Alex 
    embed = discord.Embed(title="Ritsu Bot",url="https://ritsu-shop.000webhostapp.com/", description=f"""
    ============[Site internet :]===========

    https://ritsu-shop.000webhostapp.com/

    ============[Soutiens :]===========

    Tu peux mettre notre site dans ton statut !
                        OU
    Tu peux mettre notre servveur dans ton status

    ============[Soutiens :]===========

    Tu peux mettre le liens de notre serveur dans ton statut !
    https://ritsu-shop.000webhostapp.com/

    ============[Fin de la liste]===========

    ============[Fin de la liste]===========
    """, color=0xb429ff)

    embed.set_thumbnail(url="https://zupimages.net/up/20/49/gnd7.png")
    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    embed.set_footer(text="Si besoin intéresser contacter ->  ristu.contact.team@gmail.com - https://ritsu-shop.000webhostapp.com/ ")
    await ctx.send(embed=embed)
#---------------------================[Début du code pour la musique]================----------------------
#                  

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)
    
    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('Vous êtes connecter a aucun channel vocaux ou vous avez mal écrit le channel a rejoindre !')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Aucun sons est jouer en se moment ')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Le son du joueur à été mis à {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())



    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Les vote pour skip son ajouter, actuellement à **{}/3**'.format(total_votes))

        else:
            await ctx.send('Vous avez déjà voter pour skip')

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('Vous n êtes pas connecter dans un channel vocal !')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Le bot est déjà dans un channel !')


bot.add_cog(Music(bot))


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@bot.command(pass_context = True)
@commands.has_role(role)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await client.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@bot.command(pass_context = True)
@commands.has_role(role)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await ctx.send(f"{user.name} has never been reported")  
"""
@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await client.send_message(ctx.message.channel, text)  
"""

# addrole command
@bot.command(pass_context=True)
async def addrole(ctx, member: discord.Member, *, role):
    """Add a role to a user (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.add_roles(member, role)
        embed = discord.Embed(title="Role added", description="Role was added!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await ctx.send(embed=embed)


# removerole command
@bot.command(pass_context=True)
async def removerole(ctx, member: discord.Member, *, role):
    """Remove a role (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="Role removed", description="Role was removed!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await ctx.send(embed=embed)


# slap command
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://m.popkey.co/08a7fe/VelWq_s-200x150.gif")
    await ctx.send(embed=embed)

# punch command
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
    await ctx.send(embed=embed)


# shoot command
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Shoot someone."""
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await ctx.send(embed=embed)

# cookie command
@bot.command(pass_context=True)
async def cookie(ctx, member: discord.Member):
    """Give a cookie to someone."""
    embed = discord.Embed(title="Nom nom nom!", description="**{1}** gave a cookie to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x176cd5)
    await ctx.send(embed=embed)



# cat command
@bot.command(pass_context=True)
async def cat(ctx):
    embed = discord.Embed(title="Meow!", description=" ", color=0x176cd5)
    embed.set_image(url="http://thecatapi.com/api/images/get?format=src&type=png")
    await ctx.send(embed=embed)

# duck command
@bot.command(pass_context=True)
async def duck(ctx):
    embed = discord.Embed(title="Quack!", description=" ", color=0x176cd5)
    embed.set_image(url="https://random-d.uk/api/v1/randomimg")
    await ctx.send(embed=embed)



# 8ball command
@bot.command(pass_context=True, name='8ball', aliases=['eightball'])
async def _8ball(ctx, *, question):
    responses = ["That is a resounding no" , "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "Reply hazy, try again"]
    embed=discord.Embed(title="The magic 8 ball has spoken.", color=0x176cd5)
    embed.add_field(name="Question", value=question, inline=True)
    embed.add_field(name="Answer", value=random.choice(responses), inline=True)
    await ctx.send(embed=embed)

@bot.command(name='del')
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.administrator):
        await ctx.message.delete()
        embed=discord.Embed(title="__Yui.Error__", description="La commande demande d'avoir une permission spéciale.", color=000000,  timestamp=datetime.now())
        embed.set_author(name="", url="")
        embed.set_image(url="")
        embed.set_footer(text="Commande faite par : {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
        #await ctx.send(f"La commande demande d'avoir une permission spéciale.")
        return
    ammount = amount+1
    if amount > 501:
        embed=discord.Embed(title="__Yui.Error__", description="Je ne peux pas supprimer plus de **500 messages**.", color=000000,  timestamp=datetime.now())
        embed.set_author(name="", url="")
        embed.set_image(url="")
        embed.set_footer(text="La commande a été faite par: :  {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
        #await ctx.send(f"Je ne peux pas supprimer plus de 500 messages.")
    else:
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title="__Mayuko__", description="{} messages vient d'être supprimer.".format(amount), color=000000,  timestamp=datetime.now())
        embed.set_author(name="", url="")
        embed.set_image(url="https://zupimages.net/up/20/06/3fgf.gif")
        embed.set_footer(text="La commande a été faite par: :  {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
        #await ctx.send(f"{amount} messages vient d'être supprimer.")
    z = time.localtime()
    current=time.strftime("%H:%M:%S",z)
    print("----------------------")
    print("la commande del a été faite par : {}".format(ctx.author), current)
    print("ayant l'id : {}".format(ctx.author.id))


@bot.command()
async def genServerRp(ctx):
    staff = "STAFF"
    imp = "IMPORTANT"
    voc = "VOCALES"
    cmd = "COMMANDES BOTS"
    pub = "PUBLIC"
    frp = "FICHES RP"
    RP = "ROLEPLAY"
    lyc = "LYCÉE 🏫"
    lyce1 = "LYCÉE ETGAE 1 "
    lyce2 = "LYCÉE ETAGE 2"
    toit = "TOIT"
    df = "DORTOIRS FEMME"
    dh = "DORTOIR HOMME"
    tdd = "TOI DU DORTOIR"
    acv = "AYUMI : CENTRE VILLE"
    ab = "AYUMI : BANLIEUE"
    ahv = "AYUMI : HORS VILLE"
    

    category1 = await ctx.guild.create_category(staff)
    category2 = await ctx.guild.create_category(imp)
    category3 = await ctx.guild.create_category(voc)
    category4 = await ctx.guild.create_category(cmd)
    category5 = await ctx.guild.create_category(pub)
    category6 = await ctx.guild.create_category(frp)
    category7 = await ctx.guild.create_category(RP)
    category8 = await ctx.guild.create_category(lyc)
    category9 = await ctx.guild.create_category(lyce1)
    category10 = await ctx.guild.create_category(lyce2)
    category11 = await ctx.guild.create_category(toit)
    category12 = await ctx.guild.create_category(df)
    category13 = await ctx.guild.create_category(dh)
    category14 = await ctx.guild.create_category(tdd)
    category15 = await ctx.guild.create_category(acv)
    category16 = await ctx.guild.create_category(ab)
    category1ddd = await ctx.guild.create_category(ahv)
    #catégorie 1
    await ctx.guild.create_text_channel(f"général-staff", category=category1)
    await ctx.guild.create_voice_channel(f"Vocal Staff", category=category1)
    #catégorie 2 
    await ctx.guild.create_text_channel(f"règlement-📜", category=category2)
    await ctx.guild.create_text_channel(f"contexte-📖", category=category2)
    await ctx.guild.create_text_channel(f"annonce-📢", category=category2)
    await ctx.guild.create_text_channel(f"événements-🎉", category=category2)
    #catégorie 3
    await ctx.guild.create_text_channel(f"Yui", category=category3)
    await ctx.guild.create_voice_channel(f"🎵-groovy-🎵", category=category3)
    await ctx.guild.create_voice_channel(f"🎵-rythm-🎵", category=category3)
    await ctx.guild.create_voice_channel(f"🕴-tupperbox-🕴", category=category3)
    await ctx.guild.create_voice_channel(f"🏆-rank🏆", category=category3)
    #catégorie 4 
    await ctx.guild.create_text_channel(f"général-💬", category=category4)
    await ctx.guild.create_text_channel(f"images-📸", category=category4)
    await ctx.guild.create_text_channel(f"commandes-💻", category=category4)
    await ctx.guild.create_text_channel(f"questions-❓", category=category4)
    await ctx.guild.create_text_channel(f"suggestion-➕", category=category4)
    await ctx.guild.create_text_channel(f"⛔-𝙽𝚂𝙵𝚆-⛔", category=category4)
    #catégorie 5
    await ctx.guild.create_text_channel(f"no-micro-🔇", category=category5)
    await ctx.guild.create_voice_channel(f"🔉Vocal 2🔉", category=category5)
    await ctx.guild.create_voice_channel(f"Voc Solo 😔", category=category5)
    await ctx.guild.create_voice_channel(f"Vocal Duo ✌", category=category5)
    await ctx.guild.create_voice_channel(f"🥂 Voc Trio 🥂", category=category5)
    #catégorie 6 
    await ctx.guild.create_texte_channel(f"exemple-fiche-📄", category=category6)
    await ctx.guild.create_texte_channel(f"📗-salon-fiche-1-📗", category=category6)
    await ctx.guild.create_texte_channel(f"📘-salon-fiche-2-📘", category=category6)
    await ctx.guild.create_texte_channel(f"📙-salon-fiche-3-📙", category=category6)
    await ctx.guild.create_texte_channel(f"📕-salon-fiche-4-📕", category=category6)
    #catégorie7
    await ctx.guild.create_texte_channel(f"portail-dentrée", category=category7)
    await ctx.guild.create_texte_channel(f"allée-devant-le-lycée", category=category7)
    await ctx.guild.create_voice_channel(f"entrée-du-bâtiment", category=category7)
    await ctx.guild.create_voice_channel(f"salle-de-permanence", category=category7)
    await ctx.guild.create_voice_channel(f"bibliothèque", category=category7)
    await ctx.guild.create_voice_channel(f"cafétéria", category=category7)
    await ctx.guild.create_voice_channel(f"self", category=category7)
    #catégorie8
    await ctx.guild.create_voice_channel(f"𝑆𝑎𝑙𝑙𝑒-𝐷𝑒-𝐶𝑙𝑎𝑠𝑠𝑒-1", category=category8)
    await ctx.guild.create_voice_channel(f"𝑆𝑎𝑙𝑙𝑒-𝐷𝑒-𝐶𝑙𝑎𝑠𝑠𝑒-2", category=category8)
    await ctx.guild.create_voice_channel(f"𝑆𝑎𝑙𝑙𝑒-𝐷𝑒-𝐶𝑙𝑎𝑠𝑠𝑒-3", category=category8)
    await ctx.guild.create_voice_channel(f"𝐵𝑢𝑟𝑒𝑎𝑢-𝐷𝑢-𝑃𝑟𝑖𝑛𝑐𝑖𝑝𝑎𝑙𝑒", category=category8)
    await ctx.guild.create_voice_channel(f"𝐿𝑜𝑔𝑒-𝐷𝑢-𝐺𝑎𝑟𝑑𝑖𝑒𝑛", category=category8)
    await ctx.guild.create_voice_channel(f"𝐵𝑢𝑟𝑒𝑎𝑢-𝐷𝑒-𝐿𝑎-𝑉𝑖𝑒-𝑆𝑐𝑜𝑙𝑎𝑖𝑟𝑒", category=category8)
    #catégorie9
    await ctx.guild.create_voice_channel(f"club-d-art-martiaux", category=category9)
    await ctx.guild.create_voice_channel(f"club-de-cuisine", category=category9)
    await ctx.guild.create_voice_channel(f"club-de-jeu-vidéo", category=category9)
    await ctx.guild.create_voice_channel(f"club-de-photo", category=category9)
    await ctx.guild.create_voice_channel(f"club", category=category9)
    await ctx.guild.create_voice_channel(f"club", category=category9)
    #catégorie10
    await ctx.guild.create_voice_channel(f"toit-nord", category=category10)
    await ctx.guild.create_voice_channel(f"toit-sud", category=category10)
    #catégorie11
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-1-🛏", category=category11)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-2-🛏", category=category11)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-3-🛏", category=category11)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-4-🛏", category=category11)
    #catégorie12
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-1-🛏", category=category12)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-2-🛏", category=category12)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-3-🛏", category=category12)
    await ctx.guild.create_voice_channel(f"𝐶ℎ𝑎𝑚𝑏𝑟𝑒-4-🛏", category=category12)
    #categorie13
    await ctx.guild.create_voice_channel(f"𝑇𝑜𝑖𝑡-𝐶𝑜̂𝑡𝑒́-𝐹𝑒𝑚𝑚𝑒", category=category13)
    await ctx.guild.create_voice_channel(f"𝑇𝑜𝑖𝑡-𝐶𝑜̂𝑡𝑒́-𝐻𝑜𝑚𝑚𝑒", category=category13)
    #catégorie14
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-1-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-2-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-3-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-4-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-5-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-6-🏠", category=category14)
    await ctx.guild.create_voice_channel(f"𝐻𝑎𝑏𝑖𝑡𝑎𝑡𝑖𝑜𝑛-7-🏠", category=category14)
    #categorie15
    await ctx.guild.create_voice_channel(f"𝑀𝑒𝑟", category=category15)
    await ctx.guild.create_voice_channel(f"𝐹𝑜𝑟𝑒̂𝑡", category=category15)
    await ctx.guild.create_voice_channel(f"𝑀𝑜𝑛𝑡𝑎𝑔𝑛𝑒", category=category15)
    



@bot.command()
@commands.has_role(role)
async def genRoleRp(ctx):
    try:
        guild = ctx.guild
        await guild.create_role(name="Fondateurs")
        await guild.create_role(name="Membres")
        await guild.create_role(name="Admin")
        await guild.create_role(name="Sans-Fiche")
        await guild.create_role(name="Communautaire")
        await guild.create_role(name="Bots")
        await guild.create_role(name="Rp")
        await guild.create_role(name="Fille")
        await guild.create_role(name="Garçon")

    except Exception as errors:
        print('bot Error : {errors}')


@bot.command()
@commands.has_role(role)
async def setup_counter(ctx):
    try:
        guild = client.get_guild(816713276993568859) # <-- insert yor guild id here
        await ctx.send("Setting up management!")
        category = await ctx.guild.create_category("Management", overwrites=None, reason=None)
        await ctx.guild.create_voice_channel(f"Member Count: {ctx.guild.member_count}", overwrites=None, category=category, reason=None)
        await ctx.send("Setup finished!")
    except Exception as errors:
        print(f"Bot Error: {errors}")

@bot.command()
async def onlinebot(ctx):
    date = datetime.now()
    await ctx.message.delete()
    embed=discord.Embed(title="Bot Online ", url="", description=(f""" 

    Bot Online and Ready to use
    {date}


    """), color=0xff0000)

    embed.set_thumbnail(url="https://www.icone-png.com/png/54/53901.png")

    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)

@bot.command()
async def offlinebot(ctx):
    date = datetime.now()
    await ctx.message.delete()
    embed=discord.Embed(title="Bot Offline ", url="", description=(f""" 


    Bot is offline  
    {date}


    """), color=0xff0000)

    embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/133/385/png-clipart-computer-icons-xchng-open-philippine-red-cross-logo-logo-cross.png")

    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)
    sys.exit()

@bot.command()
async def maintenancebot(ctx):
    date = datetime.now()
    await ctx.message.delete()
    embed=discord.Embed(title="Maintenance du Bot ", url="", description=(f""" 

    @everyone
    Bot en maintenance. Merci de ne pas l'utiliser sous peine de sanction
    {date}


    """), color=0xff0000)

    embed.set_thumbnail(url="https://www.pinclipart.com/picdir/middle/74-741814_exclamation-mark-png-icone-point-d-exclamation-orange.png")

    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)



role3 = "unverified" 


@bot.command()
async def roll(ctx):
    rollnumber = randint(0, 100)
    await ctx.send(f"{ctx.author.display_name} Votre résultat est de {rollnumber} ")
  


@bot.command()
async def hug(ctx, memeber: discord.Member):
    
    url = random.choice(embedlinks.messages)

    embed = discord.Embed(title="CALIN", description=f"**{1}** hugs **{0}**!", color=0xff0000)
    embed.image(url=url)
    embed.set_thumbnail(url="https://zupimages.net/up/20/06/3fgf.gif")
    embed.add_field(name="Ritsu Project", value="2020", inline=False) 
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    await ctx.send(embed=embed)
"""
@bot.command()
async def album(ctx):
    r = requests.get(f"https://api.imgur.com/3/album/{album_id}/images?client_id={imgur_key}").json()
    em = discord.Embed(title="Album")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))

"""


@bot.command()
async def restartbot(ctx):
    date = datetime.now()
    await ctx.message.delete()
    embed=discord.Embed(title="Bot Restart ", url="", description=(f""" 


    Bot Restart   
    {date}


    """), color=0xff0000)

    embed.set_thumbnail(url="https://www.pinclipart.com/picdir/middle/74-741814_exclamation-mark-png-icone-point-d-exclamation-orange.png")

    embed.add_field(name="Ritsu Project", value="2020", inline=False)
    
    embed.set_footer(text="Si besoin intéresser contacter -> ristu.contact.team@gmail.com ")
    embed.set_image(url='https://zupimages.net/up/20/06/3fgf.gif')
    await ctx.send(embed=embed)
    subprocess.run("python restart.py")
    time.sleep(5)
    sys.exit()



#-------------------------------------------------------------------------------------------

bot.run("ODE1Mjg3MTI3ODE3ODQ2ODQ1.G76Dzc._HTGb1d6XQFPbsds6TTFeONck2G5d-HT-yDv4Q") # permet de lancer le bot 

