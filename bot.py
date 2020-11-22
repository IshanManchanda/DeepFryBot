from os import environ

import discord
from dotenv import load_dotenv

if 'DISCORD_TOKEN' not in environ:
	load_dotenv()
TOKEN = environ.get('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	print('Message from {0.author}: {0.content}'.format(message))

	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')


client.run(TOKEN)
