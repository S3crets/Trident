import discord
import asyncio
client = discord.Client()
from discord import Game
import discord.ext import commands
from discord.ext.commands import bot


      
@client.event
async def on_ready():
      print("Logged in as:")
      print(client.user.name)
      print("ID:")
      print(client.user.id)
      print("Ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!ping"):
        await client.send_message(message.channel, "Pong!")

@client.event
async def on_message(message):
       if message.content.startswith ("!embed"):
             em = discord.Embed(title="Invite your friends using this link!", description= "https://discord.gg/Ekgycs5", colour=0x00ff6e)


             
           



             await client.send_message(message.channel,  embed=em)


@client.event
async def on_ready():
      await client.change_presence(game=Game(name="$tacked trident games"))
      print ("Running...")

#@client.event
#sync def on_message(message):




 






            


            



 

        
        

      


       
      





client.run("NTY5MjU1NDQxMDA4MTY0ODc2.XPqtgg.Fo4xy7gKc_c0c3hbE27p-oib9qo")



 






            


            



 

        
        

      


       
      








            


            



 

        
        

      


       
      









            


            



 

        
        

      


       
      





