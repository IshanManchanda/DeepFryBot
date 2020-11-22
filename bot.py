from os import environ

import discord
from dotenv import load_dotenv

if 'DISCORD_TOKEN' not in environ:
	load_dotenv()
TOKEN = environ.get('DISCORD_TOKEN')


class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run(TOKEN)
