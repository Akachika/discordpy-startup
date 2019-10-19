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


@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
   


@bot.command()
async def date(ctx):
    now = datetime.now().strftime('%m/%d')
    await ctx.send(now)
bot.run(token)
