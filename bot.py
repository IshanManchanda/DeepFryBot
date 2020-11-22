import logging
from os import environ

import discord
from dotenv import load_dotenv

from bin.helpers import fry_helper

if 'DISCORD_TOKEN' not in environ:
	load_dotenv()
TOKEN = environ.get('DISCORD_TOKEN')

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
handler.setFormatter(
	logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
)
logger.addHandler(handler)


@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	print('Message from {0.author}: {0.content}'.format(message))

	if message.author == client.user:
		return

	if len(message.embeds):
		print(f'Found {len(message.embeds)} embeds')
		print(message.embeds[0].url)

	if len(message.attachments):
		# with message.channel.typing:
		await fry_helper(message)

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')


client.run(TOKEN)
