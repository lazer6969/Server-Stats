import discord
from discord.ext import commands

client = commands.Bot(command_prefix="PREFIX",help_command=None)

@client.event 
async def on_ready():
    print("Bot is online")
    
@client.command()
async def ping(ctx):
    await ctx.send("Pong!)
                   
@client.command()
async def commandname(ctx):
    await ctx.send("Response")
                   
@client.command()
async def newcommand(ctx):
    await ctx.send("Response")
                   
client.run("TOKEN_HERE)
