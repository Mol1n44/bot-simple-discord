#Library
import discord
from discord.ext import commands
import asyncio


bot=commands.Bot(intents=discord.Intents.all() , command_prefix='!') 
#The "command_prefix" is a symbol, so your bot's commands will work. Example = "!hello"


#   Commands example #

@bot.command()
async def hello(ctx):      #HELLO is a command.
    await ctx.send("text")
@bot.command()           
async def bye(ctx):        #BYE is a command.
    await ctx.send("text")
@bot.command()  
async def laugh(ctx):      #LAUGH is a command.
    await ctx.send("text")
@bot.command()
async def cry(ctx):        #CRY is a command.
    await ctx.send("text")    




#  Command for repeat a word #
@bot.command()
async def say(ctx, *, arg): #"Say" is the command.
    await ctx.send(arg)

#   Send messages to a especifyc channel  #

@bot.command(pass_context=True)
async def saygen(ctx, *, arg): # "Saygen" is the command.
    channel = bot.get_channel(10101010) #ID from channel.
    await channel.send(arg)

#   Events    #
@bot.event 
async def on_ready():
    print("On") #  When the bot is running it will print the word "On" to the terminal.


#Run 
bot.run("") #Put her the token of ur bot.