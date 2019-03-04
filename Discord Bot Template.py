import discord, asyncio, time
import urllib.request, urllib.parse, re
from discord.ext.commands import Bot
from discord.ext import commands
from threading import Thread

#SETTINGS-----------------------------------------------------------------------
botID               = ""    #Add the bot token here (Google it, you need one)
symb                = "_"   #The symbol used to define the start of a command

#GLOBAL VARIABLES---------------------------------------------------------------
client = discord.Client()

#THREADS------------------------------------------------------------------------
@asyncio.coroutine
def clock(interval): #Cal this with "asyncio.async(clock(1))"
    #CODE HERE THAT HAPPENS EVERY SECOND

    #Sleep for the required seconds   
    yield from asyncio.sleep(interval)
    asyncio.async(clock(interval))

#EVENTS-------------------------------------------------------------------------
@client.event
async def on_ready(): #CODE HERE WHEN BOT TURNS ON
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message): #CODE HERE WHEN A PERSON SENDS A MESSAGE
    dat = message.content.split(" ")
    message = " ".join(dat[1:].)
        
    #Message based
    if dat[0].lower() == symb+"ping": #If the first word of the message was the ping command
        await client.send_message(message.channel, "**Pong**") #Send pong

    #Add you code here
    #if dat[0].lower == symb+"[command call]:
        #Do stuff here (idk, read the API at:
        #http://discordpy.readthedocs.io/en/latest/api.html

#RUN----------------------------------------------------------------------------
asyncio.async(clock(1))
client.run(botID)
