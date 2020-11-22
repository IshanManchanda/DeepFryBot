from bin.fryer import fry_image


async def fry_helper(message):
	print(f'Found {len(message.attachments)} attachments')

	for attachment in message.attachments:
		print('Attachment found:', attachment.url)
		await fry_image(message, attachment)

		# bio = BytesIO()

		# bio =
		# bio.name = filename
		# bio.save()
		# await attachment.save(f'temp/{attachment.filename}')
		# print('Downloaded attachment')
