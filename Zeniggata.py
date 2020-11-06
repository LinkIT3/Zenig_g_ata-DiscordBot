import discord
from discord.ext import commands
import random

token = 'Njk1Mjg2OTIxODYxMDA1Mzc2.XoX-Zw.yv-P2GSs22o6Mu940Rd_mS3mJ9c'

prefix=""

client = commands.Bot(command_prefix = "z.")

prefix=client.command_prefix

@client.event                                                                           #bot ready
async def on_ready():
    print('Bot is ready.')

@client.event                                                                           #member join
async def on_member_join(member):                                                     
    print(f'{member}, che gay')

@client.event                                                                           #member remove
async def on_member_remove(member):
    print(f'{member}, pisciaturo')

@client.command()                                                                       #ping message
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()                                                                       #change prefix
async def prefix(ctx, pref):
    client.command_prefix=pref
    if client.command_prefix==pref:
        await ctx.send(f'{pref} is the new prefix!')
        prefix=pref
    else:
        await ctx.send(f'Error, the prefix is yet {prefix}')

@client.command()                                                                       #delete messages
async def delete(ctx, amount=10):
    amount+=1
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['8ball', 'test'])                                              #8ball
async def _8ball(ctx, *, question):
    responses = ['Si', 'No', 'È sicuro', 'Manco per il ca']

    await ctx.send(f'{random.choice(responses)}')

@client.command()                                                                       #Elon Musk pic
async def elon(ctx):
    await ctx.send(f'https://i.imgur.com/qGzaoXB.png')

client.run(token)