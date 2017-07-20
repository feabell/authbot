import discord
import asyncio
from discord.ext import commands
import random
import yaml
import logging


logging.basicConfig(filename='authbot.log', level=logging.INFO)

config = yaml.load(open('authbot.conf', 'r'))
BOT_TOKEN = config['BOT_TOKEN']

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
@asyncio.coroutine 
def on_ready():
    logging.info('Logged in as')
    logging.info(bot.user.name)
    logging.info(bot.user.id)
    logging.info('------')

@bot.event
@asyncio.coroutine
def on_message(message):

   if message.content.startswith('!authme'):
      #open a private conversation
      logging.info("[LOG] !authme received from " + str(message.author))
      
      content = """Thankyou for authing to the WiNGSPAN Discord Service!

Before we continue, please make sure that you have provided your email to 
Discord (from the "User Settings" cog at the bottom left) and are connected to Discord 
using the same email address that you provided to 

      <https://services.torpedodelivery.com>

and that you have clicked the link sent to you by discord to verify your account.

Once you have verified this.  Please type !getonwithit"""
      yield from bot.send_message(message.author, content) 

   if message.content.startswith('!getonwithit'):
      #getting on with it
      logging.info("[LOG] !getonwithit received from " + str(message.author))

      content = """Please click the following link to authorise me to access 
your email account details:

     <https://services.torpedodelivery.com/discordauth>

You will be redirected to the services.torpedodelivery.com site, and everything
should just happen automagically from there!"""

      yield from bot.send_message(message.author, content) 

bot.run(BOT_TOKEN)
