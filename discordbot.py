import discord
from discord.ext import commands
import os
import traceback
import datetime

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
    nowNum = datetime.datetime.now()
    await ctx.send(nowNum)
    nowStr = datetime.datetime.strftime(nowNum,'%m月%d日')
    await ctx.send(nowStr)
    nowNum += datetime.timedelta(days=10)
    nowStr = datetime.datetime.strftime(nowNum,'%m月%d日')
    await ctx.send(nowStr)

@bot.command()
async def cid(ctx):
    category_id = ctx.channel.category_id
    await ctx.send(category_id)

@bot.command()
async def mkch(ctx):
    category_id = ctx.channel.category_id
    category = ctx.guild.get_channel(category_id)
    now = datetime.datetime.now().strftime('%m月%d日')
    new_channel = await category.create_text_channel(name=now)
    reply = f'{new_channel.mention} を作成しました'
    await ctx.send(reply)

@bot.command()
async def weekch(ctx):
    category_id = ctx.channel.category_id  ##634406237395746816 団体戦のカテゴリID
    category = ctx.guild.get_channel(category_id)
    nowNum = datetime.datetime.now()
    for i in range(7):  
        nowNum += datetime.timedelta(days=1)
        nnowStr = datetime.datetime.strftime(nowNum,'%m月%d日')
        await ctx.send(nowStr)
    await ctx.send(nowStr)
    ##    new_channel = await category.create_text_channel(name=now)
    ##    reply = f'{new_channel.mention} を作成しました'
    ##await ctx.send(reply)
   
bot.run(token)
