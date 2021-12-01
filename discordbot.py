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
    await ctx.send(ctx.channel.category_id)
    await ctx.send(ctx.channel.id)
    await ctx.send('今回もモブでした')

@bot.command()
async def mkch(ctx):
    category_id = ctx.channel.category_id
    category = ctx.guild.get_channel(category_id)
    now = datetime.datetime.now().strftime('%m月%d日')
    await category.create_text_channel(name=now)
 

@bot.command()
async def weekch(ctx):
    category_id = ctx.channel.category_id  ##914751704535298058　日程調整のチャンネルID
    category = ctx.guild.get_channel(category_id)
    nowNum = datetime.datetime.now()
    weekday = nowNum.weekday()
    if weekday < 5:
        nowNum -= datetime.timedelta(days=weekday)
        await ctx.send('今週のチャンネルを作成します')
    elif weekday == 5:
        nowNum += datetime.timedelta(days=2)
        await ctx.send('次週のチャンネルを作成します')
    else:
        nowNum += datetime.timedelta(days=1)
        await ctx.send('次週のチャンネルを作成します')
    for i in range(7):
        nowStr = datetime.datetime.strftime(nowNum,'%m月%d日')
        new_channel = await category.create_text_channel(name=nowStr)
        reply = f'{new_channel.mention} までを作成しました'
        nowNum += datetime.timedelta(days=1)
    await ctx.send(reply)

@bot.command()
async def nxtweek(ctx, arg):
    ##pollChannelId = '914751704535298058' ##日程調整のチャンネルID
    ##pollChannel = ctx.guild.get_channel(pollChannelId)
    nowNum = datetime.datetime.now()
    weekday = nowNum.weekday()
    
    poll = '日程調整W'
    poll += arg
    await ctx.send(poll)

    date = nowNum
    if weekday < 5:
        date -= datetime.timedelta(days=weekday)
        await ctx.send('今週の試合を設定をします')
    elif weekday == 5:
        date += datetime.timedelta(days=2)
        await ctx.send('次週の試合を設定します')
    else:
        date += datetime.timedelta(days=1)
        await ctx.send('次週の試合を設定します')
    for i in range(7):
        strDate = datetime.datetime.strftime(date,'. %m月%d日(%a)')
        Out = str(i+1) + strDate
        msg = await ctx.send(Out)
        
        for reaction in ['⭕', '❌', '❓']:
            await msg.add_reaction(reaction)
        date += datetime.timedelta(days=1)


bot.run(token)
