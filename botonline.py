import discord
from discord.ext import commands
import json

intents=discord.Intents.default()
intents.members=True
intents.typing=False
intents.presences=False



with open('set.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

#呼教機器人命令字首
bot=commands.Bot(command_prefix='喵',intents=intents)


@bot.event
async def on_ready():
    print('>> Bot is online<<')
#加入
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(940941583610675241)
    await channel.send(f"{member}join!")
    
#離開
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(940941620461842432)
    await channel.send(f"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

@bot.command()
async def 喵(ctx):
    await ctx.send('喵')







bot.run(jdata['TOKEN'])