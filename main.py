import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # If the bot is the sender
  if message.author == client.user:
      return  
  if message.channel.name.lower() == "help":
    # Process NLP here
    # Call Charity API here
    # Return local retailer details here
    await message.channel.send('Hello!')

client.run(os.getenv("TOKEN"))