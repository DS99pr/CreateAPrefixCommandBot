# i must admit that I literally copied this code from the previous repository, and modified it (named "CreateABotThatReactsToMessages")

import discord # importing the Discord library, use "pip install discord" or "conda install discord" to install it
from discord.ext import commands

intents = discord.Intents.default() # setting the intents the bot will be able to use, check it in the Discord Developers Portal so that the bot can send messages, etc.
intents.message_content = True # allowing the bot to send messages

bot = commands.Bot(
  command_prefix="?", # the "command_prefix" parameter is the prefix of our commands
  intents=intents # assign intents to the bot
) # creating a bot instance, it is responsible for the application

@bot.event # decorator "@bot.event" allows you to listen for events
async def on_ready(): # we use an asynchronous "on_ready" function, it is executed when the bot is ready
   print("bot is ready") # sending a log, you can do anything else here, but if you want to do something related to the Discord API, use "await" before the command

@bot.command(name="ping") # creating a command called "ping", it will be called like this: "?ping"
async def pingCommand(ctx: commands.Context): # creating an asynchronous "pingCommand" function, you can add any name here, just make sure it's alphanumeric. The context in this case refers to the channel or the caller of the command (author)
   await ctx.send("Pong!") # asynchronous sending of messages to the channel. "ctx.send" is equal to "message.channel.send", but "ctx" is not the same as "message.channel", because it depends on how you use it.
   # after executing the "?ping" command, the bot responds with "Pong!" if it has "message_content" intentions assigned.

bot.run("token") # replace the "token" with your token from the "Bot" tab in the Discord Developers Portal, and give it here (as a string), remember not to share it with ANYONEawa
