from bin.fryer import fry_image
from bin.utils.text import keys


async def fry_helper(message):
	print(f'Found {len(message.attachments)} attachments')

	for attachment in message.attachments:
		print('Attachment found:', attachment.url)
		args = {key: 1 if key in message.content else 0 for key in keys}
		await fry_image(message, attachment, 1, args)

		# bio = BytesIO()

		# bio =
		# bio.name = filename
		# bio.save()
		# await attachment.save(f'temp/{attachment.filename}')
		# print('Downloaded attachment')
