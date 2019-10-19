import discord
from discord.ext import commands
import os
import traceback
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
   


@bot.command()
async def date(ctx):
    now = datetime.now().strftime('%m/%d')
    await ctx.send(now)

@bot.command()
async def cid(ctx):
    category_id = ctx.channel.category_id
    await ctx.send(category_id)

@bot.command()
async def mkch(ctx):
    category_id = ctx.channel.category_id
    category = ctx.guild.get_channel(category_id)
    now = datetime.now().strftime('%m月%d日')
    new_channel = await category.create_text_channel(name=now)
    reply = f'{new_channel.mention} を作成しました'
    await ctx.send(reply)

bot.run(token)
