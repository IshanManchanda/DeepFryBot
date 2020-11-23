import logging
from os import environ

import discord
from dotenv import load_dotenv

from bin.helpers import fry_helper
from bin.utils.logs import log_info

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
	log_info(f'Message from {message.author}: {message.content}')

	if message.author == client.user:
		return

	# TODO: Enable frying embeds as well
	if len(message.embeds):
		print(f'Found {len(message.embeds)} embeds')
		print(message.embeds[0].url)

	if len(message.attachments):
		# TODO: Send channel typing update
		# with message.channel.typing:
		await fry_helper(message)

	if message.content.lower().startswith('!ping'):
		log_info('Ping')
		await message.channel.send(f'Pong! Latency: {client.latency}')


client.run(TOKEN)
